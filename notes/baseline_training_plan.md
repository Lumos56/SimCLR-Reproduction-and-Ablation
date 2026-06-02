# Baseline Training Plan Decision

Date: 2026-06-03

## Purpose

This is a planning document, not an experiment result.

It defines the first formal baseline stage after smoke validation. It must not be used as evidence of model performance, convergence, or final project quality.

## Current Smoke Validation Status

| Workflow | Status | Evidence |
|---|---|---|
| SimCLR fake smoke | Passed | `experiments/exp01_fake_smoke_cli.md` |
| CIFAR-10 SimCLR smoke | Passed | `experiments/exp04_cifar10_smoke_cli.md` |
| Fake linear probe smoke | Passed | `experiments/exp05_fake_linear_probe_cli.md` |
| CIFAR-10 linear probe smoke | Passed | `experiments/exp07_cifar10_linear_probe_cli.md` |
| Fake supervised smoke | Passed | `experiments/exp08_fake_supervised_cli.md` |
| CIFAR-10 supervised smoke | Passed and merged | `experiments/exp10_cifar10_supervised_cli.md`, Task 24 commit `38639cf` |

Smoke runs verified that the command paths can execute, write small logs, and follow storage rules. Smoke logs are not baseline results.

## First Formal Baseline Stage

The first formal baseline stage is named:

```text
short baseline
```

This stage is intentionally limited. It is meant to produce the first controlled baseline evidence before any longer training, evaluation report, or ablation.

## Proposed Short Baseline

| Component | Plan |
|---|---|
| Dataset | CIFAR-10 |
| Device | `cuda` or `auto` |
| Preferred batch size | `128` |
| Fallback batch size | `64` if CUDA memory issues occur |
| SimCLR pretrain | 10 epochs |
| Linear probe | 5 epochs |
| Supervised baseline | 10 epochs |

The short baseline should use explicit configs created in a separate task. Existing smoke configs should not be edited into baseline configs.

## Recommended Run Order

Recommended order:

1. Supervised short baseline.
2. SimCLR short pretrain.
3. Linear probe on the short SimCLR checkpoint.

## Why Supervised First

- It checks normal supervised training on CIFAR-10 before relying on contrastive checkpoints.
- It gives a sanity-check reference for later SimCLR plus linear-probe results.
- It does not depend on SimCLR checkpoint quality.
- It can reveal data, optimizer, logging, or checkpoint issues in a simpler training path.

## Output Rules

- Raw datasets must remain under `/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation`.
- Checkpoints and model weights must go to `/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation`.
- Large exports must go to `/home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation`.
- Small CSV logs may be committed to the repository.
- Model weights must not be committed.
- TensorBoard event files, W&B runs, `.pt`, `.pth`, `.ckpt`, `.onnx`, and dataset files must not be committed.
- Configs must keep checkpoint paths outside the repository.

## Result Interpretation Rules

- Smoke logs are not baseline results.
- Short baseline results are preliminary.
- The README must not present short baseline metrics as final performance.
- The final report should mark the short baseline as the first controlled run.
- Any failed or partial run must remain in the experiment record.
- No result should be reported without its config, command, seed, dataset path, checkpoint path, and limitations.

## Stopping And Failure Rules

- If CUDA out-of-memory occurs, stop, record the error, and reduce batch size from `128` to `64`.
- If loss becomes NaN or non-finite, stop and record the exact error, command, and config.
- If any checkpoint path writes into the Git repository, stop and fix the config before continuing.
- If training exceeds the approved short-baseline scope, stop and ask the Human Owner.
- If dataset files are missing, do not download automatically; ask the Human Owner.
- If a run produces unexpected large artifacts in the repository, stop and fix storage before continuing.

## Next Task Sequence

Recommended next tasks:

| Task | Scope |
|---|---|
| Task 26 | Create short-baseline configs, but do not run long training yet. |
| Task 27 | Run supervised short baseline. |
| Task 28 | Run SimCLR short pretrain. |
| Task 29 | Run linear probe on the short SimCLR checkpoint. |

Task 26 should only prepare configs and safety checks. It should not start baseline training.

## Decision

Use a short baseline stage before longer baseline training or ablation. Treat short baseline outputs as preliminary controlled-run evidence, not final project performance.
