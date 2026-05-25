# Exp00: Environment Check

## Date

2026-05-22

## Machine

- OS:
- WSL distro:
- GPU:
- NVIDIA driver:
- nvidia-smi CUDA Version:

## Conda

```bash
conda info --envs
conda activate simclr
python --version
which python
```

## Storage Path Check

Before downloading datasets or saving checkpoints, verify that `/home/yeyee/research` points to the intended external research storage area.

```bash
pwd
df -h .
ls -ld ~/research || true
readlink -f ~/research || true
df -h ~/research || true
```

Expected external paths:

```text
Raw datasets:
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation

Models and checkpoints:
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation

Large exports:
/home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation
```

Storage verification result:

- `/home/yeyee/research` exists: yes/no
- `/home/yeyee/research` resolved path:
- Filesystem / mount:
- Data root approved by Human Owner: yes/no
- Checkpoint directory approved by Human Owner: yes/no

## PyTorch Install Source

- Official PyTorch selector checked: yes/no
- Selected build:
- Install command used:

## Verification Commands

```bash
python - <<'PY'
import sys
print("python:", sys.version)

try:
    import torch
    print("torch:", torch.__version__)
    print("torch.version.cuda:", torch.version.cuda)
    print("cuda available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("device:", torch.cuda.get_device_name(0))
except Exception as e:
    print("torch import failed:", repr(e))

try:
    import torchvision
    print("torchvision:", torchvision.__version__)
except Exception as e:
    print("torchvision import failed:", repr(e))

try:
    import pytest
    print("pytest:", pytest.__version__)
except Exception as e:
    print("pytest import failed:", repr(e))

try:
    import yaml
    print("pyyaml import: ok")
except Exception as e:
    print("pyyaml import failed:", repr(e))
PY
```

## Result

- Status: PASS / FAIL / PARTIAL
- Blocking issue:
- Next action:
