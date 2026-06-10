# Batch Size Ablation Results

This table records short batch-size ablation evidence on CIFAR-10. It compares the existing SimCLR short plus linear-probe baseline using SimCLR pretraining batch size 128 against the matching batch64 SimCLR short plus linear-probe run.

These are short ablation results. They are not final SimCLR performance, not final project performance, and not paper-scale SimCLR comparisons.

| Method | SimCLR pretrain batch size | Linear probe batch size | Projection head setting | Augmentation strength | Pretrain epochs | Linear probe epochs | CIFAR-10 test Top-1 accuracy | Correct / total | Result file | SimCLR checkpoint path | Linear probe checkpoint path | Interpretation |
|---|---:|---:|---|---|---:|---:|---:|---:|---|---|---|---|
| Batch128 SimCLR short + linear probe | 128 | 128 | Enabled | Strong | 10 | 5 | 0.621400 | 6214 / 10000 | `results/tables/linear_probe_short_eval.csv` | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_short/cifar10_simclr_short.pt` | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_short/cifar10_linear_probe_short.pt` | Short baseline reference for the current SimCLR plus linear-probe path. |
| Batch64 SimCLR short + linear probe | 64 | 128 | Enabled | Strong | 10 | 5 | 0.596100 | 5961 / 10000 | `results/tables/linear_probe_batch64_short_eval.csv` | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_batch64_short/cifar10_simclr_batch64_short.pt` | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_batch64_short/cifar10_linear_probe_batch64_short.pt` | Short batch64 ablation result. Lower than the batch128 baseline in this short run. |

## Difference

Batch64 minus batch128:

```text
0.596100 - 0.621400 = -0.025300
```

The batch64 run is 2.53 percentage points lower than the batch128 baseline in this short setup.

## Interpretation Note

- The batch64 result is slightly lower than the batch128 baseline in this short, single-run comparison.
- This may suggest that the original batch128 setting worked better in the current short setup.
- This does not prove that batch size 128 is universally better than batch size 64.
- This comparison uses fixed epochs, not fixed optimizer steps, so batch64 and batch128 do not have matched optimizer-step counts.
- Batch64 produced more optimizer steps per epoch during SimCLR pretraining than batch128.
- The result is limited by the short 10-epoch pretraining run, 5-epoch linear probe, one dataset, one seed, and no batch-size hyperparameter tuning.
- The supervised short baseline exists as broader project context, but it is not a primary row in this ablation table because this ablation compares SimCLR batch-size variants.
