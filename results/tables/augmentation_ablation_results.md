# Augmentation Ablation Results

This table records short augmentation ablation evidence on CIFAR-10. It compares the existing strong-augmentation SimCLR short plus linear-probe baseline against the matching weak-augmentation SimCLR short plus linear-probe run.

These are short ablation results. They are not final SimCLR performance, not final project performance, and not paper-scale SimCLR comparisons.

| Method | Augmentation strength | Projection head setting | Pretrain epochs | Linear probe epochs | CIFAR-10 test Top-1 accuracy | Correct / total | Result file | Checkpoint paths | Interpretation |
|---|---|---|---:|---:|---:|---:|---|---|---|
| Strong augmentation SimCLR short + linear probe | Strong | Enabled | 10 | 5 | 0.621400 | 6214 / 10000 | `results/tables/linear_probe_short_eval.csv` | Linear probe: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_short/cifar10_linear_probe_short.pt`<br>SimCLR: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_short/cifar10_simclr_short.pt` | Short baseline reference for the current SimCLR plus linear-probe path. |
| Weak augmentation SimCLR short + linear probe | Weak | Enabled | 10 | 5 | 0.356600 | 3566 / 10000 | `results/tables/linear_probe_weak_aug_short_eval.csv` | Linear probe: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_weak_aug_short/cifar10_linear_probe_weak_aug_short.pt`<br>SimCLR: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_weak_aug_short/cifar10_simclr_weak_aug_short.pt` | Short weak-augmentation ablation result. Much lower than the strong-augmentation baseline in this short run. |

## Difference

Weak augmentation minus strong augmentation:

```text
0.356600 - 0.621400 = -0.264800
```

The weak augmentation run is 26.48 percentage points lower than the strong augmentation baseline in this short setup.

## Interpretation Note

- The weak augmentation result is much lower in this short, single-run comparison.
- This is consistent with SimCLR's reliance on strong data augmentation to create useful contrastive views.
- This does not prove that strong augmentation is universally or definitively better.
- The result is limited by the short 10-epoch pretraining run, 5-epoch linear probe, one dataset, one seed, and no tuning.
- The supervised short baseline exists as broader project context, but it is not a primary row in this ablation table because this ablation compares SimCLR augmentation variants.
