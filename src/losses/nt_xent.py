"""NT-Xent contrastive loss for SimCLR."""

from __future__ import annotations

import torch
from torch import nn
from torch.nn import functional as F


def build_positive_pair_targets(batch_size: int, device: torch.device | None = None) -> torch.Tensor:
    """Build positive-pair targets for a concatenated ``[z1, z2]`` batch.

    For original batch size ``B``, embeddings are arranged as ``[2B, D]``:
    indices ``0..B-1`` are view 1 and indices ``B..2B-1`` are view 2.
    The positive for ``i`` in view 1 is ``i+B``; the positive for ``i`` in
    view 2 is ``i-B``.
    """

    if batch_size < 2:
        raise ValueError(f"batch_size must be >= 2, got {batch_size}")

    indices = torch.arange(2 * batch_size, device=device)
    return (indices + batch_size) % (2 * batch_size)


class NTXentLoss(nn.Module):
    """Normalized temperature-scaled cross entropy loss.

    Args:
        temperature: Positive scalar used to scale cosine similarities.

    Forward inputs:
        z1: Tensor with shape ``[batch_size, projection_dim]``.
        z2: Tensor with shape ``[batch_size, projection_dim]``.

    Returns:
        Scalar loss tensor.
    """

    def __init__(self, temperature: float = 0.5) -> None:
        super().__init__()
        if temperature <= 0:
            raise ValueError(f"temperature must be > 0, got {temperature}")
        self.temperature = temperature

    def forward(self, z1: torch.Tensor, z2: torch.Tensor) -> torch.Tensor:
        """Compute NT-Xent over two augmented views.

        The two input batches are concatenated into ``z`` with shape
        ``[2B, D]``. Cross entropy is computed over the ``[2B, 2B]`` cosine
        similarity matrix after masking self-similarity on the diagonal.
        Positive labels follow the paired-index rule from
        ``build_positive_pair_targets``.
        """

        self._validate_inputs(z1, z2)

        batch_size = z1.shape[0]
        z = torch.cat([z1, z2], dim=0)
        z = F.normalize(z, dim=1)

        logits = torch.matmul(z, z.T) / self.temperature
        logits = logits.masked_fill(
            torch.eye(2 * batch_size, dtype=torch.bool, device=z.device),
            float("-inf"),
        )

        targets = build_positive_pair_targets(batch_size, device=z.device)
        return F.cross_entropy(logits, targets)

    @staticmethod
    def _validate_inputs(z1: torch.Tensor, z2: torch.Tensor) -> None:
        if z1.ndim != 2 or z2.ndim != 2:
            raise ValueError(
                "z1 and z2 must be 2D tensors with shape [batch_size, projection_dim]"
            )
        if z1.shape != z2.shape:
            raise ValueError(f"z1 and z2 must have the same shape, got {z1.shape} and {z2.shape}")
        if z1.shape[0] < 2:
            raise ValueError(f"batch_size must be >= 2, got {z1.shape[0]}")
