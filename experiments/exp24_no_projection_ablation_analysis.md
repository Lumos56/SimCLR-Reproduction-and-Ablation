# Experiment 24: No-Projection Ablation Analysis

## Purpose

Record the first ablation analysis after the no-projection setup, no-projection SimCLR short pretrain, no-projection linear probe short training, and no-projection linear probe CIFAR-10 test-set evaluation.

This is analysis and documentation only. It uses existing result CSVs and does not run training, evaluation, tests, figure generation, or checkpoint creation.

## Compared Runs

| Run | Projection head | SimCLR pretrain | Linear probe | Evaluation split | Result CSV |
|---|---|---|---|---|---|
| Baseline SimCLR short + linear probe | Enabled | CIFAR-10, 10 epochs | CIFAR-10, 5 epochs | CIFAR-10 test | `results/tables/linear_probe_short_eval.csv` |
| No-projection SimCLR short + linear probe | Disabled | CIFAR-10, 10 epochs | CIFAR-10, 5 epochs | CIFAR-10 test | `results/tables/linear_probe_no_projection_short_eval.csv` |

## Result

| Metric | Baseline SimCLR short + linear probe | No-projection SimCLR short + linear probe | Difference |
|---|---:|---:|---:|
| CIFAR-10 test Top-1 accuracy | 0.621400 | 0.594500 | -0.026900 |
| Correct / total | 6214 / 10000 | 5945 / 10000 | -269 correct |
| Percentage-point difference | - | - | -2.69 pp |

All values come from existing result CSVs:

- `results/tables/linear_probe_short_eval.csv`
- `results/tables/linear_probe_no_projection_short_eval.csv`

## Conservative Interpretation

- The no-projection run is lower than the baseline SimCLR short plus linear-probe run in this short comparison.
- This is consistent with the idea that the projection head may help representation learning.
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
- No checkpoint was created.
- No ablation beyond no-projection was started.
- No final benchmark claim was made.

## Next Stage

The next ablation should be planned separately. Good candidates are:

- strong vs weak augmentation;
- batch size 64 vs 128.

Do not start the next ablation inside Task 44.
