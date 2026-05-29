"""Minimal linear probe scaffold for frozen SimCLR encoders."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision.datasets import FakeData

from src.augmentations import CIFAR10_IMAGE_SIZE, build_eval_transform
from src.datasets import build_cifar10_dataset
from src.models import CifarResNet18Encoder
from src.utils import append_csv_row, ensure_dir, get_device, load_yaml_config, set_seed

DEFAULT_LINEAR_PROBE_CHECKPOINT_DIR = (
    "/home/yeyee/research/04_models/"
    "SimCLR-Reproduction-and-Ablation/linear_probe"
)
DEFAULT_SIMCLR_CHECKPOINT_PATH = (
    "/home/yeyee/research/04_models/"
    "SimCLR-Reproduction-and-Ablation/checkpoints/cifar10_simclr_smoke.pt"
)


class LinearProbe(nn.Module):
    """Frozen encoder plus trainable linear CIFAR-10 classifier."""

    def __init__(
        self,
        encoder: nn.Module,
        feature_dim: int = 512,
        num_classes: int = 10,
    ) -> None:
        super().__init__()
        self.encoder = encoder
        for parameter in self.encoder.parameters():
            parameter.requires_grad = False
        self.classifier = nn.Linear(feature_dim, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Return classifier logits for input images shaped ``[B, 3, 32, 32]``."""

        self.encoder.eval()
        with torch.no_grad():
            features = self.encoder(x)
        return self.classifier(features)


def build_linear_probe_dataset(config: dict[str, Any]):
    """Build labeled fake or CIFAR-10 data for linear-probe smoke runs."""

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
            train=bool(dataset_config.get("train", True)),
            download=bool(dataset_config.get("download", False)),
            contrastive=False,
            augmentation_strength=dataset_config.get("augmentation_strength", "weak"),
        )

    raise ValueError("dataset.name must be one of {'fake', 'cifar10'}")


def build_classifier_optimizer(
    classifier: nn.Module,
    config: dict[str, Any],
) -> torch.optim.Optimizer:
    """Build an optimizer over classifier parameters only."""

    optimizer_config = config.get("optimizer", {})
    optimizer_name = str(optimizer_config.get("name", "adam")).strip().lower()
    learning_rate = float(optimizer_config.get("lr", 1e-3))
    weight_decay = float(optimizer_config.get("weight_decay", 0.0))

    if optimizer_name == "adam":
        return torch.optim.Adam(
            classifier.parameters(),
            lr=learning_rate,
            weight_decay=weight_decay,
        )
    if optimizer_name == "sgd":
        return torch.optim.SGD(
            classifier.parameters(),
            lr=learning_rate,
            momentum=float(optimizer_config.get("momentum", 0.9)),
            weight_decay=weight_decay,
        )
    raise ValueError("optimizer.name must be one of {'adam', 'sgd'}")


def load_encoder_from_simclr_checkpoint(checkpoint_path: str | Path) -> CifarResNet18Encoder:
    """Load a CIFAR ResNet18 encoder from a SimCLR checkpoint."""

    resolved_path = Path(checkpoint_path).expanduser()
    if not resolved_path.is_file():
        raise FileNotFoundError(f"SimCLR checkpoint not found: {resolved_path}")

    checkpoint = torch.load(resolved_path, map_location="cpu", weights_only=False)
    state_dict = checkpoint.get("model_state_dict", checkpoint)
    if not isinstance(state_dict, dict):
        raise ValueError("SimCLR checkpoint must contain a model state dict")

    encoder_state_dict = {
        key.removeprefix("encoder."): value
        for key, value in state_dict.items()
        if key.startswith("encoder.")
    }
    if not encoder_state_dict:
        raise ValueError("SimCLR checkpoint does not contain encoder weights")

    encoder = CifarResNet18Encoder()
    encoder.load_state_dict(encoder_state_dict)
    return encoder


def clone_state_dict(module: nn.Module) -> dict[str, torch.Tensor]:
    """Clone a module state dict for smoke-test inspection."""

    return {
        key: value.detach().cpu().clone()
        for key, value in module.state_dict().items()
    }


def save_linear_probe_checkpoint(
    path: str | Path,
    model: LinearProbe,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    step: int,
) -> Path:
    """Save a linear-probe checkpoint to a configured external or test path."""

    checkpoint_path = Path(path).expanduser()
    repo_root = Path(__file__).resolve().parents[1]
    if checkpoint_path.resolve().is_relative_to(repo_root):
        raise ValueError("linear probe checkpoints must not be saved inside the repository")

    ensure_dir(checkpoint_path.parent)
    torch.save(
        {
            "epoch": epoch,
            "step": step,
            "classifier_state_dict": model.classifier.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
        },
        checkpoint_path,
    )
    return checkpoint_path


