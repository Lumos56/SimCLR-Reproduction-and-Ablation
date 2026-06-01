import csv
import math
from pathlib import Path

from src.train_supervised import run_supervised_training


def test_fake_supervised_smoke_training_creates_log_and_tmp_checkpoint(tmp_path: Path) -> None:
    config = {
        "seed": 0,
        "device": "cpu",
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
            "log_filename": "supervised_smoke.csv",
            "save_checkpoint": True,
            "checkpoint_dir": str(tmp_path / "checkpoints"),
            "checkpoint_filename": "supervised_smoke.pt",
        },
    }

    result = run_supervised_training(config)
    log_path = Path(result["log_path"]).resolve()
    checkpoint_path = Path(result["checkpoint_path"]).resolve()
    repo_root = Path(__file__).resolve().parents[1]

    assert result["steps"] == 1
    assert log_path.is_file()
    assert checkpoint_path.is_file()
    assert log_path.is_relative_to(tmp_path.resolve())
    assert checkpoint_path.is_relative_to(tmp_path.resolve())
    assert not checkpoint_path.is_relative_to(repo_root)
    assert not (repo_root / "supervised_smoke.pt").exists()

    with log_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 1
    assert rows[0]["epoch"] == "1"
    assert rows[0]["step"] == "1"
    assert "train_acc" in rows[0]
    assert math.isfinite(float(rows[0]["train_loss"]))
    assert math.isfinite(float(rows[0]["train_acc"]))
