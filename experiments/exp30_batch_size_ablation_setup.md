# Experiment 30: Batch Size Ablation Setup

## Purpose

Prepare configuration files for the batch size ablation after the no-projection and augmentation-strength ablation cycles.

This is a setup-only task. It does not run training, evaluation, tests, result-table generation, figure generation, checkpoint creation, data download, or source-code changes.

## Ablation Question

The next required ablation compares SimCLR pretraining batch size 64 against the existing SimCLR short baseline batch size 128.

This is the third core ablation after:

- no projection head;
- strong vs weak augmentation.

## Baseline Reference

The current short baseline reference is:

```text
Baseline SimCLR short + linear probe CIFAR-10 test Top-1: 0.621400
```

Baseline setup:

- SimCLR pretrain batch size: 128.
- SimCLR pretrain epochs: 10.
- Linear probe batch size: 128.
- Linear probe epochs: 5.
- Projection head: enabled.
- Augmentation strength: strong.
- Result CSV: `results/tables/linear_probe_short_eval.csv`.

## Planned Batch64 Ablation

The new ablation will use:

- SimCLR pretrain batch size: 64.
- SimCLR pretrain epochs: 10.
- Linear probe batch size: 128.
- Linear probe epochs: 5.
- Projection head: enabled.
- Augmentation strength: strong for SimCLR pretraining.

The linear probe batch size remains 128 to reduce confounding. `batch64` refers to the SimCLR pretraining checkpoint, not to the linear probe batch size.

This comparison is fixed-epoch, not fixed-optimizer-step. Because `batch_size=64` creates more optimizer steps per epoch than `batch_size=128`, interpretation must remain preliminary.

The batch64 result is not available yet.

## Files Prepared

| Stage | Config | Purpose |
|---|---|---|
| Task 52 | `configs/cifar10_simclr_batch64_short.yaml` | SimCLR short pretraining with batch size 64. |
| Task 53 | `configs/cifar10_linear_probe_batch64_short.yaml` | Linear probe training on the batch64 SimCLR checkpoint. |
| Task 54 | `configs/evaluate_linear_probe_batch64_short.yaml` | CIFAR-10 test-set evaluation for the batch64 linear probe. |

## Fixed Conditions

- Dataset: CIFAR-10.
- Dataset root: `/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation`.
- Dataset download: `false`.
- Device: `auto`.
- SimCLR pretraining epochs: 10.
- Linear probe epochs: 5.
- Projection head: enabled.
- Temperature: 0.5 for SimCLR pretraining.
- Checkpoints: external model directory under `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation`.
- Logs and evaluation CSV paths: lightweight repository paths under `results/`.

## Changed Variable

- SimCLR pretraining batch size changes from `128` to `64`.

## Controlled Variable

- Linear probe batch size remains `128`.

## Planned External Artifacts

These files should be created only by later owner-approved runs:

- SimCLR checkpoint: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_batch64_short/cifar10_simclr_batch64_short.pt`
- Linear probe checkpoint: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_batch64_short/cifar10_linear_probe_batch64_short.pt`

## Planned Repository Outputs

These files should be produced only by later owner-approved tasks:

- Task 52 log: `results/logs/cifar10_simclr_batch64_short.csv`
- Task 53 log: `results/logs/cifar10_linear_probe_batch64_short.csv`
- Task 54 evaluation table: `results/tables/linear_probe_batch64_short_eval.csv`

## Interpretation Boundary

- No batch64 metric exists yet.
- Task 52 should record batch64 SimCLR short pretraining only.
- Task 53 should record batch64 linear probe short training only.
- Task 54 should record the CIFAR-10 test-set metric.
- Task 55 should update the batch-size ablation result table and provide the first conservative interpretation.
- This ablation remains a short, single-run, fixed-epoch comparison and should not be reported as final SimCLR performance.

## Not Done

- No training was run.
- No evaluation was run.
- No tests were run.
- No checkpoints were created.
- No result table was created.
- No figures were created.
- No data was downloaded.
- No source code was modified.

## Next Step

Task 52 should run and record the batch64 SimCLR short pretraining result after Human Owner approval.
