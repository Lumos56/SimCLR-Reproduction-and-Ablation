"""CIFAR-10 ResNet18 encoder."""

from __future__ import annotations

import torch
from torch import nn
from torchvision.models import resnet18


class CifarResNet18Encoder(nn.Module):
    """ResNet18 encoder adapted for 32x32 CIFAR-10 inputs.

    Expected input shape: ``[batch_size, 3, 32, 32]``.
    Output shape: ``[batch_size, 512]``. Torchvision ResNet18's default
    penultimate representation is 512-dimensional, and this encoder keeps that
    feature size explicit.
    """

    def __init__(self, feature_dim: int = 512) -> None:
        super().__init__()
        if feature_dim != 512:
            raise ValueError(
                "CifarResNet18Encoder only supports feature_dim=512 because "
                f"torchvision ResNet18 outputs 512-dimensional features; got {feature_dim}"
            )
        self.feature_dim = feature_dim
        self.backbone = resnet18(weights=None)
        self.backbone.conv1 = nn.Conv2d(
            in_channels=3,
            out_channels=64,
            kernel_size=3,
            stride=1,
            padding=1,
            bias=False,
        )
        self.backbone.maxpool = nn.Identity()
        self.backbone.fc = nn.Identity()

    @property
    def conv1(self) -> nn.Conv2d:
        return self.backbone.conv1

    @property
    def maxpool(self) -> nn.Module:
        return self.backbone.maxpool

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Encode CIFAR-10 images into feature vectors of shape ``[B, 512]``."""

        return self.backbone(x)
