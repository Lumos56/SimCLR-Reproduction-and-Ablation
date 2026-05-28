# Experiment 01: Fake Smoke CLI Run

## Purpose

Record the first manual fake-data SimCLR smoke CLI run. This confirms that the Gate 2 smoke training entry point can run from the command line with fake data, write a small CSV log inside the repository, and save the checkpoint outside the repository.

## Dataset

- Dataset mode: fake
- Real CIFAR-10 downloaded: no
- Real CIFAR-10 training run: no

## Command That Failed

```bash
python src/train_simclr.py --config configs/simclr_fake_smoke.yaml
```

Error:

```text
ModuleNotFoundError: No module named 'src'
```

## Fixed Command

Run the CLI as a module from the repository root:

```bash
python -m src.train_simclr --config configs/simclr_fake_smoke.yaml
```

Owner-used environment command:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.train_simclr --config configs/simclr_fake_smoke.yaml
```

## Result

Verified successful output from the Human Owner:

```text
completed smoke training: steps=2 final_loss=1.900701
log_path=results/logs/simclr_fake_smoke.csv
checkpoint_path=/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/checkpoints/simclr_fake_smoke.pt
```

## CSV Log

Repository log path:

```text
results/logs/simclr_fake_smoke.csv
```

Content:

```csv
epoch,step,loss
1,1,1.9976015090942383
1,2,1.9007006883621216
```

## Checkpoint

External checkpoint path:

```text
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/checkpoints/simclr_fake_smoke.pt
```

- Checkpoint size: about 132M
- Location: outside the Git repository
- Repository checkpoint/model files created: no

## Repository Safety Check

Owner-verified repository checks:

- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository.
- No files over 10MB were found inside the repository.
- `results/logs/simclr_fake_smoke.csv` is a small CSV log and may be committed.

## Limitation

This is a fake-data smoke run only. It does not validate real CIFAR-10 training quality, downstream linear probing, supervised baseline performance, evaluation, ablation behavior, or any real experiment result.

## Next Step

Review and commit this fake smoke CLI record, then decide whether to run the Gate 2 real CIFAR-10 smoke test.
