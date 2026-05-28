# Experiment 02: CIFAR-10 Smoke Preflight

## Purpose

Record the Human Owner's read-only preflight check for `configs/cifar10_simclr_smoke.yaml` before any real CIFAR-10 smoke training run.

## Preflight Result

The config is safe for a future smoke run because it uses external storage paths and has `download: false`. The real CIFAR-10 smoke run is not ready yet because CIFAR-10 data was not present during preflight.

## Observed Config Values

| Field | Value |
|---|---|
| `dataset.name` | `cifar10` |
| `dataset.data_root` | `/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation` |
| `dataset.download` | `false` |
| `training.epochs` | `1` |
| `training.batch_size` | `32` |
| `training.max_train_batches` | `10` |
| `paths.log_dir` | `results/logs` |
| `paths.checkpoint_dir` | `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/checkpoints` |

## Storage Preflight

Observed by the Human Owner:

- `/home/yeyee/research` points to `/mnt/f/Research`.
- Dataset directory did not exist during preflight.
- Model directory exists.
- Export directory did not exist during preflight.
- No CIFAR-10 files were found.
- Repository status was clean.

## Readiness Assessment

- Config safety: PASS.
- Storage mapping: PASS.
- Repository cleanliness: PASS.
- CIFAR-10 data availability: NOT READY.
- Real CIFAR-10 smoke training readiness: BLOCKED until the owner explicitly approves CIFAR-10 download or provides the dataset at the configured external path.

## Owner Approval Required

CIFAR-10 must not be downloaded automatically. Downloading CIFAR-10 requires explicit owner approval and must target the external dataset path:

```text
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation
```

## Not Run

- No CIFAR-10 download was performed.
- No training was run.
- No checkpoint was created.
- No dataset, model, loss, training, evaluation, or ablation code was modified.

## Next Step

Owner decision needed: approve CIFAR-10 download to the external dataset directory, or provide the CIFAR-10 files there before running the real smoke test.
