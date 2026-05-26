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