def maybe_save_linear_probe_checkpoint(
    config: dict[str, Any],
    model: LinearProbe,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    step: int,
) -> Path | None:
    """Save a checkpoint only when explicitly enabled by config."""

    path_config = config.get("paths", {})
    if not bool(path_config.get("save_checkpoint", False)):
        return None

    checkpoint_dir = path_config.get("checkpoint_dir", DEFAULT_LINEAR_PROBE_CHECKPOINT_DIR)
    checkpoint_filename = path_config.get("checkpoint_filename", "linear_probe_smoke.pt")
    return save_linear_probe_checkpoint(
        Path(checkpoint_dir) / checkpoint_filename,
        model=model,
        optimizer=optimizer,
        epoch=epoch,
        step=step,
    )


def run_linear_probe_training(config_or_path: dict[str, Any] | str | Path) -> dict[str, Any]:
    """Run a tiny linear-probe smoke training loop."""

    if isinstance(config_or_path, dict):
        config = config_or_path
    else:
        config = load_yaml_config(config_or_path)

    set_seed(config.get("seed", 0))
    device = get_device(config.get("device", "auto"))
    checkpoint_config = config.get("checkpoint", {})
    training_config = config.get("training", {})
    path_config = config.get("paths", {})

    encoder = load_encoder_from_simclr_checkpoint(
        checkpoint_config.get("simclr_path", DEFAULT_SIMCLR_CHECKPOINT_PATH)
    )
    model = LinearProbe(
        encoder=encoder,
        feature_dim=int(config.get("model", {}).get("feature_dim", 512)),
        num_classes=int(config.get("model", {}).get("num_classes", 10)),
    ).to(device)
    initial_classifier_state = clone_state_dict(model.classifier)

    dataset = build_linear_probe_dataset(config)
    data_loader = DataLoader(
        dataset,
        batch_size=int(training_config.get("batch_size", 4)),
        shuffle=bool(training_config.get("shuffle", True)),
        num_workers=int(training_config.get("num_workers", 0)),
        drop_last=True,
    )

    optimizer = build_classifier_optimizer(model.classifier, config)
    loss_fn = nn.CrossEntropyLoss()
    epochs = int(training_config.get("epochs", 1))
    max_train_batches = training_config.get("max_train_batches", 1)
    max_train_batches = None if max_train_batches is None else int(max_train_batches)

    log_dir = ensure_dir(path_config.get("log_dir", "results/logs"))
    log_path = log_dir / path_config.get("log_filename", "linear_probe_smoke.csv")

    global_step = 0
    final_train_loss = None
    final_train_acc = None
    for epoch in range(1, epochs + 1):
        model.train()
        model.encoder.eval()
        for batch_index, (images, targets) in enumerate(data_loader, start=1):
            if max_train_batches is not None and batch_index > max_train_batches:
                break

            images = images.to(device)
            targets = targets.to(device)
            optimizer.zero_grad(set_to_none=True)
            logits = model(images)
            loss = loss_fn(logits, targets)
            if not torch.isfinite(loss):
                raise RuntimeError(f"non-finite loss at epoch={epoch}, step={global_step + 1}")
            loss.backward()
            optimizer.step()

            predictions = logits.argmax(dim=1)
            train_acc = (predictions == targets).float().mean()
            global_step += 1
            final_train_loss = float(loss.detach().cpu())
            final_train_acc = float(train_acc.detach().cpu())
            append_csv_row(
                log_path,
                {
                    "epoch": epoch,
                    "step": global_step,
                    "train_loss": final_train_loss,
                    "train_acc": final_train_acc,
                },
            )

    if global_step == 0:
        raise RuntimeError("linear probe smoke training ran zero optimizer steps")

    saved_checkpoint_path = maybe_save_linear_probe_checkpoint(
        config=config,
        model=model,
        optimizer=optimizer,
        epoch=epochs,
        step=global_step,
    )

    return {
        "steps": global_step,
        "final_train_loss": final_train_loss,
        "final_train_acc": final_train_acc,
        "log_path": str(log_path),
        "checkpoint_path": None if saved_checkpoint_path is None else str(saved_checkpoint_path),
        "device": str(device),
        "model": model,
        "initial_classifier_state": initial_classifier_state,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run minimal linear-probe smoke training.")
    parser.add_argument("--config", required=True, help="Path to a linear-probe YAML config.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_linear_probe_training(args.config)
    print(
        "completed linear probe smoke training: "
        f"steps={result['steps']} "
        f"final_train_loss={result['final_train_loss']:.6f} "
        f"final_train_acc={result['final_train_acc']:.6f}"
    )
    print(f"log_path={result['log_path']}")
    if result["checkpoint_path"] is not None:
        print(f"checkpoint_path={result['checkpoint_path']}")


if __name__ == "__main__":
    main()
