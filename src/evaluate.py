"""Config-driven evaluation scaffold for supervised and linear-probe models."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision.datasets import FakeData

from src.augmentations import CIFAR10_IMAGE_SIZE, build_eval_transform
from src.datasets import build_cifar10_dataset
from src.train_linear_probe import LinearProbe, load_encoder_from_simclr_checkpoint
from src.train_supervised import SupervisedResNet18
from src.utils import ensure_dir, get_device, load_yaml_config, set_seed


SUPPORTED_MODES = {"supervised", "linear_probe"}


def _checkpoint_config(config: dict[str, Any]) -> dict[str, Any]:
    checkpoint = config.get("checkpoint", {})
    if not isinstance(checkpoint, dict):
        raise ValueError("checkpoint must be a mapping")
    return checkpoint


def _required_checkpoint_path(config: dict[str, Any], *keys: str) -> Path:
    checkpoint = _checkpoint_config(config)
    for key in keys:
        candidate = checkpoint.get(key)
        if candidate:
            return Path(candidate).expanduser()

    legacy_candidate = config.get("checkpoint_path")
    if legacy_candidate and "path" in keys:
        return Path(legacy_candidate).expanduser()

    joined_keys = ", ".join(f"checkpoint.{key}" for key in keys)
    raise ValueError(f"missing required checkpoint path; expected one of: {joined_keys}")


def _primary_checkpoint_path(config: dict[str, Any]) -> Path:
    mode = str(config.get("mode", "")).strip().lower()
    if mode == "supervised":
        return _required_checkpoint_path(config, "path", "supervised_path")
    if mode == "linear_probe":
        return _required_checkpoint_path(config, "path", "linear_probe_path")
    return _required_checkpoint_path(config, "path")


def _simclr_checkpoint_provenance(config: dict[str, Any]) -> str:
    mode = str(config.get("mode", "")).strip().lower()
    if mode != "linear_probe":
        return ""

    checkpoint = _checkpoint_config(config)
    simclr_path = checkpoint.get("simclr_path")
    if not simclr_path:
        raise ValueError("checkpoint.simclr_path is required for linear_probe evaluation provenance")
    return str(simclr_path)


def get_dataset_split(config: dict[str, Any]) -> str:
    """Return the evaluation split label recorded with result provenance."""

    dataset_config = config.get("dataset", {})
    dataset_name = str(dataset_config.get("name", "fake")).strip().lower()
    if dataset_name == "fake":
        return "fake"
    if dataset_name == "cifar10":
        return "train" if bool(dataset_config.get("train", False)) else "test"
    raise ValueError("dataset.name must be one of {'fake', 'cifar10'}")


def _load_checkpoint(path: Path, expected_key: str) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"checkpoint not found: {path}")

    checkpoint = torch.load(path, map_location="cpu", weights_only=False)
    if not isinstance(checkpoint, dict):
        raise ValueError(f"checkpoint must be a mapping: {path}")
    if expected_key not in checkpoint:
        raise ValueError(f"checkpoint {path} must contain {expected_key!r}")
    return checkpoint


def build_evaluation_dataset(config: dict[str, Any]):
    """Build labeled fake or CIFAR-10 data for evaluation."""

    dataset_config = config.get("dataset", {})
    dataset_name = str(dataset_config.get("name", "fake")).strip().lower()

    if dataset_name == "fake":
        image_size = tuple(dataset_config.get("image_size", [3, CIFAR10_IMAGE_SIZE, CIFAR10_IMAGE_SIZE]))
        return FakeData(
            size=int(dataset_config.get("size", 16)),
            image_size=image_size,
            num_classes=int(dataset_config.get("num_classes", 10)),
            transform=build_eval_transform(),
        )

    if dataset_name == "cifar10":
        data_root = dataset_config.get("data_root")
        if data_root is None:
            raise ValueError("dataset.data_root is required when dataset.name is 'cifar10'")
        return build_cifar10_dataset(
            data_root=data_root,
            train=bool(dataset_config.get("train", False)),
            download=bool(dataset_config.get("download", False)),
            contrastive=False,
            augmentation_strength=dataset_config.get("augmentation_strength", "weak"),
        )

    raise ValueError("dataset.name must be one of {'fake', 'cifar10'}")


def build_data_loader(config: dict[str, Any]) -> DataLoader:
    evaluation_config = config.get("evaluation", {})
    dataset = build_evaluation_dataset(config)
    return DataLoader(
        dataset,
        batch_size=int(evaluation_config.get("batch_size", config.get("batch_size", 128))),
        shuffle=bool(evaluation_config.get("shuffle", config.get("shuffle", False))),
        num_workers=int(evaluation_config.get("num_workers", config.get("num_workers", 0))),
        drop_last=False,
    )


def build_supervised_model(config: dict[str, Any]) -> nn.Module:
    """Load a supervised checkpoint from train_supervised.py format.

    Expected checkpoint key: ``model_state_dict``. It contains the full
    ``SupervisedResNet18`` state, including ``encoder.*`` and ``classifier.*``.
    """

    model_config = config.get("model", {})
    model = SupervisedResNet18(
        feature_dim=int(model_config.get("feature_dim", 512)),
        num_classes=int(model_config.get("num_classes", 10)),
    )
    checkpoint_path = _required_checkpoint_path(config, "path", "supervised_path")
    checkpoint = _load_checkpoint(checkpoint_path, expected_key="model_state_dict")
    model.load_state_dict(checkpoint["model_state_dict"])
    return model


def build_linear_probe_model(config: dict[str, Any]) -> nn.Module:
    """Load a linear-probe checkpoint from train_linear_probe.py format.

    Expected checkpoint keys:
    - ``checkpoint.path`` points to the linear-probe checkpoint with
      ``classifier_state_dict``.
    - ``checkpoint.simclr_path`` points to the SimCLR checkpoint with
      ``model_state_dict`` so the frozen encoder can be reconstructed.

    The linear-probe training checkpoint stores only classifier weights.
    """

    model_config = config.get("model", {})
    simclr_path = _required_checkpoint_path(config, "simclr_path")
    encoder = load_encoder_from_simclr_checkpoint(simclr_path)
    model = LinearProbe(
        encoder=encoder,
        feature_dim=int(model_config.get("feature_dim", 512)),
        num_classes=int(model_config.get("num_classes", 10)),
    )

    checkpoint_path = _required_checkpoint_path(config, "path", "linear_probe_path")
    checkpoint = _load_checkpoint(checkpoint_path, expected_key="classifier_state_dict")
    model.classifier.load_state_dict(checkpoint["classifier_state_dict"])
    return model


def build_evaluation_model(config: dict[str, Any]) -> nn.Module:
    mode = str(config.get("mode", "")).strip().lower()
    if mode == "supervised":
        return build_supervised_model(config)
    if mode == "linear_probe":
        return build_linear_probe_model(config)
    raise ValueError(f"mode must be one of {sorted(SUPPORTED_MODES)}, got {mode!r}")


@torch.inference_mode()
def compute_top1_accuracy(
    model: nn.Module,
    data_loader: DataLoader,
    device: torch.device,
    max_batches: int | None = None,
) -> tuple[float, int, int]:
    """Compute Top-1 accuracy for a labeled image dataset."""

    model.eval()
    correct = 0
    total = 0

    for batch_index, (images, targets) in enumerate(data_loader, start=1):
        if max_batches is not None and batch_index > max_batches:
            break

        images = images.to(device)
        targets = targets.to(device)
        logits = model(images)
        predictions = logits.argmax(dim=1)
        correct += int((predictions == targets).sum().item())
        total += int(targets.numel())

    if total == 0:
        raise RuntimeError("evaluation ran over zero examples")

    return correct / total, correct, total


def write_evaluation_result(path: str | Path, result: dict[str, Any]) -> Path:
    """Write a small CSV or Markdown evaluation result file."""

    output_path = Path(path).expanduser()
    ensure_dir(output_path.parent)
    row = {
        "mode": result["mode"],
        "dataset": result["dataset"],
        "dataset_split": result["dataset_split"],
        "top1_accuracy": result["top1_accuracy"],
        "correct": result["correct"],
        "total": result["total"],
        "checkpoint_path": result["checkpoint_path"],
        "simclr_checkpoint_path": result["simclr_checkpoint_path"],
    }

    if output_path.suffix.lower() == ".md":
        simclr_checkpoint_path = row["simclr_checkpoint_path"]
        simclr_checkpoint_cell = f"`{simclr_checkpoint_path}`" if simclr_checkpoint_path else ""
        lines = [
            (
                "| mode | dataset | dataset_split | top1_accuracy | correct | total | "
                "checkpoint_path | simclr_checkpoint_path |"
            ),
            "|---|---|---|---:|---:|---:|---|---|",
            (
                f"| {row['mode']} | {row['dataset']} | {row['dataset_split']} | "
                f"{row['top1_accuracy']} | {row['correct']} | {row['total']} | "
                f"`{row['checkpoint_path']}` | {simclr_checkpoint_cell} |"
            ),
            "",
        ]
        output_path.write_text("\n".join(lines), encoding="utf-8")
        return output_path

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row.keys()))
        writer.writeheader()
        writer.writerow(row)
    return output_path


def run_evaluation(config_or_path: dict[str, Any] | str | Path) -> dict[str, Any]:
    """Run config-driven Top-1 evaluation without saving model weights."""

    if isinstance(config_or_path, dict):
        config = config_or_path
    else:
        config = load_yaml_config(config_or_path)

    set_seed(config.get("seed", 0))
    device = get_device(config.get("device", "auto"))
    checkpoint_path = _primary_checkpoint_path(config)
    data_loader = build_data_loader(config)
    model = build_evaluation_model(config).to(device)

    evaluation_config = config.get("evaluation", {})
    max_batches = evaluation_config.get("max_batches", config.get("max_batches"))
    max_batches = None if max_batches is None else int(max_batches)
    top1_accuracy, correct, total = compute_top1_accuracy(
        model=model,
        data_loader=data_loader,
        device=device,
        max_batches=max_batches,
    )

    result = {
        "mode": str(config.get("mode")).strip().lower(),
        "dataset": str(config.get("dataset", {}).get("name", "fake")).strip().lower(),
        "dataset_split": get_dataset_split(config),
        "top1_accuracy": float(top1_accuracy),
        "correct": correct,
        "total": total,
        "checkpoint_path": str(checkpoint_path),
        "simclr_checkpoint_path": _simclr_checkpoint_provenance(config),
        "device": str(device),
    }

    output_path = config.get("output_path") or config.get("paths", {}).get("output_path")
    if output_path:
        result["output_path"] = str(write_evaluation_result(output_path, result))

    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate supervised or linear-probe CIFAR-10 checkpoints.")
    parser.add_argument("--config", required=True, help="Path to an evaluation YAML config.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_evaluation(args.config)
    print(
        "completed evaluation: "
        f"mode={result['mode']} "
        f"dataset={result['dataset']} "
        f"top1_accuracy={result['top1_accuracy']:.6f} "
        f"correct={result['correct']} "
        f"total={result['total']}"
    )
    if "output_path" in result:
        print(f"output_path={result['output_path']}")


if __name__ == "__main__":
    main()
