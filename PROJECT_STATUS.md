# Project Status

| 字段 | 当前内容 |
|---|---|
| Current Stage | Gate 2 / CIFAR-10 Smoke Preflight |
| Current Task | Task 14 CIFAR-10 smoke preflight recorded |
| Last Completed Task | Task 13 fake smoke CLI result merged to main |
| Git State | working on branch `run/cifar10-smoke-preflight` |
| Branch | `run/cifar10-smoke-preflight` |
| Next Gate | Owner decision on CIFAR-10 download |
| Do Not Start Yet | real CIFAR-10 training, linear probe, supervised baseline, evaluation, ablation, long runs |
| Blockers | none for Gate 0 |
| Next Owner Decision | decide whether to approve CIFAR-10 download to external storage |

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
- [ ] CIFAR-10 data was not found during preflight.
- [ ] CIFAR-10 download requires explicit owner approval.
- [ ] Real CIFAR-10 smoke training has not been run.
