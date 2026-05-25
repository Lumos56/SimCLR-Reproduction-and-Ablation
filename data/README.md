# Data Directory Policy

This directory is only for documenting data storage policy. Do not place CIFAR-10 files, raw datasets, archives, extracted images, or generated dataset caches inside this repository.

## External Storage Paths

Raw datasets:

```text
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation
```

Models and checkpoints:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation
```

Large exports:

```text
/home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation
```

Small Markdown experiment notes and selected small CSV logs may stay in this repository. Large logs, checkpoints, model weights, raw datasets, and generated artifacts must stay outside the repository.

## Required Check Before Data Download

Before downloading datasets or saving checkpoints, the Human Owner must verify that `/home/yeyee/research` points to the intended research storage area.

Suggested check:

```bash
pwd
df -h .
ls -ld ~/research || true
readlink -f ~/research || true
df -h ~/research || true
```

## Current Status

- Dataset downloaded: no
- Dataset path verified: no
- Checkpoint path verified: no
- Environment verified: no
