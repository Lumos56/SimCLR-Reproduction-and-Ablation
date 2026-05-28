# Experiment 03: CIFAR-10 External Download

## Purpose

Record the Human Owner-approved CIFAR-10 download to external F-drive research storage. This is a data availability step for Gate 2 preparation, not a training run and not an experiment result.

## Owner Approval

CIFAR-10 was downloaded only after explicit Human Owner approval. The download target was the external research data directory, not the Git repository.

## Data Root

```text
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation
```

Storage mapping verified by the Human Owner:

```text
/home/yeyee/research -> /mnt/f/Research
```

## Download Method

The Human Owner ran the download manually using `torchvision.datasets.CIFAR10`.

## Verified Dataset Counts

| Split | Samples |
|---|---:|
| Train | 50000 |
| Test | 10000 |

## Verified Files

Downloaded archive:

```text
cifar-10-python.tar.gz
```

- Archive size: about 163M

Extracted directory:

```text
cifar-10-batches-py
```

Sample files found:

```text
cifar-10-batches-py/batches.meta
cifar-10-batches-py/data_batch_1
cifar-10-batches-py/data_batch_2
cifar-10-batches-py/data_batch_3
cifar-10-batches-py/data_batch_4
cifar-10-batches-py/data_batch_5
cifar-10-batches-py/readme.html
cifar-10-batches-py/test_batch
cifar-10-python.tar.gz
```

Total data directory size:

```text
341M
```

## Repository Safety Check

Verified by the Human Owner after download:

- `git status --short` was clean after download.
- No files under repository `data/` except `data/README.md`.
- No `.pt`, `.pth`, `.ckpt`, or `.onnx` files were found inside the repository.
- No files over 10MB were found inside the repository.

## Interpretation

CIFAR-10 is now available at the approved external storage path for a future real CIFAR-10 smoke run. This record does not validate model training, loss behavior on real data, accuracy, downstream linear probing, supervised baseline performance, evaluation, or ablation behavior.

## Not Run

- No CIFAR-10 smoke training was run by Codex for this task.
- No fake smoke training was rerun by Codex for this task.
- No checkpoint was created by Codex for this task.
- No dataset, model, loss, training, config, test, or results/log files were modified.

## Next Step

Review and commit this download record, then run the real CIFAR-10 smoke command only after the owner explicitly approves that run.
