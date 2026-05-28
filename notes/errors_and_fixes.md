# Errors and Fixes

This file records real errors, debugging steps, fixes, and reusable lessons.

## Template

### YYYY-MM-DD - Error Title

#### Context

#### Error Message

```text
```

#### Investigation

#### Fix

#### Lesson

### 2026-05-28 - Direct Script Import Error for SimCLR CLI

#### Context

The Human Owner ran the fake-data SimCLR smoke CLI after Task 12.

#### Error Message

```text
ModuleNotFoundError: No module named 'src'
```

#### Investigation

The failing command was:

```bash
python src/train_simclr.py --config configs/simclr_fake_smoke.yaml
```

Direct script execution from the `src` path does not put the repository root on Python's package path, so imports such as `from src...` cannot be resolved.

#### Fix

Run the CLI as a module from the repository root:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.train_simclr --config configs/simclr_fake_smoke.yaml
```

#### Lesson

Use module-style execution for `src` package CLI commands so imports resolve from the repository root.
