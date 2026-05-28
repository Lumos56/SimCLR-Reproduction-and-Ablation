"""Projection head used by SimCLR."""

from __future__ import annotations

import torch
from torch import nn


class ProjectionHead(nn.Module):
    """Two-layer MLP projection head.

    Expected input shape: ``[batch_size, input_dim]``.
    Output shape: ``[batch_size, output_dim]``.
    """

    def __init__(
        self,
        input_dim: int = 512,
        hidden_dim: int = 512,
        output_dim: int = 128,
    ) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, h: torch.Tensor) -> torch.Tensor:
        """Project encoder features from ``[B, 512]`` to ``[B, 128]``."""

        return self.net(h)
