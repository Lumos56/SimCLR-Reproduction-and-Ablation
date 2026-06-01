# Agent Workflow Log

## Overview

This file records how agents are used in this project.

## Agent Roles

| Agent | Role | Main Tasks |
|---|---|---|
| Human Owner | Final Owner | direction, environment, experiments, merge decision |
| ChatGPT Pro | PM / Research Lead / Reviewer | planning, explanation, code review, experiment analysis |
| Codex | Implementation Owner | code, tests, small scoped PRs |
| Claude Code | Docs / QA / Ops | logs, docs, consistency checks |

## Timeline

### 2026-05-22

#### Task

- Issue #1: Initialize repository structure and AGENTS.md

#### Agent Used

- Codex

#### Prompt Summary

- Initialize the Day 1 / Sprint 0 repository skeleton without implementation, installation, training, or fabricated results.

#### Output

- Repository skeleton, setup documentation, environment template, GitHub templates, and placeholder logs.
- Required README sections, `.gitignore` entries, placeholder `environment.yml`, and directory skeleton were created.
- No dataset, model, loss, training, evaluation, visualization, package installation, or experiment result was added.

#### Human Review

- Task 02 was approved on 2026-05-26, which implicitly accepted the setup direction and moved the project to the updated reporting standard.

#### What Was Correct

- The repository root was confirmed as `/home/yeyee/projects/SimCLR-Reproduction-and-Ablation`.
- No large files were reported by the size check.
- `results/tables`, `results/figures`, and `results/logs` remained trackable through `.gitkeep`.

#### What Was Wrong

- The WSL environment had `python3` available but no `python` command alias.
- `tree` was not installed, so the optional tree command was not available.
- The repository had no baseline commit, so all setup files remained untracked.

#### Follow-up

- Run Gate 0 environment verification when the Human Owner is ready.
- Add storage policy documentation and the future project decision memo.

### 2026-05-22

#### Task

- Task 02: Update `AGENTS.md` with mandatory task completion reporting.

#### Agent Used

- Codex

#### Prompt Summary

- Replace repository `AGENTS.md` with `AGENTS_v3_clean.md` and verify that task completion and blocked report rules are present.

#### Output

- `AGENTS.md` was replaced with the v3 clean version.
- Verified `Codex Task Completion Reporting`, `Task Completion Report`, and `Blocked Report` sections.
- Confirmed the replacement matched the downloaded source by SHA256.

#### Human Review

- Approved on 2026-05-26.

#### What Was Correct

- The new report standard made Codex task handoff requirements explicit.
- The task stayed limited to `AGENTS.md`.

#### What Was Wrong

- The repository still had no baseline commit, so `git diff --stat` did not show untracked setup files.

#### Follow-up

- Finalize setup docs and storage policy in Task 03.

### 2026-05-26

#### Task

- Task 03: Finalize setup docs and storage policy.

#### Agent Used

- Codex

#### Prompt Summary

- Add data storage documentation, allow `data/README.md` through `.gitignore`, add a future project decision memo, add storage path checks to the environment template, and append Task 01 / Task 02 summaries.

#### Output

- Added `data/README.md` to document external dataset, checkpoint, and export paths.
- Updated `.gitignore` so real files under `data/` remain ignored while `data/README.md` is trackable.
- Added `notes/avi_review/future_project_decision_memo.md`.
- Added storage path checks to `experiments/exp00_environment_check.md`.
- Completed Task 01 / Task 02 summaries in this workflow log.

#### Human Review

- Approved on 2026-05-26.

#### What Was Correct

- The task stayed documentation-only and did not add implementation code.
- Storage policy now points future data and checkpoint work outside the repository.
- `data/README.md` is visible to Git, while example real data files remain ignored.

#### What Was Wrong

- The repository still had no baseline commit, so `git diff --stat` remained empty for untracked setup files.

#### Follow-up

- Add `PROJECT_STATUS.md` and prepare initial commit readiness in Task 04.

### 2026-05-26

#### Task

- Task 06: Record Gate 0 environment check results.

#### Agent Used

