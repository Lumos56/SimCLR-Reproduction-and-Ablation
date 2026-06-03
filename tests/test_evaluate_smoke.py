import csv
import math
from pathlib import Path

import torch
import yaml

from src.evaluate import run_evaluation
from src.models import CifarResNet18Encoder, SimCLR
from src.train_linear_probe import LinearProbe
from src.train_supervised import SupervisedResNet18


def read_single_csv_row(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
    return rows[0]


def assert_accuracy_result_is_valid(result: dict, output_path: Path, tmp_path: Path) -> dict[str, str]:
    repo_root = Path(__file__).resolve().parents[1]
    assert 0.0 <= result["top1_accuracy"] <= 1.0
    assert math.isfinite(result["top1_accuracy"])
    assert result["total"] > 0
    assert 0 <= result["correct"] <= result["total"]
    assert output_path.is_file()
    assert output_path.resolve().is_relative_to(tmp_path.resolve())
    assert not output_path.resolve().is_relative_to(repo_root)

    row = read_single_csv_row(output_path)
    assert math.isfinite(float(row["top1_accuracy"]))
    assert 0.0 <= float(row["top1_accuracy"]) <= 1.0
    assert int(row["total"]) == result["total"]
    assert row["dataset_split"] == result["dataset_split"]
    assert row["checkpoint_path"] == result["checkpoint_path"]
    assert row["simclr_checkpoint_path"] == result["simclr_checkpoint_path"]
    return row


def test_fake_supervised_evaluation_smoke(tmp_path: Path) -> None:
    checkpoint_path = tmp_path / "checkpoints" / "supervised.pt"
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "epoch": 1,
            "step": 1,
            "model_state_dict": SupervisedResNet18().state_dict(),
            "optimizer_state_dict": {},
        },
        checkpoint_path,
    )
    output_path = tmp_path / "outputs" / "supervised_eval.csv"

    config = {
        "seed": 0,
        "mode": "supervised",
        "device": "cpu",
        "checkpoint": {
            "path": str(checkpoint_path),
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
        "batch_size": 4,
        "num_workers": 0,
        "output_path": str(output_path),
    }
    config_path = tmp_path / "configs" / "supervised_eval.yaml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(yaml.safe_dump(config), encoding="utf-8")

    result = run_evaluation(config_path)

    assert result["mode"] == "supervised"
    assert result["dataset"] == "fake"
    assert result["dataset_split"] == "fake"
    assert result["simclr_checkpoint_path"] == ""
    row = assert_accuracy_result_is_valid(result, output_path, tmp_path)
    assert row["simclr_checkpoint_path"] == ""


def test_fake_linear_probe_evaluation_smoke(tmp_path: Path) -> None:
    checkpoint_dir = tmp_path / "checkpoints"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    simclr_checkpoint_path = checkpoint_dir / "simclr.pt"
    linear_probe_checkpoint_path = checkpoint_dir / "linear_probe.pt"

    torch.save(
        {
            "epoch": 1,
            "step": 1,
            "model_state_dict": SimCLR().state_dict(),
            "optimizer_state_dict": {},
        },
        simclr_checkpoint_path,
    )
    linear_probe = LinearProbe(encoder=CifarResNet18Encoder())
    torch.save(
        {
            "epoch": 1,
            "step": 1,
            "classifier_state_dict": linear_probe.classifier.state_dict(),
            "optimizer_state_dict": {},
        },
        linear_probe_checkpoint_path,
    )
    output_path = tmp_path / "outputs" / "linear_probe_eval.csv"

    result = run_evaluation(
        {
            "seed": 0,
            "mode": "linear_probe",
            "device": "cpu",
            "checkpoint": {
                "path": str(linear_probe_checkpoint_path),
                "simclr_path": str(simclr_checkpoint_path),
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
            "batch_size": 4,
            "num_workers": 0,
            "output_path": str(output_path),
        }
    )

    assert result["mode"] == "linear_probe"
    assert result["dataset"] == "fake"
    assert result["dataset_split"] == "fake"
    assert result["simclr_checkpoint_path"] == str(simclr_checkpoint_path)
    row = assert_accuracy_result_is_valid(result, output_path, tmp_path)
    assert row["simclr_checkpoint_path"] == str(simclr_checkpoint_path)
