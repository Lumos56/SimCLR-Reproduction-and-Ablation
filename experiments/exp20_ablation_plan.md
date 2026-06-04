# Experiment 20: Ablation Plan

## Purpose

Record the decision to move from short-baseline reporting into ablation planning.

This is a planning and documentation record only. No ablation code, config, training run, evaluation run, checkpoint, figure, result table, or metric is created by this task.

## Why Ablation Begins Now

Ablation planning is appropriate now because the project has completed the minimum controlled reference needed before changing experimental variables:

- supervised short baseline training and CIFAR-10 test evaluation;
- SimCLR short pretraining;
- short linear probe training and CIFAR-10 test evaluation;
- short-baseline result table and first interpretation;
- short-baseline figures;
- README v0.2;
- first GitHub publication.

The next step should be a plan, not an ablation run, because the project still needs explicit scope, output paths, failure rules, and interpretation rules before modifying implementation or configs.

## Existing Evidence

The current short-baseline reference is:

| Method | Evaluation split | Top-1 accuracy | Correct / total | Evidence |
|---|---|---:|---:|---|
| Supervised short baseline | CIFAR-10 test | 0.873700 | 8737 / 10000 | `results/tables/supervised_short_eval.csv` |
| SimCLR short + linear probe | CIFAR-10 test | 0.621400 | 6214 / 10000 | `results/tables/linear_probe_short_eval.csv` |

Supporting records:

- `results/tables/short_baseline_results.md`
- `experiments/exp17_short_baseline_analysis.md`
- `experiments/exp18_short_baseline_curves.md`
- `notes/baseline_training_plan.md`
- `README.md`

These values are preliminary short-baseline results, not final benchmark results.

## Chosen First Ablation

The first ablation should be:

```text
no projection head
```

Rationale:

- It directly tests a core SimCLR design choice.
- It requires explicit model/config support before any run, making it a good first structural ablation.
- It can be compared against the current short SimCLR plus linear-probe reference under the same short-baseline scale.
- It helps determine whether the projection head matters in this small CIFAR-10 setting before moving to augmentation or batch-size ablations.

## Planned Scale

Use the same short-baseline scale first:

- SimCLR pretrain: 10 epochs.
- Linear probe: 5 epochs.
- Preferred batch size: 128.
- Fallback batch size: 64 only if CUDA memory issues occur and the fallback is recorded.

No long run should start during the setup or planning stage.

## Not Done Yet

The following are explicitly not part of this task:

- no long runs;
- no final report;
- no broad hyperparameter sweep;
- no README performance update until ablation results are reviewed;
- no ablation configs;
- no training;
- no evaluation;
- no model/checkpoint creation;
- no result-table update from fabricated or unrun metrics.

## Next Planned Tasks

| Task | Scope |
|---|---|
| Task 40 | No projection ablation setup. |
| Task 41 | Run no projection short pretrain. |
| Task 42 | Run no projection linear probe. |
| Task 43 | Evaluate no projection linear probe. |
| Task 44 | Update ablation result table. |

## Decision

Start the ablation stage with planning, then implement no-projection-head support as the first ablation setup task. Do not start ablation runs until the setup task is reviewed and approved.
