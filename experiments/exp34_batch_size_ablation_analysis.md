# Experiment 34: Batch Size Ablation Analysis

## Purpose

Record the third core ablation analysis after the no-projection and weak-augmentation ablation cycles.

This ablation focuses on SimCLR pretraining batch size 128 vs 64. It is analysis and documentation only. It uses existing result CSVs and does not run training, evaluation, tests, figure generation, checkpoint creation, or CSV editing.

## Compared Runs

| Run | SimCLR pretrain batch size | Linear probe batch size | Projection head | Augmentation strength | SimCLR pretrain | Linear probe | Evaluation split | Result CSV |
|---|---:|---:|---|---|---|---|---|---|
| Batch128 SimCLR short + linear probe | 128 | 128 | Enabled | Strong | CIFAR-10, 10 epochs | CIFAR-10, 5 epochs | CIFAR-10 test | `results/tables/linear_probe_short_eval.csv` |
| Batch64 SimCLR short + linear probe | 64 | 128 | Enabled | Strong | CIFAR-10, 10 epochs | CIFAR-10, 5 epochs | CIFAR-10 test | `results/tables/linear_probe_batch64_short_eval.csv` |

All values come from existing result CSVs:

- `results/tables/linear_probe_short_eval.csv`
- `results/tables/linear_probe_batch64_short_eval.csv`

## Result

| Metric | Batch128 SimCLR short + linear probe | Batch64 SimCLR short + linear probe | Difference |
|---|---:|---:|---:|
| CIFAR-10 test Top-1 accuracy | 0.621400 | 0.596100 | -0.025300 |
| Correct / total | 6214 / 10000 | 5961 / 10000 | -253 correct |
| Percentage-point difference | - | - | -2.53 pp |

## Conservative Interpretation

- The batch64 run is slightly lower than the batch128 baseline in this short comparison.
- This may suggest that the original batch128 setting worked better in the current short setup.
- This conclusion is preliminary because the comparison uses fixed epochs, not fixed optimizer steps.
- Batch64 had more optimizer steps per epoch than batch128 during SimCLR pretraining.
- The result is single-seed, short-run, and not tuned, so it does not support strong claims about batch size in general.
- This result should not be treated as final SimCLR performance or a final benchmark result.
- This result should not be compared with paper-scale SimCLR results.

## Limitations

- CIFAR-10 only.
- 10-epoch SimCLR pretraining.
- 5-epoch linear probe.
- Single run.
- No repeated seeds.
- No long training.
- Fixed epochs rather than fixed optimizer steps.
- No hyperparameter tuning for batch size.

## Not Done

- No new training was run.
- No new evaluation was run.
- No tests were run.
- No figures were created.
- No checkpoints were created.
- No CSV files were edited.
- No final benchmark claim was made.
- No combined ablation summary table was created.

## Next Stage

The next stage should build a combined ablation summary table across projection head, augmentation strength, and batch size.

Do not start the combined summary inside Task 55.