- Codex

#### Prompt Summary

- Record Human Owner-verified storage and environment check results without installing packages, downloading data, or implementing dataset/model/loss/training/evaluation/visualization code.

#### Output

- Recorded Gate 0 PASS results in `experiments/exp00_environment_check.md`.
- Updated `PROJECT_STATUS.md` to show Gate 0 checks passed and next gate is Gate 1 module setup.
- Recorded verified storage mapping: `~/research` resolves to `/mnt/f/Research`, `/mnt/f` is the F drive, and available space is about 1.9T.
- Recorded verified environment: `simclr`, Python 3.10.20, torch 2.11.0+cu128, CUDA available, RTX 5080, torchvision 0.26.0+cu128, pytest 9.0.3, PyYAML import ok, and nvidia-smi works.

#### Human Review

-

#### What Was Correct

- Gate 0 evidence is recorded as Human Owner-verified output.
- The task stayed documentation-only.

#### What Was Wrong

-

#### Follow-up

- Review and commit the Gate 0 record before starting Gate 1 module setup.

### 2026-05-26

#### Task

- Gate 0 merge summary.

#### Agent Used

- Human Owner / Codex record update

#### Prompt Summary

- Gate 0 storage and environment record was merged into `main`; update project status for Gate 1 preparation.

#### Output

- Gate 0 environment check is now merged to `main`.
- Project status moved to Gate 1 / Module Setup.
- Next owner decision is to approve the first Gate 1 task, starting with dataset and augmentation.

#### Human Review

- Gate 0 merge completed by Human Owner.

#### Follow-up

- Prepare and review the dataset + augmentation issue before implementation begins.

### 2026-05-27

#### Task

- Task 07: Add task registry and decision log.

#### Agent Used

- Codex

#### Prompt Summary

- Add lightweight workflow tracking files before Gate 1 implementation and update project status.

#### Output

- Added `notes/task_registry.md` as a concise index of completed setup and Gate 0 tasks.
- Added `notes/decision_log.md` with key project decisions made so far.
- Updated `PROJECT_STATUS.md` current task to Task 07.

#### Human Review

-

#### What Was Correct

- The task stayed documentation-only.
- No dataset, model, loss, training, evaluation, ablation, package installation, or data download was started.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 07 tracking files, then approve the first Gate 1 dataset + augmentation task.

### 2026-05-27

#### Task

- Task 08: Implement CIFAR-10 dataset utilities and TwoCropTransform.

#### Agent Used

- Codex

#### Prompt Summary

- Implement CIFAR-10 transform builders, two-crop contrastive augmentation, dataset builder utilities, and lightweight tests without downloading data or starting model/loss/training work.

#### Output

- Added `src/augmentations.py` with CIFAR-10 normalization constants, strong SimCLR transform, weak transform, eval transform, and `TwoCropTransform`.
- Added `src/datasets.py` with a CIFAR-10 dataset builder that accepts external `data_root` and defaults `download=False`.
- Added `tests/test_dataset.py` using synthetic PIL images and monkeypatching, with no real CIFAR-10 dependency.
- Follow-up refined the strong transform with CIFAR-10-safe Gaussian blur and added non-contrastive train/eval dataset builder tests.
- Updated `PROJECT_STATUS.md` and `notes/task_registry.md` for Task 08.

#### Validation

- `python -m pytest -q tests/test_dataset.py`: passed, 10 tests.
- Dataset import check: passed.

#### Human Review

-

#### What Was Correct

- The tests do not require CIFAR-10 files or internet access.
- No data files, checkpoints, model weights, model code, loss code, or training code were added.

#### What Was Wrong

- The bare non-interactive WSL shell still has no `python` command unless the `simclr` environment is activated or the environment Python path is used.

#### Follow-up

- Review and commit Task 08, then continue Gate 1 with the next approved module task.

### 2026-05-28

#### Task

- Task 09: Implement CIFAR ResNet18 encoder, projection head, and SimCLR model shape tests.

#### Agent Used

- Codex

#### Prompt Summary

