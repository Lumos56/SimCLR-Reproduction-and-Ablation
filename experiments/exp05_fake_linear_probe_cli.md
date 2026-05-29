# Experiment 05: Fake Linear Probe CLI Smoke Run

## Purpose

Record the Human Owner's manual fake-data linear probe CLI smoke run.

This is fake-data smoke validation only. It verifies that the linear probe CLI can load the configured SimCLR checkpoint, freeze the encoder, train the classifier for a tiny fake-data run, and write a small CSV log. It is not a real CIFAR-10 linear probe run and not an evaluation result.

## Command

Run from the repository root:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.train_linear_probe --config configs/linear_probe_fake_smoke.yaml
```

## Observed Output

Verified successful output from the Human Owner:

```text
completed linear probe smoke training: steps=2 final_train_loss=2.759471 final_train_acc=0.250000
log_path=results/logs/linear_probe_fake_smoke.csv
```

## CSV Log

Repository log path:

```text
results/logs/linear_probe_fake_smoke.csv
```

Content:

```csv
epoch,step,train_loss,train_acc
1,1,2.2778279781341553,0.0
1,2,2.7594711780548096,0.25
```

## Interpretation

- This run used fake data only.
- `final_train_acc=0.25` is not a real model performance result.
- The logged `train_acc` must not be reported as real evaluation accuracy.
- This run does not validate real CIFAR-10 linear probing, baseline performance, convergence, generalization, or representation quality.

## Checkpoint Behavior

The config has:

```yaml
save_checkpoint: false
```

Therefore no linear probe checkpoint was expected or saved.

Observed by the Human Owner:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe
```

did not exist, which is expected for this fake smoke run.

## Repository Safety Check

Owner-verified repository checks:

- `results/logs/linear_probe_fake_smoke.csv` is a small smoke log and may be committed.
- No repository data files were found.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository.
- No files over 10MB were found inside the repository.

## Not Run

- No real CIFAR-10 linear probe was run.
- No fake linear probe training was rerun by Codex for this task.
- No data was downloaded.
- No checkpoint was created.
- No supervised baseline was implemented or run.
- No evaluation report was implemented.
- No ablation or long run was started.

## Next Step

Review and commit this fake linear probe smoke record, then decide whether to run a real CIFAR-10 linear probe smoke command.
