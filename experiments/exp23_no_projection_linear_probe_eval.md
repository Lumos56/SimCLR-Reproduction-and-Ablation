# Experiment 23: No Projection Linear Probe Evaluation

## Purpose

Record the Human Owner-run CIFAR-10 test-set evaluation for the no-projection linear probe trained on the no-projection SimCLR short checkpoint.

This is an evaluation record, not a training run. Codex did not rerun evaluation, run training, run supervised evaluation, run ablation table generation, download data, or create checkpoints for this task.

## Evaluation Scope

| Field | Value |
|---|---|
| Task | Task 43 |
| Model | No-projection linear probe trained on no-projection SimCLR encoder |
| SimCLR pretrain scope | 10-epoch no-projection short SimCLR pretrain |
| Linear probe training scope | 5-epoch no-projection short linear probe |
| Evaluation split | CIFAR-10 test split |
| Evaluation config | `configs/evaluate_linear_probe_no_projection_short.yaml` |
| Result CSV | `results/tables/linear_probe_no_projection_short_eval.csv` |
| Linear probe checkpoint | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_no_projection_short/cifar10_linear_probe_no_projection_short.pt` |
| SimCLR checkpoint | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_no_projection_short/cifar10_simclr_no_projection_short.pt` |

## Command Run By Human Owner

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.evaluate --config configs/evaluate_linear_probe_no_projection_short.yaml
```

## Observed Output

```text
completed evaluation: mode=linear_probe dataset=cifar10 top1_accuracy=0.594500 correct=5945 total=10000
output_path=results/tables/linear_probe_no_projection_short_eval.csv
```

## Result CSV Content

```csv
mode,dataset,dataset_split,top1_accuracy,correct,total,checkpoint_path,simclr_checkpoint_path
linear_probe,cifar10,test,0.5945,5945,10000,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_no_projection_short/cifar10_linear_probe_no_projection_short.pt,/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_no_projection_short/cifar10_simclr_no_projection_short.pt
```

## Metric Interpretation

- `top1_accuracy=0.594500` is a real CIFAR-10 test-set Top-1 accuracy for this short no-projection linear probe run.
- `correct=5945` and `total=10000` mean the evaluated no-projection linear probe classified 5945 of 10000 CIFAR-10 test examples correctly.
- This is the CIFAR-10 test-set evaluation metric for the no-projection short linear probe.
- This remains a short ablation result, not final SimCLR performance.
- This result must not be described as a final benchmark result or final project performance.
- Task 44 will compare this result against the baseline SimCLR short plus linear-probe result and build the first no-projection ablation interpretation.

## Provenance

| Field | Value |
|---|---|
| mode | `linear_probe` |
| dataset | `cifar10` |
| dataset_split | `test` |
| checkpoint_path | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_no_projection_short/cifar10_linear_probe_no_projection_short.pt` |
| simclr_checkpoint_path | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_no_projection_short/cifar10_simclr_no_projection_short.pt` |

## Repository Safety

The Human Owner reported:

- `results/tables/linear_probe_no_projection_short_eval.csv` is untracked and may be committed as a small evaluation result table.
- No repository data files were reported.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were reported inside the repository.
- No files over 10MB were reported inside the repository.

Codex performed read-only safety checks for this recording task and did not create checkpoints or large artifacts.

Codex safety check results:

- `git diff --check` passed.
- No disallowed `src/*`, `configs/*`, `tests/*`, `README.md`, `AGENTS.md`, training logs, or `notes/decision_log.md` paths were listed as modified.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository.
- No files over 10MB were found inside the repository.
- The linear probe checkpoint and no-projection SimCLR checkpoint were confirmed with read-only `ls -lh` outside the repository.

## Limitations

- This evaluation covers only the short no-projection SimCLR plus short no-projection linear-probe path.
- This task does not compare the result against the baseline SimCLR short plus linear probe result.
- No ablation result table or first interpretation was created in Task 43.
- Longer SimCLR pretraining and final baseline or ablation evaluation have not been run.

## Not Run

- Codex did not rerun evaluation.
- Codex did not run training.
- Codex did not run supervised evaluation.
- Codex did not run ablation table generation.
- Codex did not create checkpoints.
- Codex did not load external checkpoint weights.
- Codex did not move, delete, or edit external checkpoints.
- Codex did not fabricate or alter metrics.

## Next Step

Review and commit Task 43, then proceed to Task 44 no-projection ablation result table and first interpretation if approved by the Human Owner.
