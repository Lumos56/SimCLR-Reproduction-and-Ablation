# Experiment 15: Supervised Short Evaluation

## Purpose

Record the Human Owner-run CIFAR-10 test-set evaluation for the supervised short baseline.

This is an evaluation record, not a training run. Codex did not rerun evaluation, run training, run ablation, download data, or create checkpoints for this task.

## Evaluation Scope

| Field | Value |
|---|---|
| Task | Task 33 |
| Model | Supervised ResNet18 short baseline |
| Training scope | 10-epoch short baseline |
| Evaluation split | CIFAR-10 test split |
| Evaluation config | `configs/evaluate_supervised_short.yaml` |
| Result CSV | `results/tables/supervised_short_eval.csv` |
| Checkpoint | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/supervised_short/cifar10_supervised_short.pt` |

## Command Run By Human Owner

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.evaluate --config configs/evaluate_supervised_short.yaml
```

## Observed Output

```text
completed evaluation: mode=supervised dataset=cifar10 top1_accuracy=0.873700 correct=8737 total=10000
output_path=results/tables/supervised_short_eval.csv
```

## Result CSV Content

```csv
mode,dataset,dataset_split,top1_accuracy,correct,total,checkpoint_path,simclr_checkpoint_path
supervised,cifar10,test,0.8737,8737,10000,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/supervised_short/cifar10_supervised_short.pt,
```

## Metric Interpretation

- `top1_accuracy=0.873700` is a real CIFAR-10 test-set Top-1 accuracy for the supervised short baseline checkpoint.
- `correct=8737` and `total=10000` mean the evaluated supervised short checkpoint classified 8737 of 10000 CIFAR-10 test examples correctly.
- This is preliminary short-baseline evaluation evidence.
- This is not the final supervised baseline result because the supervised model was trained only for the approved 10-epoch short-baseline scope.
- This result must not be described as final project performance or state-of-the-art performance.

## Provenance

| Field | Value |
|---|---|
| mode | `supervised` |
| dataset | `cifar10` |
| dataset_split | `test` |
| checkpoint_path | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/supervised_short/cifar10_supervised_short.pt` |
| simclr_checkpoint_path | Not applicable for supervised evaluation |

## Repository Safety

The Human Owner reported:

- `results/tables/supervised_short_eval.csv` is untracked and may be committed as a small evaluation result table.
- No repository data files were found.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository.
- No files over 10MB were found inside the repository.

Codex performed read-only safety checks for this recording task and did not create checkpoints or large artifacts.

## Limitations

- This evaluation covers only the supervised short baseline.
- Linear-probe short evaluation has not been recorded yet.
- Ablations have not started.
- Longer supervised baseline training has not been run or evaluated.

## Next Step

Review and commit Task 33, then proceed to Task 34 linear probe short evaluation if approved by the Human Owner.
