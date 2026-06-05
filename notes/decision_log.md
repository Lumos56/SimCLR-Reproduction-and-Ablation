# Decision Log

This file records project workflow decisions.

| Date | Decision | Rationale | Status |
|---|---|---|---|
| 2026-05-22 | Use WSL repository location `/home/yeyee/projects/SimCLR-Reproduction-and-Ablation`. | Keep project files in the Linux filesystem and avoid the Windows empty repo path. | Active |
| 2026-05-22 | Do not use `C:\Users\ye\Documents\SimCLR` as the official project root. | Avoid split-brain project state between Windows and WSL. | Active |
| 2026-05-26 | Store large external artifacts under `/home/yeyee/research`, mapped to `/mnt/f/Research`. | Keep datasets, checkpoints, and large exports outside the Git repository while using F-drive capacity. | Active |
| 2026-05-26 | Use a separate Conda environment named `simclr`. | Isolate project dependencies from base/system environments. | Active |
| 2026-05-22 | Require Codex Task Completion Reports and Blocked Reports. | Make every task reviewable with files changed, commands run, validation, risks, and next steps. | Active |
| 2026-05-26 | Add `PROJECT_STATUS.md`. | Provide a quick, reusable status table for stage, task, branch, blockers, and next decision. | Active |
| 2026-05-26 | Complete Gate 0 before implementation. | Verify storage, Python, PyTorch, CUDA, GPU, torchvision, pytest, and PyYAML before writing dataset/model/loss/training code. | Completed |
| 2026-05-26 | Use branch/report/review/commit workflow. | Keep each task scoped, reviewable, and traceable before moving to the next gate. | Active |
| 2026-05-28 | Require explicit owner approval before downloading CIFAR-10. | The CIFAR-10 smoke config is safe with `download: false`, but the dataset was missing during preflight; any download must be an owner-approved action to the external dataset directory. | Active |
| 2026-05-29 | CIFAR-10 download approved only to external F-drive research storage. | The Human Owner explicitly approved the CIFAR-10 download and ran it manually with `torchvision.datasets.CIFAR10`; dataset files remain outside the repository under `/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation`. | Completed |
| 2026-06-03 | Use a short baseline stage before longer baseline or ablation. | Smoke runs are not baseline results; a short supervised, SimCLR, and linear-probe baseline stage provides preliminary controlled-run evidence before longer training or ablation. | Active |
| 2026-06-03 | Treat short baseline as preliminary and not final performance. | README and final report must distinguish short baseline outputs from final performance claims and preserve limitations, configs, commands, and failure records. | Active |
| 2026-06-03 | Create a reusable workflow playbook before short-baseline configs. | The SimCLR project has enough smoke-stage workflow evidence to capture a lightweight draft for future AI research coding projects before moving into baseline training. | Active |
| 2026-06-03 | Implement evaluation scaffold before ablation. | The project has short-baseline training logs and checkpoints, but no CIFAR-10 test-set metrics; supervised and linear-probe checkpoints need comparable Top-1 evaluation before ablation. | Active |
| 2026-06-04 | Treat the short-baseline result table as a preliminary controlled comparison, not final benchmark performance. | Task 35 compares supervised short and SimCLR short plus linear-probe test-set results, but the SimCLR pretrain is only 10 epochs, the linear probe is only 5 epochs, and no ablation or tuning has been done. | Active |
| 2026-06-04 | Publish the project to GitHub after README v0.2 and short-baseline figures were ready. | The first GitHub push happened after the short-baseline comparison, visualization figures, and README v0.2 were merged to `main`, giving the remote repository a coherent first public project state. | Active |
| 2026-06-04 | Start ablation planning with the no-projection-head ablation. | No projection head directly tests a core SimCLR design choice, requires explicit model/config support, and should be compared first against the current short SimCLR plus linear-probe reference before augmentation or batch-size ablations. | Active |
| 2026-06-05 | Treat the no-projection ablation result as preliminary and lower than the short SimCLR baseline by 2.69 percentage points. | Task 44 compares existing CIFAR-10 test-set result CSVs only: baseline SimCLR short plus linear probe is 0.621400, no-projection SimCLR short plus linear probe is 0.594500, and the result is short, single-seed, and not tuned. | Active |
| 2026-06-05 | Audit workflow reproducibility after the first ablation. | The project has now passed setup, implementation, smoke, short baseline, GitHub first push, and one ablation cycle, so the workflow should be checked for restartability across long conversations and future projects before starting the next ablation. | Active |

## Guardrails Carried Into Gate 1

- Do not download data into the repository.
- Do not commit checkpoints, weights, TensorBoard event files, W&B runs, or large artifacts.
- Do not start model, loss, training, evaluation, ablation, or long runs before the approved Gate 1 task scope.
- Record commands actually run; do not report planned commands as completed validation.
