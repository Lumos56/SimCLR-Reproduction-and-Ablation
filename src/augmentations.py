"""CIFAR-10 transforms used by the SimCLR data pipeline."""

from __future__ import annotations

from collections.abc import Callable

from PIL import Image
from torch import Tensor
from torchvision import transforms
from torchvision.transforms import InterpolationMode

CIFAR10_MEAN = (0.4914, 0.4822, 0.4465)
CIFAR10_STD = (0.2470, 0.2435, 0.2616)
CIFAR10_IMAGE_SIZE = 32


class TwoCropTransform:
    """Apply one transform twice to produce two independent SimCLR views."""

    def __init__(self, transform: Callable[[Image.Image], Tensor]) -> None:
        self.transform = transform

    def __call__(self, image: Image.Image) -> tuple[Tensor, Tensor]:
        return self.transform(image), self.transform(image)


def _normalize() -> transforms.Normalize:
    return transforms.Normalize(mean=CIFAR10_MEAN, std=CIFAR10_STD)


def validate_augmentation_strength(augmentation_strength: str) -> str:
    normalized = augmentation_strength.strip().lower()
    if normalized not in {"strong", "weak"}:
        raise ValueError(
            "augmentation_strength must be one of {'strong', 'weak'}, "
            f"got {augmentation_strength!r}"
        )
    return normalized


def build_simclr_transform(image_size: int = CIFAR10_IMAGE_SIZE) -> transforms.Compose:
    """Build the strong SimCLR augmentation for CIFAR-10 pretraining."""

    color_jitter = transforms.ColorJitter(
        brightness=0.4,
        contrast=0.4,
        saturation=0.4,
        hue=0.1,
    )
    return transforms.Compose(
        [
            transforms.RandomResizedCrop(
                size=image_size,
                scale=(0.2, 1.0),
                interpolation=InterpolationMode.BICUBIC,
            ),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomApply([color_jitter], p=0.8),
            transforms.RandomGrayscale(p=0.2),
            transforms.RandomApply(
                [transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 2.0))],
                p=0.5,
            ),
            transforms.ToTensor(),
            _normalize(),
        ]
    )


def build_weak_transform(image_size: int = CIFAR10_IMAGE_SIZE) -> transforms.Compose:
    """Build a weaker CIFAR-10 training augmentation for ablation."""

    return transforms.Compose(
        [
            transforms.RandomCrop(size=image_size, padding=4),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.ToTensor(),
            _normalize(),
        ]
    )


def build_eval_transform() -> transforms.Compose:
    """Build the deterministic CIFAR-10 evaluation transform."""

    return transforms.Compose(
        [
            transforms.ToTensor(),
            _normalize(),
        ]
    )


def build_cifar10_train_transform(
    augmentation_strength: str = "strong",
    image_size: int = CIFAR10_IMAGE_SIZE,
) -> transforms.Compose:
    """Build a CIFAR-10 train transform selected by augmentation strength."""

    normalized = validate_augmentation_strength(augmentation_strength)
    if normalized == "strong":
        return build_simclr_transform(image_size=image_size)
    return build_weak_transform(image_size=image_size)


def build_two_crop_transform(
    augmentation_strength: str = "strong",
    image_size: int = CIFAR10_IMAGE_SIZE,
) -> TwoCropTransform:
    """Build a two-crop transform for contrastive CIFAR-10 samples."""

    return TwoCropTransform(
        build_cifar10_train_transform(
            augmentation_strength=augmentation_strength,
            image_size=image_size,
        )
    )
