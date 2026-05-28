import pytest
import torch

from src.losses import NTXentLoss, build_positive_pair_targets


def test_nt_xent_returns_scalar_tensor() -> None:
    loss_fn = NTXentLoss()
    z1 = torch.randn(4, 128)
    z2 = torch.randn(4, 128)

    loss = loss_fn(z1, z2)

    assert isinstance(loss, torch.Tensor)
    assert loss.ndim == 0


def test_nt_xent_is_finite_on_random_inputs() -> None:
    loss_fn = NTXentLoss()
    z1 = torch.randn(4, 128)
    z2 = torch.randn(4, 128)

    loss = loss_fn(z1, z2)

    assert torch.isfinite(loss)


def test_nt_xent_backward_produces_gradients() -> None:
    loss_fn = NTXentLoss()
    z1 = torch.randn(4, 128, requires_grad=True)
    z2 = torch.randn(4, 128, requires_grad=True)

    loss = loss_fn(z1, z2)
    loss.backward()

    assert z1.grad is not None
    assert z2.grad is not None
    assert torch.isfinite(z1.grad).all()
    assert torch.isfinite(z2.grad).all()


def test_invalid_temperature_raises_value_error() -> None:
    with pytest.raises(ValueError, match="temperature must be > 0"):
        NTXentLoss(temperature=0)

    with pytest.raises(ValueError, match="temperature must be > 0"):
        NTXentLoss(temperature=-0.1)


def test_mismatched_input_shapes_raise_value_error() -> None:
    loss_fn = NTXentLoss()
    z1 = torch.randn(4, 128)
    z2 = torch.randn(5, 128)

    with pytest.raises(ValueError, match="same shape"):
        loss_fn(z1, z2)


def test_non_2d_inputs_raise_value_error() -> None:
    loss_fn = NTXentLoss()
    z1 = torch.randn(4, 2, 64)
    z2 = torch.randn(4, 2, 64)

    with pytest.raises(ValueError, match="2D tensors"):
        loss_fn(z1, z2)


def test_batch_size_less_than_two_raises_value_error() -> None:
    loss_fn = NTXentLoss()
    z1 = torch.randn(1, 128)
    z2 = torch.randn(1, 128)

    with pytest.raises(ValueError, match="batch_size must be >= 2"):
        loss_fn(z1, z2)


def test_positive_pair_target_construction() -> None:
    targets = build_positive_pair_targets(batch_size=3)

    assert targets.tolist() == [3, 4, 5, 0, 1, 2]


def test_identical_positive_pairs_have_lower_loss_than_mismatched_pairs() -> None:
    loss_fn = NTXentLoss(temperature=0.5)
    z1 = torch.eye(4)
    z2 = z1.clone()
    mismatched_z2 = torch.roll(z2, shifts=1, dims=0)

    matched_loss = loss_fn(z1, z2)
    mismatched_loss = loss_fn(z1, mismatched_z2)

    assert matched_loss < mismatched_loss
