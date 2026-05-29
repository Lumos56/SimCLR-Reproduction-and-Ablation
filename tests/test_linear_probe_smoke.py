import csv
import math
from pathlib import Path

import torch

from src.models import SimCLR
from src.train_linear_probe import run_linear_probe_training


def any_classifier_parameter_changed(
    initial_state: dict[str, torch.Tensor],
    current_state: dict[str, torch.Tensor],
) -> bool:
    return any(
        not torch.allclose(initial_state[name], current_state[name].detach().cpu())
        for name in initial_state
    )


def any_classifier_gradient_is_nonzero(model) -> bool:
    return any(
        parameter.grad is not None and torch.count_nonzero(parameter.grad.detach()).item() > 0
        for parameter in model.classifier.parameters()
    )


def test_fake_linear_probe_smoke_training(tmp_path: Path) -> None:
    simclr_checkpoint = tmp_path / "checkpoints" / "simclr_smoke.pt"
    simclr_checkpoint.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {"model_state_dict": SimCLR().state_dict()},
        simclr_checkpoint,
    )

    config = {
        "seed": 0,
        "device": "cpu",
        "checkpoint": {
            "simclr_path": str(simclr_checkpoint),
        },
        "model": {
            "feature_dim": 512,
            "num_classes": 10,
        },
        "dataset": {
            "name": "fake",
            "size": 8,
            "image_size": [3, 32, 32],
            "num_classes": 10,
        },
        "training": {
            "epochs": 1,
            "batch_size": 4,
            "max_train_batches": 1,
            "num_workers": 0,
            "shuffle": False,
        },
        "optimizer": {
            "name": "adam",
            "lr": 0.001,
            "weight_decay": 0.0,
        },
        "paths": {
            "log_dir": str(tmp_path / "logs"),
            "log_filename": "linear_probe_smoke.csv",
            "save_checkpoint": True,
            "checkpoint_dir": str(tmp_path / "linear_probe"),
            "checkpoint_filename": "linear_probe_smoke.pt",
        },
    }

    result = run_linear_probe_training(config)
    model = result["model"]
    log_path = Path(result["log_path"]).resolve()
    checkpoint_path = Path(result["checkpoint_path"]).resolve()
    repo_root = Path(__file__).resolve().parents[1]

    assert result["steps"] == 1
    assert log_path.is_file()
    assert checkpoint_path.is_file()
    assert log_path.is_relative_to(tmp_path.resolve())
    assert checkpoint_path.is_relative_to(tmp_path.resolve())
    assert not checkpoint_path.is_relative_to(repo_root)
    assert all(not parameter.requires_grad for parameter in model.encoder.parameters())
    assert all(parameter.grad is None for parameter in model.encoder.parameters())
    assert any_classifier_gradient_is_nonzero(model)
    assert any_classifier_parameter_changed(
        result["initial_classifier_state"],
        model.classifier.state_dict(),
    )

    with log_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 1
    assert rows[0]["epoch"] == "1"
    assert rows[0]["step"] == "1"
    assert math.isfinite(float(rows[0]["train_loss"]))
    assert math.isfinite(float(rows[0]["train_acc"]))
