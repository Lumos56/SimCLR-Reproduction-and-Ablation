# Project Status

| 字段 | 当前内容 |
|---|---|
| Current Stage | Gate 3 / Supervised Baseline Scaffold |
| Current Task | Task 21 supervised baseline scaffold |
| Last Completed Task | Task 20 real CIFAR-10 linear probe smoke result merged to main |
| Git State | working on branch `baseline/supervised-scaffold` |
| Branch | `baseline/supervised-scaffold` |
| Next Gate | supervised fake smoke CLI |
| Do Not Start Yet | real supervised baseline, evaluation report, ablation, long runs |
| Blockers | none for Task 21 |
| Next Owner Decision | review Task 21 and decide whether to run supervised fake smoke CLI |

## Gate 0 Status

- [x] Repository skeleton exists.
- [x] Agent rules exist in `AGENTS.md`.
- [x] README v0.1 exists and does not claim experiments are complete.
- [x] Storage policy is documented.
- [x] No dataset/model/loss/training code has been added.
- [x] No dataset, checkpoint, model weight, or large artifact is present.
- [x] Initial setup commit has been created.
- [x] Storage check passed.
- [x] Environment check passed.
- [x] Gate 0 record has been merged to `main`.

## Gate 1 Readiness

- [x] First Gate 1 task has been approved.
- [x] Dataset and augmentation issue has been merged.
- [x] Model encoder and projection head issue has been merged.
- [x] NT-Xent loss issue has been merged.
- [x] Synthetic model + loss forward-backward integration test has been merged.
- [ ] Linear probe, supervised baseline, evaluation, ablation, and long runs must not start yet.

## Gate 2 Status

- [x] Minimal fake-data smoke training setup has been merged.
- [x] Smoke training config keeps checkpoints outside the repository by default.
- [x] Fake-data smoke CLI run has been recorded.
- [x] CIFAR-10 smoke preflight has been recorded.
- [x] CIFAR-10 download was explicitly approved by the Human Owner.
- [x] CIFAR-10 data is available in external F-drive research storage.
- [x] Repository safety checks passed after external data download.
- [x] Real CIFAR-10 smoke training has been run and recorded.
- [x] Linear probe scaffold has been merged.
- [x] Fake-data linear probe CLI smoke run has been recorded.
- [x] Real CIFAR-10 linear probe smoke preflight has been recorded.
- [x] Real CIFAR-10 linear probe smoke CLI run has been recorded.
- [x] The CIFAR-10 linear probe smoke train accuracy is documented as not being real model performance.
- [x] Supervised baseline scaffold and fake-data smoke test have been added.
- [ ] Real supervised baseline training, evaluation report, ablation, and long runs have not been started.
