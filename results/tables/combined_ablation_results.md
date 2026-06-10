# Combined Ablation Results

This table summarizes the completed short SimCLR ablations on CIFAR-10:
projection head, augmentation strength, and SimCLR pretraining batch size.

All values come from existing result CSVs and existing ablation records. No
training, evaluation, tests, checkpoint creation, figure generation, or CSV
editing was done for this combined summary.

These are short ablation results. They are not final SimCLR performance, not
final project performance, and not paper-scale SimCLR comparisons.

Baseline reference:

```text
Baseline SimCLR short + linear probe Top-1 = 0.621400
Delta vs baseline = variant Top-1 - 0.621400
```

| Run / variant | Changed factor | Projection head | Augmentation strength | SimCLR pretrain batch size | Linear probe batch size | Pretrain epochs | Linear probe epochs | CIFAR-10 test Top-1 | Correct / total | Delta vs baseline | Result file | Interpretation |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Baseline SimCLR short + linear probe | Reference | Enabled | Strong | 128 | 128 | 10 | 5 | 0.621400 | 6214 / 10000 | 0.00 pp | `results/tables/linear_probe_short_eval.csv` | Short SimCLR plus linear-probe baseline used as the reference for completed ablations. |
| No-projection SimCLR short + linear probe | Projection head disabled | Disabled | Strong | 128 | 128 | 10 | 5 | 0.594500 | 5945 / 10000 | -2.69 pp | `results/tables/linear_probe_no_projection_short_eval.csv` | Lower than the projection-head baseline in this short run; consistent with the projection head helping, but not definitive. |
| Weak-augmentation SimCLR short + linear probe | Weak augmentation | Enabled | Weak | 128 | 128 | 10 | 5 | 0.356600 | 3566 / 10000 | -26.48 pp | `results/tables/linear_probe_weak_aug_short_eval.csv` | Largest observed negative drop among completed short ablations; consistent with strong views being important, but not definitive. |
| Batch64 SimCLR short + linear probe | SimCLR pretrain batch size 64 | Enabled | Strong | 64 | 128 | 10 | 5 | 0.596100 | 5961 / 10000 | -2.53 pp | `results/tables/linear_probe_batch64_short_eval.csv` | Slightly lower than the batch128 baseline in this short run; interpretation remains preliminary because the comparison is fixed-epoch, not fixed-step. |

## Source Records

- `results/tables/linear_probe_short_eval.csv`
- `results/tables/linear_probe_no_projection_short_eval.csv`
- `results/tables/linear_probe_weak_aug_short_eval.csv`
- `results/tables/linear_probe_batch64_short_eval.csv`
- `results/tables/no_projection_ablation_results.md`
- `results/tables/augmentation_ablation_results.md`
- `results/tables/batch_size_ablation_results.md`
- `experiments/exp24_no_projection_ablation_analysis.md`
- `experiments/exp29_augmentation_ablation_analysis.md`
- `experiments/exp34_batch_size_ablation_analysis.md`

## Main Observations

- Weak augmentation produced the largest observed negative drop among the
  completed short SimCLR ablations: `-26.48 pp` versus the strong-augmentation
  baseline.
- The no-projection run was lower than the baseline by `-2.69 pp`.
- The batch64 run was lower than the batch128 baseline by `-2.53 pp`.
- The no-projection and batch64 drops are similar in magnitude in these short
  single-run results.
- These observations are preliminary and should not be treated as final evidence
  about representation quality or general SimCLR behavior.

## Limitations

- CIFAR-10 only.
- 10-epoch SimCLR pretraining.
- 5-epoch linear probe.
- Single run per variant.
- No repeated seeds.
- No long training.
- No hyperparameter tuning.
- The batch-size comparison uses fixed epochs, not fixed optimizer steps.
- Batch64 produced more optimizer steps per epoch than batch128 during SimCLR
  pretraining.
- The supervised baseline is broader project context, but it is not a primary row
  here because this table compares SimCLR variants.

## Next Stage

Task 57 should update README v0.3 using the completed short baseline and ablation
records. Task 58 should scaffold the final report after README v0.3 review.

Do not start Task 57 inside Task 56.
