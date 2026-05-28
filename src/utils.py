"""Small utilities shared by smoke-training scripts."""

from __future__ import annotations

import csv
import random
from pathlib import Path
from typing import Any

import torch
import yaml


def load_yaml_config(path: str | Path) -> dict[str, Any]:
    """Load a YAML config file as a dictionary."""

    config_path = Path(path).expanduser()
    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}
    if not isinstance(config, dict):
        raise ValueError(f"config must be a YAML mapping, got {type(config).__name__}")
    return config


def set_seed(seed: int | None) -> None:
    """Set Python, NumPy if available, and PyTorch RNG seeds."""

    if seed is None:
        return

    random.seed(seed)
    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def get_device(device_name: str | None) -> torch.device:
    """Resolve a configured device name into a torch device."""

    if device_name is None or device_name == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

    device = torch.device(device_name)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise ValueError("CUDA device was requested, but torch.cuda.is_available() is False")
    return device


def ensure_dir(path: str | Path) -> Path:
    """Create a directory if needed and return it as a Path."""

    directory = Path(path).expanduser()
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def append_csv_row(path: str | Path, row: dict[str, Any]) -> Path:
    """Append one row to a CSV file, writing the header when the file is new."""

    csv_path = Path(path).expanduser()
    ensure_dir(csv_path.parent)
    file_exists = csv_path.exists() and csv_path.stat().st_size > 0
    fieldnames = list(row.keys())
    with csv_path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
    return csv_path
