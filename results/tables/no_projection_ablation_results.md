# No-Projection Ablation Results

This table records short no-projection ablation evidence on CIFAR-10. It compares the existing short SimCLR plus linear-probe baseline against the matching no-projection short SimCLR plus linear-probe run.

These are short ablation results. They are not final SimCLR performance, not final project performance, and not paper-scale SimCLR comparisons.

| Method | Projection head setting | Pretrain epochs | Linear probe epochs | CIFAR-10 test Top-1 accuracy | Correct / total | Result file | Checkpoint paths | Interpretation |
|---|---|---:|---:|---:|---:|---|---|---|
| Baseline SimCLR short + linear probe | Enabled | 10 | 5 | 0.621400 | 6214 / 10000 | `results/tables/linear_probe_short_eval.csv` | Linear probe: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_short/cifar10_linear_probe_short.pt`<br>SimCLR: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_short/cifar10_simclr_short.pt` | Short baseline reference for the current SimCLR plus linear-probe path. |
| No-projection SimCLR short + linear probe | Disabled | 10 | 5 | 0.594500 | 5945 / 10000 | `results/tables/linear_probe_no_projection_short_eval.csv` | Linear probe: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_no_projection_short/cifar10_linear_probe_no_projection_short.pt`<br>SimCLR: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_no_projection_short/cifar10_simclr_no_projection_short.pt` | Short no-projection ablation result. Lower than the projection-head baseline in this short run. |

## Difference

No-projection minus baseline:

```text
0.594500 - 0.621400 = -0.026900
```

The no-projection run is 2.69 percentage points lower than the baseline SimCLR short plus linear-probe run.

## Interpretation Note

- The no-projection result is lower in this short, single-run comparison.
- This is consistent with the idea that the projection head may help representation learning in this setup.
- This does not prove that the projection head is definitively necessary.
- The result is limited by the short 10-epoch pretraining run, 5-epoch linear probe, one dataset, one seed, and no tuning.
- The supervised short baseline exists as broader project context, but it is not a primary row in this ablation table because this ablation compares SimCLR variants.
