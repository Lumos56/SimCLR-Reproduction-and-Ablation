"""Dataset builders for CIFAR-10."""

from __future__ import annotations

from pathlib import Path

from torchvision.datasets import CIFAR10

from src.augmentations import (
    TwoCropTransform,
    build_cifar10_train_transform,
    build_eval_transform,
    build_two_crop_transform,
    validate_augmentation_strength,
)


def build_cifar10_dataset(
    data_root: str | Path,
    train: bool,
    download: bool = False,
    contrastive: bool = True,
    augmentation_strength: str = "strong",
) -> CIFAR10:
    """Build a CIFAR-10 dataset without assuming a repository-local data path.

    Args:
        data_root: External CIFAR-10 root directory. This should not be inside
            the repository.
        train: Whether to build the CIFAR-10 train split.
        download: Passed to ``torchvision.datasets.CIFAR10``. Defaults to
            ``False`` to avoid unintended downloads.
        contrastive: If ``True``, return two transformed views per image.
        augmentation_strength: ``"strong"`` for SimCLR or ``"weak"`` for the
            augmentation ablation.
    """

    if data_root is None:
        raise ValueError("data_root must be provided and should point outside the repository")

    root = Path(data_root).expanduser()
    validate_augmentation_strength(augmentation_strength)
    if contrastive:
        transform = build_two_crop_transform(augmentation_strength=augmentation_strength)
    elif train:
        transform = build_cifar10_train_transform(
            augmentation_strength=augmentation_strength,
        )
    else:
        transform = build_eval_transform()

    return CIFAR10(
        root=str(root),
        train=train,
        transform=transform,
        download=download,
    )


__all__ = ["TwoCropTransform", "build_cifar10_dataset"]
