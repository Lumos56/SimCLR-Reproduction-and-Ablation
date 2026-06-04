import torch

from src.losses import NTXentLoss
from src.models import SimCLR


def has_nonzero_gradient(parameters) -> bool:
    return any(
        parameter.grad is not None and torch.count_nonzero(parameter.grad.detach()).item() > 0
        for parameter in parameters
    )


def test_simclr_forward_backward_on_synthetic_views() -> None:
    torch.manual_seed(0)
    model = SimCLR()
    loss_fn = NTXentLoss(temperature=0.5)
    x1 = torch.randn(4, 3, 32, 32)
    x2 = torch.randn(4, 3, 32, 32)

    h1, z1 = model(x1)
    h2, z2 = model(x2)

    assert tuple(h1.shape) == (4, 512)
    assert tuple(z1.shape) == (4, 128)
    assert tuple(h2.shape) == (4, 512)
    assert tuple(z2.shape) == (4, 128)

    loss = loss_fn(z1, z2)

    assert loss.ndim == 0
    assert torch.isfinite(loss)

    loss.backward()

    assert has_nonzero_gradient(model.encoder.parameters())
    assert has_nonzero_gradient(model.projection_head.parameters())


def test_no_projection_simclr_forward_backward_on_synthetic_views() -> None:
    torch.manual_seed(0)
    model = SimCLR(use_projection_head=False)
    loss_fn = NTXentLoss(temperature=0.5)
    x1 = torch.randn(4, 3, 32, 32)
    x2 = torch.randn(4, 3, 32, 32)

    h1, z1 = model(x1)
    h2, z2 = model(x2)

    assert tuple(h1.shape) == (4, 512)
    assert tuple(z1.shape) == (4, 512)
    assert tuple(h2.shape) == (4, 512)
    assert tuple(z2.shape) == (4, 512)

    loss = loss_fn(z1, z2)

    assert loss.ndim == 0
    assert torch.isfinite(loss)

    loss.backward()

    assert has_nonzero_gradient(model.encoder.parameters())