- Add CIFAR-adapted ResNet18 encoder, projection head, SimCLR wrapper, and lightweight synthetic shape tests without implementing loss, training, evaluation, ablation, or data download.

#### Output

- Added `src/models/encoder.py` with a torchvision ResNet18 adapted for CIFAR-10 input shape `[B, 3, 32, 32]`.
- Added `src/models/projection_head.py` with a Linear -> ReLU -> Linear projection head.
- Added `src/models/simclr.py` returning encoder features `h` and projection `z`.
- Added `tests/test_model_shapes.py` for encoder, projection head, wrapper, CIFAR conv1 settings, and maxpool replacement.
- Updated `PROJECT_STATUS.md` and `notes/task_registry.md`.

#### Validation

- `python -m pytest -q tests/test_model_shapes.py`: passed, 6 tests.
- `python -m pytest -q tests/test_dataset.py tests/test_model_shapes.py`: passed, 16 tests.

#### Human Review

-

#### What Was Correct

- The task stayed within Gate 1 model-shape scope.
- No loss, training, evaluation, checkpoint, or data download code was added.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 09 before starting NT-Xent loss or training tasks.

### 2026-05-28

#### Task

- Task 10: Implement NT-Xent contrastive loss with tests.

#### Agent Used

- Codex

#### Prompt Summary

- Add NT-Xent loss module and tests without implementing training, evaluation, linear probe, supervised baseline, data download, or checkpointing.

#### Output

- Added `src/losses/nt_xent.py` with `NTXentLoss` and `build_positive_pair_targets`.
- Added `src/losses/__init__.py`.
- Added `tests/test_nt_xent.py` covering scalar output, finite loss, backward gradients, validation errors, positive-pair targets, and a deterministic matched-vs-mismatched behavior check.
- Updated `PROJECT_STATUS.md` and `notes/task_registry.md`.

#### Validation

- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_nt_xent.py`: passed, 9 tests.
- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_dataset.py tests/test_model_shapes.py tests/test_nt_xent.py`: passed, 25 tests.

#### Human Review

-

#### What Was Correct

- The task stayed within Gate 1 loss scope.
- No training, evaluation, checkpoint, data download, or model changes were added.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 10 before starting training or evaluation tasks.

### 2026-05-28

#### Task

- Task 11: Add synthetic SimCLR forward-backward integration test.

#### Agent Used

- Codex

#### Prompt Summary

- Add a lightweight synthetic integration test for SimCLR model + NT-Xent loss before any training-loop implementation.

#### Output

- Added `tests/test_simclr_integration.py` using two synthetic `[4, 3, 32, 32]` views.
- Verified SimCLR output shapes for `h` and `z`, scalar finite NT-Xent loss, backward pass, and nonzero gradients in both encoder and projection head.
- Updated `PROJECT_STATUS.md` and `notes/task_registry.md` for Task 11.

#### Validation

- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_simclr_integration.py`: passed, 1 test.
- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_dataset.py tests/test_model_shapes.py tests/test_nt_xent.py tests/test_simclr_integration.py`: passed, 26 tests.
- No files over 10MB were found.
- No dataset files beyond `data/README.md`, checkpoints, or model weight files were found.

#### Human Review

-

#### What Was Correct

- The task stayed within the requested integration-test scope.
- No training loop, evaluation code, data download, checkpoint, or model weight file was added.

#### What Was Wrong

- One preliminary artifact-check command failed because PowerShell parsed `find` grouping syntax; it was rerun successfully through `bash -lc`.

#### Follow-up

- Review and commit Task 11 before starting Gate 2 smoke training.

### 2026-05-28

#### Task

- Task 12: Implement minimal SimCLR smoke training setup.

#### Agent Used

- Codex

#### Prompt Summary

- Add the first Gate 2 config-driven SimCLR smoke training setup using fake data for tests, without running real CIFAR-10 training or implementing evaluation/baseline/ablation work.

#### Output

