"""Minimal supervised ResNet18 baseline scaffold."""

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

DEFAULT_SUPERVISED_CHECKPOINT_DIR = (
    "/home/yeyee/research/04_models/"
    "SimCLR-Reproduction-and-Ablation/supervised"
)


class SupervisedResNet18(nn.Module):
    """Trainable CIFAR ResNet18 encoder plus a CIFAR-10 classifier head."""

    def __init__(
        self,
        feature_dim: int = 512,
        num_classes: int = 10,
    ) -> None:
        super().__init__()
        self.encoder = CifarResNet18Encoder(feature_dim=feature_dim)
        self.classifier = nn.Linear(feature_dim, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Return class logits for input images shaped ``[B, 3, 32, 32]``."""

        features = self.encoder(x)
        return self.classifier(features)


def build_supervised_dataset(config: dict[str, Any]):
    """Build labeled fake or CIFAR-10 data for supervised smoke runs."""

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


def build_supervised_optimizer(
    model: nn.Module,
    config: dict[str, Any],
) -> torch.optim.Optimizer:
    """Build an optimizer over all supervised model parameters."""

    optimizer_config = config.get("optimizer", {})
    optimizer_name = str(optimizer_config.get("name", "adam")).strip().lower()
    learning_rate = float(optimizer_config.get("lr", 1e-3))
    weight_decay = float(optimizer_config.get("weight_decay", 0.0))

    if optimizer_name == "adam":
        return torch.optim.Adam(
            model.parameters(),
            lr=learning_rate,
            weight_decay=weight_decay,
        )
    if optimizer_name == "sgd":
        return torch.optim.SGD(
            model.parameters(),
            lr=learning_rate,
            momentum=float(optimizer_config.get("momentum", 0.9)),
            weight_decay=weight_decay,
        )
    raise ValueError("optimizer.name must be one of {'adam', 'sgd'}")


def save_supervised_checkpoint(
    path: str | Path,
    model: SupervisedResNet18,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    step: int,
) -> Path:
    """Save a supervised checkpoint to a configured external or test path."""

    checkpoint_path = Path(path).expanduser()
    repo_root = Path(__file__).resolve().parents[1]
    if checkpoint_path.resolve().is_relative_to(repo_root):
        raise ValueError("supervised checkpoints must not be saved inside the repository")

    ensure_dir(checkpoint_path.parent)
    torch.save(
        {
            "epoch": epoch,
            "step": step,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
        },
        checkpoint_path,
    )
    return checkpoint_path


def maybe_save_supervised_checkpoint(
    config: dict[str, Any],
    model: SupervisedResNet18,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    step: int,
) -> Path | None:
    """Save a checkpoint only when explicitly enabled by config."""

    path_config = config.get("paths", {})
    if not bool(path_config.get("save_checkpoint", False)):
        return None

    checkpoint_dir = path_config.get("checkpoint_dir", DEFAULT_SUPERVISED_CHECKPOINT_DIR)
    checkpoint_filename = path_config.get("checkpoint_filename", "supervised_smoke.pt")
    return save_supervised_checkpoint(
        Path(checkpoint_dir) / checkpoint_filename,
        model=model,
        optimizer=optimizer,
        epoch=epoch,
        step=step,
    )


def run_supervised_training(config_or_path: dict[str, Any] | str | Path) -> dict[str, Any]:
    """Run a tiny supervised smoke training loop."""

    if isinstance(config_or_path, dict):
        config = config_or_path
    else:
        config = load_yaml_config(config_or_path)

    set_seed(config.get("seed", 0))
    device = get_device(config.get("device", "auto"))
    model_config = config.get("model", {})
    training_config = config.get("training", {})
    path_config = config.get("paths", {})

    dataset = build_supervised_dataset(config)
    data_loader = DataLoader(
        dataset,
        batch_size=int(training_config.get("batch_size", 4)),
        shuffle=bool(training_config.get("shuffle", True)),
        num_workers=int(training_config.get("num_workers", 0)),
        drop_last=True,
    )

    model = SupervisedResNet18(
        feature_dim=int(model_config.get("feature_dim", 512)),
        num_classes=int(model_config.get("num_classes", 10)),
    ).to(device)
    optimizer = build_supervised_optimizer(model, config)
    loss_fn = nn.CrossEntropyLoss()
    epochs = int(training_config.get("epochs", 1))
    max_train_batches = training_config.get("max_train_batches", 1)
    max_train_batches = None if max_train_batches is None else int(max_train_batches)

    log_dir = ensure_dir(path_config.get("log_dir", "results/logs"))
    log_path = log_dir / path_config.get("log_filename", "supervised_smoke.csv")

    global_step = 0
    final_train_loss = None
    final_train_acc = None
    for epoch in range(1, epochs + 1):
        model.train()
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
        raise RuntimeError("supervised smoke training ran zero optimizer steps")

    saved_checkpoint_path = maybe_save_supervised_checkpoint(
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
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run minimal supervised smoke training.")
    parser.add_argument("--config", required=True, help="Path to a supervised YAML config.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_supervised_training(args.config)
    print(
        "completed supervised smoke training: "
        f"steps={result['steps']} "
        f"final_train_loss={result['final_train_loss']:.6f} "
        f"final_train_acc={result['final_train_acc']:.6f}"
    )
    print(f"log_path={result['log_path']}")
    if result["checkpoint_path"] is not None:
        print(f"checkpoint_path={result['checkpoint_path']}")


if __name__ == "__main__":
    main()
