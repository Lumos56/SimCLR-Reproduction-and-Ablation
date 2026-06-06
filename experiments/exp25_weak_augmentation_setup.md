# Experiment 25: Weak Augmentation Ablation Setup

## Purpose

Prepare configuration files for the weak-augmentation ablation after the no-projection ablation cycle.

This is a setup-only task. It does not run training, evaluation, tests, result-table generation, figure generation, or checkpoint creation.

## Ablation Question

The previous ablation removed the projection head. The next required ablation compares strong vs weak augmentation while keeping the projection head enabled.

The current short baseline reference is:

```text
Baseline SimCLR short + linear probe CIFAR-10 test Top-1: 0.621400
```

The weak-augmentation result is not available yet.

## Files Prepared

| Stage | Config | Purpose |
|---|---|---|
| Task 47 | `configs/cifar10_simclr_weak_aug_short.yaml` | Weak-augmentation SimCLR short pretraining. |
| Task 48 | `configs/cifar10_linear_probe_weak_aug_short.yaml` | Linear probe training on the weak-augmentation SimCLR checkpoint. |
| Task 49 | `configs/evaluate_linear_probe_weak_aug_short.yaml` | CIFAR-10 test-set evaluation for the weak-augmentation linear probe. |

## Fixed Conditions

- Dataset: CIFAR-10.
- Dataset root: `/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation`.
- Dataset download: `false`.
- Device: `auto`.
- SimCLR pretraining epochs: 10.
- Linear probe epochs: 5.
- Batch size: 128.
- Projection head: enabled.
- Temperature: 0.5 for SimCLR pretraining.
- Checkpoints: external model directory under `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation`.
- Logs and evaluation CSV paths: lightweight repository paths under `results/`.

## Changed Variable

- SimCLR pretraining augmentation strength changes from `strong` to `weak`.

## Planned External Artifacts

These files should be created only by later owner-approved runs:

- SimCLR checkpoint: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_weak_aug_short/cifar10_simclr_weak_aug_short.pt`
- Linear probe checkpoint: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_weak_aug_short/cifar10_linear_probe_weak_aug_short.pt`

## Planned Repository Outputs

These files should be produced only by later owner-approved tasks:

- Task 47 log: `results/logs/cifar10_simclr_weak_aug_short.csv`
- Task 48 log: `results/logs/cifar10_linear_probe_weak_aug_short.csv`
- Task 49 evaluation table: `results/tables/linear_probe_weak_aug_short_eval.csv`

## Interpretation Boundary

- No weak-augmentation metric exists yet.
- Task 47 should record weak-augmentation SimCLR short pretraining only.
- Task 48 should record weak-augmentation linear probe training only.
- Task 49 should record the CIFAR-10 test-set metric.
- Task 50 should update the augmentation ablation table and provide the first conservative interpretation.
- This ablation remains a short, single-run comparison and should not be reported as final SimCLR performance.

## Not Done

- No training was run.
- No evaluation was run.
- No tests were run.
- No checkpoints were created.
- No result table was created.
- No figures were created.
- No source code was modified.