- Added `src/utils.py` with YAML loading, seed, device, directory, and CSV append helpers.
- Added `src/train_simclr.py` with fake/CIFAR-10 dataset modes, a tiny SimCLR train loop, CSV loss logging, and checkpoint saving to a configured path.
- Added `configs/simclr_fake_smoke.yaml` and `configs/cifar10_simclr_smoke.yaml`; checkpoint directories point outside the repository by default.
- Added `tests/test_train_simclr_smoke.py` using fake data and pytest `tmp_path` for logs and checkpoints.
- Updated `PROJECT_STATUS.md` and `notes/task_registry.md` for Task 12.

#### Validation

- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_train_simclr_smoke.py`: passed, 1 test.
- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_dataset.py tests/test_model_shapes.py tests/test_nt_xent.py tests/test_simclr_integration.py tests/test_train_simclr_smoke.py`: passed, 27 tests.

#### Human Review

-

#### What Was Correct

- Fake-data smoke training completed without requiring CIFAR-10 files or internet access.
- Test checkpoint was written only under pytest `tmp_path`, not inside the repository.
- No linear probe, supervised baseline, evaluation, ablation, or long run was added.

#### What Was Wrong

- A read-only `rg --files` command failed because the mixed Windows/WSL PATH selected a Windows app resource without execute permission; file listing was rerun with WSL `find`.

#### Follow-up

- Review and commit Task 12 before running a real CIFAR-10 smoke test.

### 2026-05-28

#### Task

- Task 13: Record fake smoke CLI run result.

#### Agent Used

- Codex

#### Prompt Summary

- Record the Human Owner's manual fake-data smoke CLI run, including the failed direct script invocation, the fixed module-style command, the successful output, the small CSV log, and the external checkpoint path.

#### Output

- Added `experiments/exp01_fake_smoke_cli.md` with the purpose, failed command, fixed command, result, CSV log path, external checkpoint path, repository safety confirmation, and fake-data limitation.
- Included `results/logs/simclr_fake_smoke.csv` as the small repository log from the successful fake smoke run.
- Updated `notes/errors_and_fixes.md` with the `ModuleNotFoundError: No module named 'src'` symptom, cause, fix, and reusable lesson.
- Updated `PROJECT_STATUS.md` and `notes/task_registry.md` for Task 13.

#### Validation

- Read `results/logs/simclr_fake_smoke.csv`; contents matched the Human Owner-provided smoke log.
- Checked that no `.pt`, `.pth`, `.ckpt`, or `.onnx` files exist inside the repository.
- Checked that no files over 10MB exist inside the repository.

#### Human Review

-

#### What Was Correct

- The successful CLI result was recorded without rerunning training.
- The external checkpoint path was documented without moving, deleting, or copying the checkpoint.
- No code, config, dataset, model, loss, or test files were modified.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 13, then decide whether to run the real CIFAR-10 smoke test.

### 2026-05-28

#### Task

- Task 14: Record CIFAR-10 smoke preflight result.

#### Agent Used

- Codex

#### Prompt Summary

- Record the Human Owner's read-only preflight check for `configs/cifar10_simclr_smoke.yaml` without downloading CIFAR-10, running training, creating checkpoints, or modifying code/config/tests/results.

#### Output

- Added `experiments/exp02_cifar10_smoke_preflight.md` with observed config values, storage mapping, missing CIFAR-10 data, readiness assessment, and owner-approval requirement before download.
- Updated `PROJECT_STATUS.md` for Gate 2 / CIFAR-10 Smoke Preflight.
- Updated `notes/task_registry.md` to mark Task 13 as commit `29f497b` and add Task 14.
- Updated `notes/decision_log.md` to record that CIFAR-10 download requires explicit owner approval.

#### Validation

- Confirmed branch `run/cifar10-smoke-preflight`.
- Confirmed initial repository status was clean before edits.
- No training, download, checkpoint creation, code edits, config edits, test edits, or results/log edits were performed.

#### Human Review

-

#### What Was Correct

- The preflight result is recorded as not ready for real CIFAR-10 smoke because data is missing.
- The config is documented as safe because `download: false` and checkpoint path is external.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 14, then decide whether to approve CIFAR-10 download to external storage.

