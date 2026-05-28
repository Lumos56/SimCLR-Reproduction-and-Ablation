import pytest
import torch
from torch import nn

from src.models import CifarResNet18Encoder, ProjectionHead, SimCLR


def test_cifar_resnet18_encoder_forward_shape() -> None:
    encoder = CifarResNet18Encoder()
    encoder.eval()
    x = torch.randn(4, 3, 32, 32)

    with torch.no_grad():
        h = encoder(x)

    assert tuple(h.shape) == (4, 512)


def test_cifar_resnet18_encoder_rejects_non_default_feature_dim() -> None:
    with pytest.raises(ValueError, match="only supports feature_dim=512"):
        CifarResNet18Encoder(feature_dim=256)


def test_projection_head_shape() -> None:
    projection_head = ProjectionHead()
    x = torch.randn(4, 512)

    with torch.no_grad():
        z = projection_head(x)

    assert tuple(z.shape) == (4, 128)


def test_simclr_forward_shapes() -> None:
    model = SimCLR()
    model.eval()
    x = torch.randn(4, 3, 32, 32)

    with torch.no_grad():
        h, z = model(x)

    assert tuple(h.shape) == (4, 512)
    assert tuple(z.shape) == (4, 128)


def test_cifar_resnet18_first_conv_is_cifar_sized() -> None:
    encoder = CifarResNet18Encoder()

    assert encoder.conv1.kernel_size == (3, 3)
    assert encoder.conv1.stride == (1, 1)


def test_cifar_resnet18_maxpool_is_identity() -> None:
    encoder = CifarResNet18Encoder()

    assert isinstance(encoder.maxpool, nn.Identity)
