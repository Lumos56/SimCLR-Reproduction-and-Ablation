"""Minimal config-driven SimCLR smoke training."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import torch
from torch.utils.data import DataLoader
from torchvision.datasets import FakeData

from src.augmentations import CIFAR10_IMAGE_SIZE, build_two_crop_transform
from src.datasets import build_cifar10_dataset
from src.losses import NTXentLoss
from src.models import SimCLR
from src.utils import append_csv_row, ensure_dir, get_device, load_yaml_config, set_seed

DEFAULT_CHECKPOINT_DIR = (
    "/home/yeyee/research/04_models/"
    "SimCLR-Reproduction-and-Ablation/checkpoints"
)


def build_smoke_dataset(config: dict[str, Any]):
    """Build a contrastive dataset for fake or future CIFAR-10 smoke runs."""

    dataset_config = config.get("dataset", {})
    dataset_name = str(dataset_config.get("name", "fake")).strip().lower()
    augmentation_strength = dataset_config.get("augmentation_strength", "strong")

    if dataset_name == "fake":
        image_size = tuple(dataset_config.get("image_size", [3, CIFAR10_IMAGE_SIZE, CIFAR10_IMAGE_SIZE]))
        return FakeData(
            size=int(dataset_config.get("size", 16)),
            image_size=image_size,
            num_classes=int(dataset_config.get("num_classes", 10)),
            transform=build_two_crop_transform(augmentation_strength=augmentation_strength),
        )

    if dataset_name == "cifar10":
        data_root = dataset_config.get("data_root")
        if data_root is None:
            raise ValueError("dataset.data_root is required when dataset.name is 'cifar10'")
        return build_cifar10_dataset(
            data_root=data_root,
            train=bool(dataset_config.get("train", True)),
            download=bool(dataset_config.get("download", False)),
            contrastive=True,
            augmentation_strength=augmentation_strength,
        )

    raise ValueError("dataset.name must be one of {'fake', 'cifar10'}")


def build_optimizer(model: torch.nn.Module, config: dict[str, Any]) -> torch.optim.Optimizer:
    """Build the optimizer selected by config."""

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
        momentum = float(optimizer_config.get("momentum", 0.9))
        return torch.optim.SGD(
            model.parameters(),
            lr=learning_rate,
            momentum=momentum,
            weight_decay=weight_decay,
        )
    raise ValueError("optimizer.name must be one of {'adam', 'sgd'}")


def unpack_two_view_batch(batch) -> tuple[torch.Tensor, torch.Tensor]:
    """Extract two augmented image views from a torchvision dataset batch."""

    views = batch[0] if isinstance(batch, (list, tuple)) else batch
    if not isinstance(views, (list, tuple)) or len(views) != 2:
        raise ValueError("expected each batch to contain two contrastive views")
    return views[0], views[1]


def save_checkpoint(
    path: str | Path,
    model: torch.nn.Module,
    optimizer: torch.optim.Optimizer,
    epoch: int,
    step: int,
) -> Path:
    """Save a small smoke-test checkpoint to the configured path."""

    checkpoint_path = Path(path).expanduser()
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


def run_smoke_training(config_or_path: dict[str, Any] | str | Path) -> dict[str, Any]:
    """Run a tiny SimCLR smoke training loop from a config mapping or YAML path."""

    if isinstance(config_or_path, dict):
        config = config_or_path
    else:
        config = load_yaml_config(config_or_path)

    set_seed(config.get("seed", 0))
    device = get_device(config.get("device", "auto"))
    training_config = config.get("training", {})
    path_config = config.get("paths", {})

    dataset = build_smoke_dataset(config)
    data_loader = DataLoader(
        dataset,
        batch_size=int(training_config.get("batch_size", 4)),
        shuffle=bool(training_config.get("shuffle", True)),
        num_workers=int(training_config.get("num_workers", 0)),
        drop_last=True,
    )

    model = SimCLR().to(device)
    loss_fn = NTXentLoss(temperature=float(training_config.get("temperature", 0.5)))
    optimizer = build_optimizer(model, config)

    epochs = int(training_config.get("epochs", 1))
    max_train_batches = training_config.get("max_train_batches", 1)
    max_train_batches = None if max_train_batches is None else int(max_train_batches)

    log_dir = ensure_dir(path_config.get("log_dir", "results/logs"))
    log_path = log_dir / path_config.get("log_filename", "simclr_smoke.csv")

    # Checkpoints must be configured outside the repository for real runs.
    # Tests override this directory with pytest tmp_path.
    checkpoint_dir = ensure_dir(path_config.get("checkpoint_dir", DEFAULT_CHECKPOINT_DIR))
    checkpoint_path = checkpoint_dir / path_config.get("checkpoint_filename", "simclr_smoke.pt")

    global_step = 0
    final_loss = None
    model.train()
    for epoch in range(1, epochs + 1):
        for batch_index, batch in enumerate(data_loader, start=1):
            if max_train_batches is not None and batch_index > max_train_batches:
                break

            x1, x2 = unpack_two_view_batch(batch)
            x1 = x1.to(device)
            x2 = x2.to(device)

            optimizer.zero_grad(set_to_none=True)
            _, z1 = model(x1)
            _, z2 = model(x2)
            loss = loss_fn(z1, z2)
            if not torch.isfinite(loss):
                raise RuntimeError(f"non-finite loss at epoch={epoch}, step={global_step + 1}")
            loss.backward()
            optimizer.step()

            global_step += 1
            final_loss = float(loss.detach().cpu())
            append_csv_row(
                log_path,
                {
                    "epoch": epoch,
                    "step": global_step,
                    "loss": final_loss,
                },
            )

    if global_step == 0:
        raise RuntimeError("smoke training ran zero optimizer steps")

    saved_checkpoint_path = save_checkpoint(
        checkpoint_path,
        model=model,
        optimizer=optimizer,
        epoch=epochs,
        step=global_step,
    )

    return {
        "steps": global_step,
        "final_loss": final_loss,
        "log_path": str(log_path),
        "checkpoint_path": str(saved_checkpoint_path),
        "device": str(device),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run minimal SimCLR smoke training.")
    parser.add_argument("--config", required=True, help="Path to a SimCLR smoke-training YAML config.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_smoke_training(args.config)
    print(f"completed smoke training: steps={result['steps']} final_loss={result['final_loss']:.6f}")
    print(f"log_path={result['log_path']}")
    print(f"checkpoint_path={result['checkpoint_path']}")


if __name__ == "__main__":
    main()
