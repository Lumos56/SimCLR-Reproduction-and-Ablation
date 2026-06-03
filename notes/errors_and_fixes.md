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

### 2026-06-03 - Full CSV Log Printed During Short Baseline Review

#### Context

The Human Owner ran the supervised short baseline and inspected `results/logs/cifar10_supervised_short.csv`.

#### Error Message

```text
The full 3901-line CSV log was printed to the terminal because cat was used.
```

#### Investigation

The command template was appropriate for very small smoke logs, where printing the whole CSV is acceptable. It was reused for a short-baseline training log with 3901 lines, which made the terminal output noisy and harder to review.

This was not a code failure and did not affect the supervised short baseline run.

#### Fix

For short-baseline, baseline, or long-run CSV logs, inspect summaries instead of printing the whole file:

```bash
wc -l results/logs/cifar10_supervised_short.csv
head -n 5 results/logs/cifar10_supervised_short.csv
tail -n 10 results/logs/cifar10_supervised_short.csv
```

Use scripts or plotting tools for deeper analysis.

#### Lesson

Never `cat` full training CSV logs for short-baseline, baseline, or long-run records. Reserve full-file `cat` only for smoke logs with a few lines.
