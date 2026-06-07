# Experiment 29: Augmentation Ablation Analysis

## Purpose

Record the second core ablation analysis after the weak augmentation setup, weak augmentation SimCLR short pretrain, weak augmentation linear probe short training, and weak augmentation linear probe CIFAR-10 test-set evaluation.

This ablation focuses on strong vs weak augmentation. It is analysis and documentation only. It uses existing result CSVs and does not run training, evaluation, tests, figure generation, or checkpoint creation.

## Compared Runs

| Run | Augmentation strength | Projection head | SimCLR pretrain | Linear probe | Evaluation split | Result CSV |
|---|---|---|---|---|---|---|
| Strong augmentation SimCLR short + linear probe | Strong | Enabled | CIFAR-10, 10 epochs | CIFAR-10, 5 epochs | CIFAR-10 test | `results/tables/linear_probe_short_eval.csv` |
| Weak augmentation SimCLR short + linear probe | Weak | Enabled | CIFAR-10, 10 epochs | CIFAR-10, 5 epochs | CIFAR-10 test | `results/tables/linear_probe_weak_aug_short_eval.csv` |

## Result

| Metric | Strong augmentation SimCLR short + linear probe | Weak augmentation SimCLR short + linear probe | Difference |
|---|---:|---:|---:|
| CIFAR-10 test Top-1 accuracy | 0.621400 | 0.356600 | -0.264800 |
| Correct / total | 6214 / 10000 | 3566 / 10000 | -2648 correct |
| Percentage-point difference | - | - | -26.48 pp |

All values come from existing result CSVs:

- `results/tables/linear_probe_short_eval.csv`
- `results/tables/linear_probe_weak_aug_short_eval.csv`

## Conservative Interpretation

- The weak augmentation run is much lower than the strong augmentation baseline in this short comparison.
- This is consistent with SimCLR's reliance on strong data augmentation to create useful contrastive views.
- This result is not definitive because the run is short, single-seed, and not tuned.
- This result should not be treated as final SimCLR performance or a final benchmark result.
- This result should not be compared with paper-scale SimCLR results.

## Limitations

- CIFAR-10 only.
- 10-epoch SimCLR pretraining.
- 5-epoch linear probe.
- Single run.
- No repeated seeds.
- No long baseline.
- No hyperparameter tuning.

## Not Done

- No new training was run.
- No new evaluation was run.
- No tests were run.
- No figures were created.
- No checkpoints were created.
- No ablation beyond augmentation strength was started in this task.
- No final benchmark claim was made.

## Next Stage

The next stage should be decided separately. A good candidate is:

```text
batch size 64 vs 128
```

Do not start the next ablation inside Task 50.