### 2026-05-29

#### Task

- Task 15: Record CIFAR-10 external download result.

#### Agent Used

- Codex

#### Prompt Summary

- Record the Human Owner-approved CIFAR-10 download to external F-drive research storage without downloading again, running training, creating checkpoints, moving external data, or modifying code/config/tests/results logs.

#### Output

- Added `experiments/exp03_cifar10_download.md` with owner approval, external data root, sample counts, downloaded archive, extracted files, data directory size, and repository safety checks.
- Updated `PROJECT_STATUS.md` for Gate 2 / CIFAR-10 Smoke Preparation.
- Updated `notes/task_registry.md` to mark Task 14 as commit `4b99a85` and add Task 15.
- Updated `notes/decision_log.md` to record that CIFAR-10 download was approved only to external F-drive research storage.

#### Validation

- Confirmed branch `data/download-cifar10`.
- Confirmed initial repository status was clean before edits.
- Checked that no files under repository `data/` exist except `data/README.md`.
- Checked that no `.pt`, `.pth`, `.ckpt`, or `.onnx` files exist inside the repository.
- Checked that no files over 10MB exist inside the repository.

#### Human Review

-

#### What Was Correct

- The record clearly distinguishes data availability from training results.
- No dataset files were added to the repository.
- No training, checkpoint creation, code changes, config changes, test changes, or results/log changes were performed.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 15, then approve and run the real CIFAR-10 smoke command if ready.

### 2026-05-29

#### Task

- Task 16: Record real CIFAR-10 smoke run result.

#### Agent Used

- Codex

#### Prompt Summary

- Record the Human Owner's manual real CIFAR-10 smoke CLI run without rerunning training, downloading data, creating checkpoints, modifying external checkpoint files, or changing source/config/test code.

#### Output

- Added `experiments/exp04_cifar10_smoke_cli.md` with the command, observed output, 10-step CSV log, external checkpoint path, repository safety checks, and limitations.
- Included `results/logs/cifar10_simclr_smoke.csv` as the small repository smoke log from the successful run.
- Updated `PROJECT_STATUS.md` for Gate 2 / Smoke Training.
- Updated `notes/task_registry.md` to mark Task 15 as commit `ca44337` and add Task 16.

#### Validation

- Read `results/logs/cifar10_simclr_smoke.csv`; contents matched the Human Owner-provided smoke log.
- Checked that no files under repository `data/` exist except `data/README.md`.
- Checked that no `.pt`, `.pth`, `.ckpt`, or `.onnx` files exist inside the repository.
- Checked that no files over 10MB exist inside the repository.

#### Human Review

-

#### What Was Correct

- The record clearly identifies the run as a real CIFAR-10 smoke run, not a baseline experiment.
- The checkpoint is documented as external and was not moved, deleted, copied, or modified.
- No training, fake smoke run, data download, code change, config change, test change, evaluation, baseline, ablation, or long run was performed by Codex.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 16, then choose the next engineering step before starting baseline, evaluation, ablation, or long runs.

### 2026-05-29

#### Task

- Task 17: Implement linear probe scaffold with smoke test.

#### Agent Used

- Codex

#### Prompt Summary

- Add a small linear probe scaffold and fake-data smoke test after Gate 2 smoke training, without full linear probe training, supervised baseline, evaluation reports, ablations, downloads, repository checkpoints, or real accuracy claims.

#### Output

- Added `src/train_linear_probe.py` with SimCLR checkpoint loading, frozen encoder setup, trainable CIFAR-10 linear classifier, fake/CIFAR-10 dataset modes, tiny training loop, CSV logging, and optional external/test checkpoint saving.
- Added `configs/linear_probe_fake_smoke.yaml` and `configs/cifar10_linear_probe_smoke.yaml`.
- Added `tests/test_linear_probe_smoke.py` using fake data and pytest `tmp_path` for the SimCLR checkpoint, log directory, and optional linear-probe checkpoint.
- Updated `PROJECT_STATUS.md` and `notes/task_registry.md` for Task 17.

#### Validation

- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_linear_probe_smoke.py`: passed, 1 test.
- `/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_dataset.py tests/test_model_shapes.py tests/test_nt_xent.py tests/test_simclr_integration.py tests/test_train_simclr_smoke.py tests/test_linear_probe_smoke.py`: passed, 28 tests.

#### Human Review

-

#### What Was Correct

- The linear probe test confirms the encoder is frozen, classifier parameters get gradients and update, and CSV logging works.
- Temporary checkpoints were created only under pytest `tmp_path`, not inside the repository.
- No real CIFAR-10 linear probe run, full baseline training, supervised baseline, evaluation report, ablation, or long run was performed.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 17 before deciding whether to run a real CIFAR-10 linear-probe smoke command.

### 2026-05-29

#### Task

- Task 18: Record fake linear probe CLI smoke result.

#### Agent Used

- Codex

#### Prompt Summary

- Record the Human Owner's manual fake-data linear probe CLI smoke run without rerunning training, running real CIFAR-10 linear probe, downloading data, creating checkpoints, implementing supervised baseline, evaluation report, ablation, or reporting fake train accuracy as real performance.

#### Output

- Added `experiments/exp05_fake_linear_probe_cli.md` with the command, observed output, CSV log, no-checkpoint behavior, repository safety checks, and fake-data-only limitation.
- Included `results/logs/linear_probe_fake_smoke.csv` as the small repository smoke log from the successful run.
- Updated `PROJECT_STATUS.md` for Gate 3 / Linear Probe Smoke.
- Updated `notes/task_registry.md` to mark Task 17 as commit `525d1b5` and add Task 18.

#### Validation

- Read `results/logs/linear_probe_fake_smoke.csv`; contents matched the Human Owner-provided smoke log.
- Checked that no files under repository `data/` exist except `data/README.md`.
- Checked that no `.pt`, `.pth`, `.ckpt`, or `.onnx` files exist inside the repository.
- Checked that no files over 10MB exist inside the repository.

#### Human Review

-

#### What Was Correct

- The record clearly states that `final_train_acc=0.25` is fake-data smoke validation only and not real model performance.
- The run's no-checkpoint behavior is documented as expected because `save_checkpoint: false`.
- No training, real CIFAR-10 linear probe, download, checkpoint creation, code change, config change, test change, supervised baseline, evaluation report, ablation, or long run was performed by Codex.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 18, then decide whether to run the real CIFAR-10 linear probe smoke command.

### 2026-06-01

#### Task

- Task 19: Record real CIFAR-10 linear probe smoke preflight.

#### Agent Used

- Codex

#### Prompt Summary

- Record the Human Owner's read-only preflight check for `configs/cifar10_linear_probe_smoke.yaml` without running real or fake linear probe, downloading data, creating checkpoints, implementing supervised baseline, evaluation report, ablation, or reporting accuracy.

#### Output

- Added `experiments/exp06_cifar10_linear_probe_preflight.md` with checked config values, external SimCLR checkpoint availability, external CIFAR-10 data availability, `download=false`, `save_checkpoint=false`, and the owner-approval requirement before running the real smoke command.
- Updated `PROJECT_STATUS.md` for Gate 3 / Linear Probe Smoke Preflight.
- Updated `notes/task_registry.md` to mark Task 18 as commit `0878a6a` and add Task 19.

#### Validation

- Confirmed branch `run/cifar10-linear-probe-preflight`.
- Confirmed initial repository status was clean before edits.
- Checked final diff scope remained within the allowed files.
- No training, download, checkpoint creation, code edit, config edit, test edit, results/log edit, supervised baseline, evaluation report, ablation, or accuracy reporting was performed.

#### Human Review

-

#### What Was Correct

- The preflight record states that the config is safe for a real CIFAR-10 linear probe smoke run but that the run still requires owner approval.
- The record notes that `save_checkpoint=false`, so no linear probe weights should be created by the smoke run.

#### What Was Wrong

-

#### Follow-up

- Review and commit Task 19, then approve the real CIFAR-10 linear probe smoke command if ready.
