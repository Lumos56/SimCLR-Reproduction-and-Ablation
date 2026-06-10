# Experiment 33: Batch64 Linear Probe Evaluation

## Purpose

Record the Human Owner-run CIFAR-10 test-set evaluation result for the batch64 SimCLR short plus linear probe setup using:

```text
configs/evaluate_linear_probe_batch64_short.yaml
```

This task records the evaluation result only. It does not run training, rerun evaluation, create the batch-size ablation result table, create figures, run tests, or start Task 55.

## Evaluation Scope

| Field | Value |
|---|---|
| Task | Task 54 |
| Mode | Linear probe |
| Dataset | CIFAR-10 |
| Evaluation split | Test |
| Evaluation config | `configs/evaluate_linear_probe_batch64_short.yaml` |
| Result CSV | `results/tables/linear_probe_batch64_short_eval.csv` |
| Linear probe checkpoint | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_batch64_short/cifar10_linear_probe_batch64_short.pt` |
| SimCLR checkpoint | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_batch64_short/cifar10_simclr_batch64_short.pt` |

## Command

Run by the Human Owner:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.evaluate --config configs/evaluate_linear_probe_batch64_short.yaml
```

## Observed Output

```text
completed evaluation: mode=linear_probe dataset=cifar10 top1_accuracy=0.596100 correct=5961 total=10000
output_path=results/tables/linear_probe_batch64_short_eval.csv
```

## Result CSV

Path:

```text
results/tables/linear_probe_batch64_short_eval.csv
```

CSV content:

```csv
mode,dataset,dataset_split,top1_accuracy,correct,total,checkpoint_path,simclr_checkpoint_path
linear_probe,cifar10,test,0.5961,5961,10000,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_batch64_short/cifar10_linear_probe_batch64_short.pt,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_batch64_short/cifar10_simclr_batch64_short.pt
```

## Metric

| Metric | Value |
|---|---:|
| Dataset | CIFAR-10 |
| Split | test |
| Mode | linear probe |
| Top-1 accuracy | 0.596100 |
| Correct / total | 5961 / 10000 |

`top1_accuracy=0.596100` is a real CIFAR-10 test-set metric for the batch64 SimCLR short plus linear probe setup.

## Checkpoints

Linear probe checkpoint:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_batch64_short/cifar10_linear_probe_batch64_short.pt
```

SimCLR checkpoint:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_batch64_short/cifar10_simclr_batch64_short.pt
```

Both checkpoints are external artifacts outside the Git repository and must not be committed.

## Interpretation Boundary

- This is a short ablation result.
- This is not final SimCLR performance.
- This is not final project performance.
- Do not compare this result to paper-scale SimCLR results.
- Do not deeply interpret the batch-size ablation in Task 54.
- Task 55 will compare batch64 against the batch128 baseline.
- The batch-size comparison remains preliminary because this project uses fixed epochs, not fixed optimizer steps.

## Comparison Reference For Task 55

Do not create the batch-size ablation result table in this task. Task 55 should use these values:

| Run | CIFAR-10 test Top-1 |
|---|---:|
| Batch size 128 baseline SimCLR short + linear probe | 0.621400 |
| Batch size 64 SimCLR short + linear probe | 0.596100 |

Difference for Task 55:

```text
0.596100 - 0.621400 = -0.025300
```

This is a difference of -2.53 percentage points.

## Repository Safety Check

- `results/tables/linear_probe_batch64_short_eval.csv` is a small evaluation result CSV and should be included in the Task 54 commit.
- No repository data files were reported.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository by Codex.
- No files over 10MB were found inside the repository by Codex.
- The checkpoints remain in external model storage.

## Not Done

- Codex did not rerun evaluation.
- Codex did not run training.
- Codex did not run tests.
- Codex did not create checkpoints.
- Codex did not create figures.
- Codex did not edit existing result tables.
- Codex did not create the batch-size ablation table.
- Codex did not start Task 55.
- No final SimCLR performance claim was made.

## Next Step

Task 55 should create the batch-size ablation result table and first conservative interpretation after Human Owner approval.
