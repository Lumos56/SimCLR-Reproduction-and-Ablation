"""SimCLR model wrapper."""

from __future__ import annotations

import torch
from torch import nn

from src.models.encoder import CifarResNet18Encoder
from src.models.projection_head import ProjectionHead


class SimCLR(nn.Module):
    """Encoder plus projection head for SimCLR.

    Forward input shape: ``[batch_size, 3, 32, 32]``.
    Returns:
        ``h`` with shape ``[batch_size, 512]`` and
        ``z`` with shape ``[batch_size, 128]`` by default.
    """

    def __init__(
        self,
        encoder: nn.Module | None = None,
        projection_head: nn.Module | None = None,
        feature_dim: int = 512,
        projection_hidden_dim: int = 512,
        projection_dim: int = 128,
    ) -> None:
        super().__init__()
        self.encoder = encoder or CifarResNet18Encoder(feature_dim=feature_dim)
        self.projection_head = projection_head or ProjectionHead(
            input_dim=feature_dim,
            hidden_dim=projection_hidden_dim,
            output_dim=projection_dim,
        )

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Return encoder representation ``h`` and projected representation ``z``."""

        h = self.encoder(x)
        z = self.projection_head(h)
        return h, z
