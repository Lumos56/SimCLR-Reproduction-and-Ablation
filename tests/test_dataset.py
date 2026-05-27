from pathlib import Path

import pytest
import torch
from PIL import Image

from src.augmentations import (
    build_cifar10_train_transform,
    build_eval_transform,
    build_simclr_transform,
    build_weak_transform,
)
from src.datasets import TwoCropTransform, build_cifar10_dataset


def make_cifar_image() -> Image.Image:
    return Image.new("RGB", (32, 32), color=(128, 64, 32))


def assert_cifar_tensor(value: torch.Tensor) -> None:
    assert isinstance(value, torch.Tensor)
    assert tuple(value.shape) == (3, 32, 32)


def test_two_crop_transform_returns_two_tensors() -> None:
    transform = TwoCropTransform(build_eval_transform())

    view_a, view_b = transform(make_cifar_image())

    assert_cifar_tensor(view_a)
    assert_cifar_tensor(view_b)


def test_strong_transform_output_shape() -> None:
    transform = build_simclr_transform()

    output = transform(make_cifar_image())

    assert_cifar_tensor(output)


def test_weak_transform_output_shape() -> None:
    transform = build_weak_transform()

    output = transform(make_cifar_image())

    assert_cifar_tensor(output)


def test_eval_transform_output_shape() -> None:
    transform = build_eval_transform()

    output = transform(make_cifar_image())

    assert_cifar_tensor(output)


def test_invalid_augmentation_strength_raises_value_error() -> None:
    with pytest.raises(ValueError, match="augmentation_strength must be one of"):
        build_cifar10_train_transform(augmentation_strength="medium")


def test_augmentation_strength_allows_surrounding_whitespace() -> None:
    output = build_cifar10_train_transform(augmentation_strength=" strong ")(make_cifar_image())

    assert_cifar_tensor(output)


def test_dataset_builder_defaults_to_no_download(monkeypatch: pytest.MonkeyPatch) -> None:
    captured = {}

    class DummyCIFAR10:
        def __init__(self, root, train, transform, download):
            captured["root"] = root
            captured["train"] = train
            captured["transform"] = transform
            captured["download"] = download

    monkeypatch.setattr("src.datasets.CIFAR10", DummyCIFAR10)

    data_root = Path("/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation")
    dataset = build_cifar10_dataset(data_root=data_root, train=True)

    assert isinstance(dataset, DummyCIFAR10)
    assert captured["root"] == str(data_root)
    assert captured["train"] is True
    assert captured["download"] is False
    view_a, view_b = captured["transform"](make_cifar_image())
    assert_cifar_tensor(view_a)
    assert_cifar_tensor(view_b)


def test_dataset_builder_non_contrastive_train_transform(monkeypatch: pytest.MonkeyPatch) -> None:
    captured = {}

    class DummyCIFAR10:
        def __init__(self, root, train, transform, download):
            captured["root"] = root
            captured["train"] = train
            captured["transform"] = transform
            captured["download"] = download

    monkeypatch.setattr("src.datasets.CIFAR10", DummyCIFAR10)

    data_root = Path("/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation")
    dataset = build_cifar10_dataset(
        data_root=data_root,
        train=True,
        contrastive=False,
        augmentation_strength="weak",
    )

    assert isinstance(dataset, DummyCIFAR10)
    assert captured["root"] == str(data_root)
    assert captured["train"] is True
    assert captured["download"] is False
    assert_cifar_tensor(captured["transform"](make_cifar_image()))


def test_dataset_builder_non_contrastive_eval_transform(monkeypatch: pytest.MonkeyPatch) -> None:
    captured = {}

    class DummyCIFAR10:
        def __init__(self, root, train, transform, download):
            captured["root"] = root
            captured["train"] = train
            captured["transform"] = transform
            captured["download"] = download

    monkeypatch.setattr("src.datasets.CIFAR10", DummyCIFAR10)

    data_root = Path("/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation")
    dataset = build_cifar10_dataset(
        data_root=data_root,
        train=False,
        contrastive=False,
        augmentation_strength=" strong ",
    )

    assert isinstance(dataset, DummyCIFAR10)
    assert captured["root"] == str(data_root)
    assert captured["train"] is False
    assert captured["download"] is False
    assert_cifar_tensor(captured["transform"](make_cifar_image()))


def test_dataset_builder_invalid_augmentation_strength_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    class DummyCIFAR10:
        def __init__(self, root, train, transform, download):
            raise AssertionError("CIFAR10 should not be constructed for invalid augmentation strength")

    monkeypatch.setattr("src.datasets.CIFAR10", DummyCIFAR10)

    with pytest.raises(ValueError, match="augmentation_strength must be one of"):
        build_cifar10_dataset(
            data_root="/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation",
            train=False,
            contrastive=False,
            augmentation_strength="medium",
        )
