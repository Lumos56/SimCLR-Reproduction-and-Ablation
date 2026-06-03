# Short Baseline Results

This table summarizes the first comparable CIFAR-10 test-set evaluation results for the short-baseline stage.

These are short baseline results. They are not final benchmark results, not state-of-the-art claims, and not final project performance.

| Method | Training setup | Evaluation split | Top-1 accuracy | Correct / total | Checkpoint path | Result file | Interpretation |
|---|---|---|---:|---:|---|---|---|
| Supervised short baseline | Supervised ResNet18, CIFAR-10, 10 epochs | CIFAR-10 test | 0.873700 | 8737 / 10000 | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/supervised_short/cifar10_supervised_short.pt` | `results/tables/supervised_short_eval.csv` | Short baseline test-set metric. Higher than the current short SimCLR plus linear-probe result, but not final supervised baseline performance. |
| SimCLR short + linear probe | SimCLR pretrain, CIFAR-10, 10 epochs; linear probe, 5 epochs | CIFAR-10 test | 0.621400 | 6214 / 10000 | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_short/cifar10_linear_probe_short.pt`; encoder from `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_short/cifar10_simclr_short.pt` | `results/tables/linear_probe_short_eval.csv` | Short baseline test-set metric for the current contrastive pipeline. Lower than supervised short baseline, but not final SimCLR performance. |

## First Interpretation

- The supervised short baseline is higher than the current short SimCLR plus linear-probe result.
- This is expected and is not a failure: the SimCLR pretraining stage is short, batch size is limited, and no ablation or hyperparameter tuning has been done.
- The value of this stage is pipeline validation and the first controlled comparison between supervised training and SimCLR representation learning on the same CIFAR-10 test split.
- These results should be used as preliminary short-baseline evidence before a separate ablation plan, not as final benchmark numbers.
