import csv
import math
from pathlib import Path

from src.train_simclr import run_smoke_training


def test_fake_simclr_smoke_training_creates_log_and_checkpoint(tmp_path: Path) -> None:
    config = {
        "seed": 0,
        "device": "cpu",
        "dataset": {
            "name": "fake",
            "size": 8,
            "image_size": [3, 32, 32],
            "num_classes": 10,
            "augmentation_strength": "weak",
        },
        "training": {
            "epochs": 1,
            "batch_size": 4,
            "max_train_batches": 1,
            "num_workers": 0,
            "shuffle": False,
            "temperature": 0.5,
        },
        "optimizer": {
            "name": "adam",
            "lr": 0.001,
            "weight_decay": 0.0,
        },
        "paths": {
            "log_dir": str(tmp_path / "logs"),
            "log_filename": "simclr_smoke.csv",
            "checkpoint_dir": str(tmp_path / "checkpoints"),
            "checkpoint_filename": "simclr_smoke.pt",
        },
    }

    result = run_smoke_training(config)

    log_path = Path(result["log_path"]).resolve()
    checkpoint_path = Path(result["checkpoint_path"]).resolve()
    repo_root = Path(__file__).resolve().parents[1]

    assert result["steps"] == 1
    assert log_path.is_file()
    assert checkpoint_path.is_file()
    assert log_path.is_relative_to(tmp_path.resolve())
    assert checkpoint_path.is_relative_to(tmp_path.resolve())
    assert not checkpoint_path.is_relative_to(repo_root)

    with log_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 1
    assert rows[0]["epoch"] == "1"
    assert rows[0]["step"] == "1"
    assert math.isfinite(float(rows[0]["loss"]))
