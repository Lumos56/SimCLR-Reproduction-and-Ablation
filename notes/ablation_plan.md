# Ablation Plan Decision

Date: 2026-06-04

## Purpose

This is a planning document, not an experiment result.

It defines the first ablation stage after the short-baseline training, evaluation, plotting, README v0.2, and GitHub first-push checkpoints. It must not be used as evidence of model performance, convergence, or final SimCLR quality.

No ablation code, ablation config, training run, evaluation run, checkpoint, figure, or metric is created by this plan.

## Current Short Baseline Reference

The current comparison baseline is the short-baseline stage only:

| Method | Evaluation split | Top-1 accuracy | Correct / total | Interpretation |
|---|---|---:|---:|---|
| Supervised short baseline | CIFAR-10 test | 0.873700 | 8737 / 10000 | Preliminary short-baseline result, not final supervised performance. |
| SimCLR short + linear probe | CIFAR-10 test | 0.621400 | 6214 / 10000 | Preliminary short-baseline result, not final SimCLR performance. |

Both values are short-baseline results. They are not final benchmark results, not paper-scale comparisons, and not final project performance.

## First Ablation Stage

The first ablation stage should stay at the same short-baseline scale so that each result is comparable to the existing short SimCLR reference before any long run or broad sweep is attempted.

Planned ablations:

| Ablation | Question | Expected setup status |
|---|---|---|
| No projection head | Does removing the projection head change downstream linear-probe performance in this small CIFAR-10 setting? | Implement first. Requires explicit model/config support. |
| Strong vs weak augmentation | How sensitive is the short SimCLR pipeline to augmentation strength? | Plan after no-projection path is working. |
| Batch size 64 vs 128 | How does smaller batch size affect short SimCLR training and downstream linear-probe performance? | Plan after the first ablation path is validated. |

## Recommended First Ablation

Start with:

```text
no projection head
```

Reasons:

- It directly tests a core SimCLR design choice.
- It requires explicit model/config support, so implementing it early validates that the project can express structural ablations cleanly.
- It helps test whether the projection head matters in this small CIFAR-10 setting under the same short-baseline scale.
- It should create a clear first contrast against the current short SimCLR plus linear-probe reference.

## Safe Run Strategy

Use the existing short-baseline scale first:

| Stage | Plan |
|---|---|
| Dataset | CIFAR-10 |
| SimCLR pretrain | 10 epochs |
| Linear probe | 5 epochs |
| Preferred batch size | 128 |
| Fallback batch size | 64 if CUDA memory issues occur |
| Device | `auto` or `cuda` according to approved config behavior |

Do not start long runs yet. Do not broaden into hyperparameter search. Do not update README performance claims until ablation results are reviewed.

## Output Rules

- Raw datasets must remain under `/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation`.
- Checkpoints and model weights must be written outside the repository under `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation`.
- Large exports must remain outside the repository under `/home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation`.
- Small CSV logs may be committed when they are useful evidence.
- Result tables may be committed.
- Experiment notes may be committed.
- Model weights must not be committed.
- `.pt`, `.pth`, `.ckpt`, `.onnx`, TensorBoard event files, W&B runs, datasets, and large generated artifacts must not be committed.

## Interpretation Rules

- Ablation results are preliminary until reviewed.
- Do not claim final SimCLR performance from short ablations.
- Compare short ablation results only against the existing short SimCLR baseline unless a later longer baseline exists.
- Do not compare with paper-scale SimCLR results.
- Report every ablation with its config, command, seed, dataset path, checkpoint path, result file, and limitations.
- Failed, partial, or fallback runs should be recorded rather than hidden.

## Proposed Next Tasks

| Task | Scope |
|---|---|
| Task 40 | No projection ablation setup. |
| Task 41 | Run no projection short pretrain. |
| Task 42 | Run no projection linear probe. |
| Task 43 | Evaluate no projection linear probe. |
| Task 44 | Update ablation result table. |

Task 40 should prepare the implementation/config support needed for no-projection ablation, but it should not run training. Later run tasks should be owner-approved before execution.

## Failure Rules

- If CUDA out-of-memory occurs, stop, record the error, and reduce batch size from `128` to `64` only after recording the fallback.
- If loss becomes NaN or non-finite, stop and record the exact error, command, config, and stage.
- If any checkpoint path writes into the Git repository, stop and fix the config before continuing.
- If dataset files are missing, do not download automatically; ask the Human Owner.
- If the task scope expands into long runs, broad hyperparameter sweeps, README performance updates, or final-report work, stop and ask the Human Owner.
- If any unexpected large artifact appears in the repository, stop and fix storage before continuing.

## Decision

Begin ablation planning with the no-projection-head ablation at the current short-baseline scale. Treat the resulting ablation stage as preliminary controlled evidence, not final performance.
