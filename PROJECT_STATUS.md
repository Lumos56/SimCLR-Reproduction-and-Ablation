# Project Status

| 字段 | 当前内容 |
|---|---|
| Current Stage | Workflow Documentation |
| Current Task | Task 26 workflow playbook draft |
| Last Completed Task | Task 25 baseline training plan merged to main |
| Git State | working on branch `docs/workflow-playbook-draft` |
| Branch | `docs/workflow-playbook-draft` |
| Next Gate | short baseline config preparation |
| Do Not Start Yet | short baseline training, ablation, final report |
| Blockers | none for Task 26 |
| Next Owner Decision | review Task 26 and approve Task 27 short-baseline config preparation |

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
- [x] Gate 1 module readiness checks have been completed; later evaluation, ablation, and long runs remain gated by approved task scope.

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
- [x] Fake-data supervised CLI smoke run has been recorded.
- [x] Real CIFAR-10 supervised smoke preflight has been recorded.
- [x] Real CIFAR-10 supervised smoke CLI run has been recorded.
- [x] The CIFAR-10 supervised smoke train accuracy is documented as not being real supervised baseline performance.

## Planning / Workflow Documentation Status

- [x] Short baseline training plan decision has been drafted.
- [x] Reusable workflow playbook draft has been created.
- [ ] Short baseline configs have not been prepared yet.
- [ ] Formal baseline training, evaluation report, ablation, and long runs have not been started.
