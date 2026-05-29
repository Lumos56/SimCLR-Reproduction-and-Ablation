# Experiment 04: CIFAR-10 Smoke CLI Run

## Purpose

Record the first real CIFAR-10 SimCLR smoke run after CIFAR-10 was downloaded to the approved external F-drive research data directory.

This is a smoke training run only. It verifies that the real CIFAR-10 data path, model, loss, optimizer, CSV logging, and external checkpoint path can work together for a tiny controlled run. It is not a baseline experiment.

## Command

Run from the repository root:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.train_simclr --config configs/cifar10_simclr_smoke.yaml
```

## Observed Output

Verified successful output from the Human Owner:

```text
completed smoke training: steps=10 final_loss=3.713874
log_path=results/logs/cifar10_simclr_smoke.csv
checkpoint_path=/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/checkpoints/cifar10_simclr_smoke.pt
```

## CSV Log

Repository log path:

```text
results/logs/cifar10_simclr_smoke.csv
```

Content:

```csv
epoch,step,loss
1,1,4.135377407073975
1,2,4.12536096572876
1,3,4.087895393371582
1,4,4.037651538848877
1,5,3.9758224487304688
1,6,3.9681997299194336
1,7,3.902341365814209
1,8,3.590588092803955
1,9,3.7160251140594482
1,10,3.713874340057373
```

## Checkpoint

External checkpoint path:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/checkpoints/cifar10_simclr_smoke.pt
```

- Checkpoint size: about 132M
- Location: outside the Git repository
- Repository checkpoint/model files created: no

## Repository Safety Check

Owner-verified repository checks:

- `results/logs/cifar10_simclr_smoke.csv` is a small smoke log and may be committed.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository.
- No files over 10MB were found inside the repository.
- No dataset files were found inside repository `data/`.

## Limitation

This run used only 1 epoch and 10 batches. It is not a meaningful accuracy result, convergence result, or baseline experiment. It should be treated only as evidence that the real CIFAR-10 smoke training path can start, run for a tiny number of batches, log loss, and save a checkpoint to external storage.

## Not Run

- No linear probe was run.
- No supervised baseline was run.
- No evaluation was run.
- No ablation was run.
- No long training was run.

## Next Step

Review and commit this smoke run record, then decide the next engineering step before starting any baseline, evaluation, ablation, or long run.
