# Experiment 28: Weak Augmentation Linear Probe Evaluation

## Purpose

Record the Human Owner-run weak augmentation linear probe CIFAR-10 test-set evaluation using:

```text
configs/evaluate_linear_probe_weak_aug_short.yaml
```

This is a result-recording task only. Codex did not rerun evaluation.

## Command

The Human Owner ran:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.evaluate --config configs/evaluate_linear_probe_weak_aug_short.yaml
```

## Output

```text
completed evaluation: mode=linear_probe dataset=cifar10 top1_accuracy=0.356600 correct=3566 total=10000
output_path=results/tables/linear_probe_weak_aug_short_eval.csv
```

## Result CSV

Path:

```text
results/tables/linear_probe_weak_aug_short_eval.csv
```

CSV content:

```text
mode,dataset,dataset_split,top1_accuracy,correct,total,checkpoint_path,simclr_checkpoint_path
linear_probe,cifar10,test,0.3566,3566,10000,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_weak_aug_short/cifar10_linear_probe_weak_aug_short.pt,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_weak_aug_short/cifar10_simclr_weak_aug_short.pt
```

## Metric

| Metric | Value |
|---|---:|
| Dataset | CIFAR-10 |
| Split | test |
| Mode | linear probe |
| Top-1 accuracy | 0.356600 |
| Correct / total | 3566 / 10000 |

This is a real CIFAR-10 test-set evaluation metric for the weak augmentation short linear probe trained on the weak augmentation SimCLR short checkpoint.

## Checkpoints

Linear probe checkpoint:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_weak_aug_short/cifar10_linear_probe_weak_aug_short.pt
```

SimCLR checkpoint:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_weak_aug_short/cifar10_simclr_weak_aug_short.pt
```

Both checkpoints are external artifacts outside the Git repository.

## Interpretation

- This is the CIFAR-10 test-set evaluation for the weak augmentation linear probe trained on the weak augmentation SimCLR short checkpoint.
- `top1_accuracy=0.356600` is a real test-set metric for this short weak-augmentation ablation run.
- This is still a short ablation result.
- This is not final SimCLR performance.
- This is not final project performance.
- Do not overstate this as a final benchmark result.
- Task 50 will compare this result against the strong augmentation baseline SimCLR short plus linear probe result.

## Comparison Reference For Task 50

Do not interpret this comparison deeply in Task 49. Task 50 should build the augmentation ablation result table and first conservative interpretation.

| Run | CIFAR-10 test Top-1 |
|---|---:|
| Strong augmentation baseline SimCLR short + linear probe | 0.621400 |
| Weak augmentation SimCLR short + linear probe | 0.356600 |

## Repository Safety

- The evaluation CSV is small enough to keep in the repository.
- No checkpoint should be committed.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` file should be committed.
- No repository data files should be committed.

## Not Done

- Codex did not rerun evaluation.
- Codex did not run training.
- Codex did not run supervised evaluation.
- Codex did not generate an ablation table.
- Codex did not create checkpoints.
- Codex did not fabricate or alter metrics.

## Next Step

Task 50 should build the augmentation ablation result table and first conservative interpretation.
