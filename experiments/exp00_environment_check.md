# Exp00: Environment Check

## Date

2026-05-26

## Status

PASS

The storage and environment checks were run by the Human Owner. Codex only recorded the verified results in this file.

## Repository

- Repo path: `/home/yeyee/projects/SimCLR-Reproduction-and-Ablation`
- Branch for this record: `env/gate0-check`

## Storage Path Check

Storage check result: PASS

Verified storage facts:

- `~/research` resolves to `/mnt/f/Research`
- `/mnt/f` is the F drive
- F drive available space: about 1.9T

External storage policy:

```text
Raw datasets:
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation

Models and checkpoints:
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation

Large exports:
/home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation
```

Repository policy:

- No datasets are stored in the repository.
- No checkpoints or model weights are stored in the repository.
- Small Markdown notes and selected small CSV logs may stay in the repository.

## Machine and Driver

- GPU: NVIDIA GeForce RTX 5080
- NVIDIA-SMI: 595.58.04
- NVIDIA Driver Version: 596.21
- nvidia-smi CUDA Version: 13.2
- `nvidia-smi` works: yes

## Conda and Python

- Conda environment: `simclr`
- Python: 3.10.20
- Python path: `/home/yeyee/miniconda3/envs/simclr/bin/python`

## PyTorch Stack

- torch: 2.11.0+cu128
- torch.version.cuda: 12.8
- torch.cuda.is_available(): True
- torchvision: 0.26.0+cu128
- pytest: 9.0.3
- PyYAML import: ok

## Verification Commands Used by Human Owner

Storage:

```bash
pwd
df -h .
ls -ld ~/research || true
readlink -f ~/research || true
df -h ~/research || true
```

Environment:

```bash
conda activate simclr
python --version
which python
nvidia-smi
python - <<'PY'
import sys
print("python:", sys.version)

import torch
print("torch:", torch.__version__)
print("torch.version.cuda:", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("device:", torch.cuda.get_device_name(0))

import torchvision
print("torchvision:", torchvision.__version__)

import pytest
print("pytest:", pytest.__version__)

import yaml
print("pyyaml import: ok")
PY
```

## Result

- Status: PASS
- Blocking issue: none for Gate 0
- Next action: commit the Gate 0 record, then proceed to Gate 1 module setup after review
