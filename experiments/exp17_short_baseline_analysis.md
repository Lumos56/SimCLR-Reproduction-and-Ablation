# Experiment 17: Short Baseline Result Analysis

## Purpose

Build the first comparable result table after Task 33 supervised short evaluation and Task 34 linear probe short evaluation.

This is an analysis and documentation task. No new training, evaluation, tests, downloads, checkpoints, figures, or ablations were run in Task 35. All values come from existing result files.

## Source Files

| Source | Role |
|---|---|
| `experiments/exp15_supervised_short_eval.md` | Supervised short evaluation record |
| `experiments/exp16_linear_probe_short_eval.md` | Linear probe short evaluation record |
| `results/tables/supervised_short_eval.csv` | Supervised short CIFAR-10 test-set metric |
| `results/tables/linear_probe_short_eval.csv` | Linear probe short CIFAR-10 test-set metric |
| `results/tables/short_baseline_training_summary.md` | Training-log context from Tasks 28-30 |

## What Was Evaluated

Two short-baseline paths have comparable CIFAR-10 test-set evaluations:

| Method | Evaluation task | Test-set Top-1 accuracy | Correct / total |
|---|---|---:|---:|
| Supervised short baseline | Task 33 | 0.873700 | 8737 / 10000 |
| SimCLR short + linear probe | Task 34 | 0.621400 | 6214 / 10000 |

The supervised short baseline used a supervised ResNet18 trained for 10 epochs. The SimCLR path used a 10-epoch SimCLR pretrain and a 5-epoch linear probe trained on the short SimCLR checkpoint.

## What Was Not Evaluated

- No longer supervised baseline was evaluated.
- No longer SimCLR pretraining run was evaluated.
- No ablation was evaluated.
- No embedding visualization was created.
- No final baseline table or final report claim was produced.
- No comparison with the SimCLR paper, ImageNet results, or external benchmarks was made.

## Why Training-Batch Metrics Were Not Enough

Tasks 28-30 recorded training-log values:

- supervised short final logged train accuracy: `0.9375`;
- SimCLR short final logged contrastive loss: `4.090417861938477`;
- linear probe short final logged train accuracy: `0.6640625`.

Those values are useful for checking that the training jobs ran, but they are not held-out test-set metrics. Last-batch training accuracy depends on the final batch composition and training-loop state. SimCLR training loss does not directly measure downstream representation quality.

Task 33 and Task 34 are more meaningful for model comparison because both report Top-1 accuracy on the CIFAR-10 test split with `total=10000`.

## Conservative First Interpretation

The supervised short baseline reached `top1_accuracy=0.873700`. The SimCLR short plus linear probe path reached `top1_accuracy=0.621400`.

The current short SimCLR setup is lower than the supervised short baseline by `0.252300` Top-1 accuracy, or 25.23 percentage points. This should not be treated as final SimCLR performance.

Likely reasons:

- SimCLR pretraining was only 10 epochs.
- Contrastive learning often benefits from longer pretraining and larger batches.
- No hyperparameter tuning has been done yet.
- The current implementation prioritizes a reproducible pipeline and honest first comparison over best possible accuracy.

This stage validates that the project can train, checkpoint, evaluate, and compare the two baseline paths under controlled short-baseline conditions.

## Result Table

The concise comparison table is stored in:

```text
results/tables/short_baseline_results.md
```

## Next Recommended Stage

Do not jump directly to ablation yet.

Recommended order:

1. Review and commit this Task 35 result table and analysis.
2. Decide whether to update README/status with a cautious short-baseline table.
3. Plan the first ablation stage separately, with clear scope and expected result files.

## Limitations

- These are preliminary short-baseline results.
- They are not final benchmark results.
- They should not be used to claim state-of-the-art performance.
- They should not be compared against the original SimCLR paper numbers or ImageNet-scale results.
