# Experiment 27: Weak Augmentation Linear Probe Short

## Purpose

Record the Human Owner-run weak augmentation linear probe short training result using:

```text
configs/cifar10_linear_probe_weak_aug_short.yaml
```

The training script printed `completed linear probe smoke training`, but this run used the weak augmentation linear probe short ablation config. Therefore this record treats it as weak augmentation linear probe short training, not as a smoke run.

## Config

- Dataset: CIFAR-10.
- `dataset.download`: `false`.
- `dataset.augmentation_strength`: `weak`.
- Epochs: 5.
- Batch size: 128.
- `paths.save_checkpoint`: `true`.
- Config path: `configs/cifar10_linear_probe_weak_aug_short.yaml`.
- SimCLR checkpoint path: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/simclr_weak_aug_short/cifar10_simclr_weak_aug_short.pt`.

## Command Result

```text
completed linear probe smoke training: steps=1950 final_train_loss=1.719550 final_train_acc=0.351562
log_path=results/logs/cifar10_linear_probe_weak_aug_short.csv
checkpoint_path=/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_weak_aug_short/cifar10_linear_probe_weak_aug_short.pt
```

## Metrics

| Metric | Value |
|---|---:|
| Steps | 1950 |
| Final logged train loss | 1.719550 |
| Final logged train accuracy | 0.351562 |

The precise last CSV value is:

```text
5,1950,1.7195498943328857,0.3515625
```

The final train accuracy is the last logged training-batch accuracy. It is not test accuracy, not final model performance, and not the weak augmentation ablation test-set metric.

The weak augmentation ablation test-set metric must be produced later by Task 49.

## CSV Log

- Path: `results/logs/cifar10_linear_probe_weak_aug_short.csv`.
- Size observed by Codex: `68K`.
- Lines observed by Codex: 1951 including header.

First rows:

```text
epoch,step,train_loss,train_acc
1,1,2.3146891593933105,0.109375
1,2,2.2980875968933105,0.109375
1,3,2.2566404342651367,0.1796875
1,4,2.2644152641296387,0.1484375
```

Last rows:

```text
5,1941,1.7187254428863525,0.4375
5,1942,1.639784336090088,0.3671875
5,1943,1.7275360822677612,0.375
5,1944,1.6661274433135986,0.3984375
5,1945,1.6422919034957886,0.4296875
5,1946,1.7917637825012207,0.328125
5,1947,1.7730505466461182,0.3203125
5,1948,1.6959178447723389,0.3828125
5,1949,1.7827671766281128,0.390625
5,1950,1.7195498943328857,0.3515625
```

## External Checkpoint

- Path: `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/linear_probe_weak_aug_short/cifar10_linear_probe_weak_aug_short.pt`.
- Size reported by the Human Owner: about 65K.
- This checkpoint is outside the Git repository, which is correct.

## Interpretation

- This is weak augmentation linear probe short training.
- It used the weak augmentation SimCLR short checkpoint.
- It used `augmentation_strength=weak` for linear probe training.
- The final train accuracy is training-batch accuracy only.
- The final train accuracy is not test accuracy or final model performance.
- This is not the weak augmentation ablation test-set metric yet.
- Do not compare this training-batch accuracy directly against CIFAR-10 test-set results.

## Repository Safety

- The CSV log is small enough to keep in the repository.
- The checkpoint remains in external model storage.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` file should be committed.
- No repository data files should be committed.

## Not Done

- Codex did not rerun training.
- Codex did not run evaluation.
- Codex did not run a supervised baseline.
- Codex did not run ablation analysis.
- Codex did not create checkpoints.

## Next Step

Task 49 should record the weak augmentation linear probe CIFAR-10 test-set evaluation result after the Human Owner runs it.
