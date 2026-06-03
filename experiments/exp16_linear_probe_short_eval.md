# Experiment 16: Linear Probe Short Evaluation

## Purpose

Record the Human Owner-run CIFAR-10 test-set evaluation for the linear probe trained on the short SimCLR checkpoint.

This is an evaluation record, not a training run. Codex did not rerun evaluation, run supervised evaluation, run training, run ablation, download data, or create checkpoints for this task.

## Evaluation Scope

| Field | Value |
|---|---|
| Task | Task 34 |
| Model | Linear probe trained on short SimCLR encoder |
| SimCLR pretrain scope | 10-epoch short SimCLR pretrain |
| Linear probe training scope | 5-epoch short linear probe |
| Evaluation split | CIFAR-10 test split |
| Evaluation config | `configs/evaluate_linear_probe_short.yaml` |
| Result CSV | `results/tables/linear_probe_short_eval.csv` |
| Linear probe checkpoint | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_short/cifar10_linear_probe_short.pt` |
| SimCLR checkpoint | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_short/cifar10_simclr_short.pt` |

## Command Run By Human Owner

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.evaluate --config configs/evaluate_linear_probe_short.yaml
```

## Observed Output

```text
completed evaluation: mode=linear_probe dataset=cifar10 top1_accuracy=0.621400 correct=6214 total=10000
output_path=results/tables/linear_probe_short_eval.csv
```

## Result CSV Content

```csv
mode,dataset,dataset_split,top1_accuracy,correct,total,checkpoint_path,simclr_checkpoint_path
linear_probe,cifar10,test,0.6214,6214,10000,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_short/cifar10_linear_probe_short.pt,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_short/cifar10_simclr_short.pt
```

## Metric Interpretation

- `top1_accuracy=0.621400` is a real CIFAR-10 test-set Top-1 accuracy for this short linear probe run.
- `correct=6214` and `total=10000` mean the evaluated linear probe classified 6214 of 10000 CIFAR-10 test examples correctly.
- This is preliminary short-baseline evaluation evidence for SimCLR plus linear probe.
- This is not final SimCLR performance because the SimCLR encoder was pretrained for only the approved 10-epoch short-baseline scope and the linear probe was trained for only 5 epochs.
- This result can be compared with Task 33 supervised short evaluation in Task 35.
- This result must not be described as a final benchmark result or final project performance.

## Provenance

| Field | Value |
|---|---|
| mode | `linear_probe` |
| dataset | `cifar10` |
| dataset_split | `test` |
| checkpoint_path | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_short/cifar10_linear_probe_short.pt` |
| simclr_checkpoint_path | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_short/cifar10_simclr_short.pt` |

## Repository Safety

The Human Owner reported:

- `results/tables/linear_probe_short_eval.csv` is untracked and may be committed as a small evaluation result table.
- No repository data files were found.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository.
- No files over 10MB were found inside the repository.

Codex performed read-only safety checks for this recording task and did not create checkpoints or large artifacts.

## Limitations

- This evaluation covers only the short SimCLR plus short linear-probe path.
- The supervised short evaluation exists separately in `experiments/exp15_supervised_short_eval.md`.
- A compact comparison table and first interpretation have not been created yet.
- Ablations have not started.
- Longer SimCLR pretraining and final baseline evaluation have not been run.

## Next Step

Review and commit Task 34, then proceed to Task 35 short baseline result table and first interpretation if approved by the Human Owner.
