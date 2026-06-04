"""SimCLR model wrapper."""

from __future__ import annotations

import torch
from torch import nn

from src.models.encoder import CifarResNet18Encoder
from src.models.projection_head import ProjectionHead


class SimCLR(nn.Module):
    """Encoder plus optional projection head for SimCLR.

    Forward input shape: ``[batch_size, 3, 32, 32]``.
    Returns:
        ``h`` with shape ``[batch_size, 512]`` and
        ``z`` with shape ``[batch_size, 128]`` by default.

    ``use_projection_head=True`` is the default SimCLR path. Setting
    ``use_projection_head=False`` disables the projection head for the
    no-projection ablation and applies NT-Xent directly to encoder features.
    """

    def __init__(
        self,
        encoder: nn.Module | None = None,
        projection_head: nn.Module | None = None,
        feature_dim: int = 512,
        projection_hidden_dim: int = 512,
        projection_dim: int = 128,
        use_projection_head: bool = True,
    ) -> None:
        super().__init__()
        if projection_head is not None and not use_projection_head:
            raise ValueError("projection_head cannot be provided when use_projection_head=False")

        self.use_projection_head = use_projection_head
        self.encoder = encoder or CifarResNet18Encoder(feature_dim=feature_dim)
        if use_projection_head:
            self.projection_head = projection_head or ProjectionHead(
                input_dim=feature_dim,
                hidden_dim=projection_hidden_dim,
                output_dim=projection_dim,
            )
        else:
            # No-projection ablation: keep the module attribute stable while
            # passing encoder features directly to the contrastive loss.
            self.projection_head = nn.Identity()

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Return encoder representation ``h`` and contrastive representation ``z``.

        With the default projection head, ``z`` is the projected ``[B, 128]``
        representation. For the no-projection ablation, ``z`` is the encoder
        representation itself with shape ``[B, 512]``.
        """

        h = self.encoder(x)
        z = self.projection_head(h)
        return h, z
