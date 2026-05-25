# AGENTS.md

Version: v3 clean, with mandatory Codex task completion reporting.

## Purpose

This file defines how AI agents and the human owner work inside this repository.

Repository:

```text
/home/yeyee/projects/SimCLR-Reproduction-and-Ablation
```

Project goal:

Build a small, reproducible PyTorch SimCLR project on CIFAR-10 as a contrastive learning foundation project toward audio-visual intelligence.

This project is not intended to reach state-of-the-art accuracy. It is intended to train research engineering workflow: implementation, validation, baseline, ablation, documentation, and honest analysis.

---

## Source of Truth

Use the following priority order when instructions conflict:

1. The human owner’s latest explicit instruction.
2. This `AGENTS.md`.
3. The current GitHub Issue or task file.
4. `SimCLR_AVI短期项目规划_Agent协作版.md`.
5. Existing repository code, tests, configs, and experiment logs.
6. Older planning documents.

Do not use older plans to expand scope if the latest plan has narrowed it.

---

## Current Project Scope

Required components:

- CIFAR-10 data loading.
- Two-crop augmentation.
- ResNet18 encoder adapted for CIFAR-10.
- Projection head.
- NT-Xent loss.
- SimCLR smoke pretraining.
- SimCLR baseline pretraining.
- Linear probe.
- Supervised ResNet18 baseline.
- Three required ablations:
  - no projection head;
  - strong vs weak augmentation;
  - batch size comparison.
- Loss curve.
- Baseline and ablation result tables.
- At least one embedding visualization.
- English `README.md`.
- Chinese `report/final_report.md`.
- `notes/agent_workflow_log.md`.
- `notes/errors_and_fixes.md`.
- `notes/avi_review/glossary_avi_terms.md`.
- `notes/avi_review/future_project_decision_memo.md`.

Out of scope for the short-term project:

- ImageNet.
- Large-scale original-paper reproduction.
- Full STL-10 experiment.
- CIFAR-100.
- Audio training implementation.
- Video data processing.
- AV-HuBERT or ImageBind reproduction.
- Gradio or complex web demos.
- Complex CI at project start.
- Tuning only to make accuracy look better.

---

## Storage and Large File Policy

The repository is for source code, configs, tests, scripts, documentation, experiment notes, small result tables, and selected lightweight figures.

Large files must not be stored inside the repository or WSL project directory.

External storage locations:

```text
Raw datasets:
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation

Models and checkpoints:
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation

Large exports:
/home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation
```

Before downloading datasets or saving checkpoints, the owner must verify that `/home/yeyee/research` is mapped to the intended F-drive research area.

Agents must not:

- download datasets into the repository;
- save checkpoints inside the repository;
- commit `.pt`, `.pth`, `.ckpt`, `.onnx`, dataset files, TensorBoard event files, W&B runs, or large generated artifacts;
- move, delete, copy, or rewrite original files in `F:\research` unless explicitly instructed by the owner.

Agents may:

- create or update `data/README.md` to document external paths;
- add config fields such as `data_root`, `checkpoint_dir`, `export_dir`, and `log_dir`;
- write code that reads datasets from external storage;
- write code that saves checkpoints to external model directories.

Default config path policy:

```yaml
paths:
  data_root: /home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation
  checkpoint_dir: /home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation/checkpoints
  export_dir: /home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation
  log_dir: results/logs
```

Small CSV logs and Markdown experiment notes may stay in the repository. Large logs and generated artifacts must go to external storage.

---

## Global Rules for All Agents

All agents must:

- work on one Issue or task file at a time;
- keep changes limited to the requested scope;
- read this `AGENTS.md` before making changes;
- avoid unrelated refactors;
- add or update tests for core logic when appropriate;
- record commands that were actually run;
- clearly state anything that was not validated;
- never fabricate experiment results;
- never delete failure records;
- never commit large files;
- never merge to `main`;
- never treat agent output as experimental evidence.

If instructions are unclear, stop and ask for clarification.

---

## Human Owner

Role:

Final Owner, Research PI, and final decision maker.

Responsibilities:

- choose the daily main task;
- approve repository location and storage policy;
- create or approve conda environments;
- run environment checks;
- run smoke tests and long training jobs on the local GPU;
- verify actual experimental results;
- decide whether to merge;
- confirm that core code and tensor shapes are understandable;
- maintain honest project direction.

The owner must not outsource final understanding or final result validation to agents.

---

## Codex

Role:

Implementation Owner / Senior ML Engineer.

Before working, Codex must read:

- `AGENTS.md`;
- the current Issue or task file;
- `README.md`;
- files directly related to the task.

Task-specific reading:

- setup task: `.gitignore`, `README.md`, `AGENTS.md`;
- data task: `src/datasets.py`, `src/augmentations.py`, `tests/test_dataset.py`;
- model task: `src/models/`, `tests/test_model_shapes.py`;
- loss task: `src/losses/nt_xent.py`, `tests/test_nt_xent.py`;
- training task: `configs/`, `src/train_simclr.py`, `src/utils.py`;
- evaluation task: `src/train_linear_probe.py`, `src/train_supervised.py`, `src/evaluate.py`;
- documentation task: `README.md`, `report/final_report.md`, `notes/`.

Codex may:

- implement small, scoped code changes;
- add or update lightweight tests;
- add config files for approved experiments;
- add documentation placeholders;
- run lightweight validation commands;
- propose the next Issue.

Codex must:

- produce a Task Completion Report at the end of every Issue, PR-style delivery, or task file;
- produce a Blocked Report if the task cannot be completed, cannot be validated, or requires an owner decision;
- include the report in its final response to the owner;
- append the same information to `notes/agent_workflow_log.md` when that file exists and updating it is within the task scope;
- include `git status --short` and `git diff --stat` when Git is available;
- stop after the assigned task and wait for owner review before starting a new Issue.

Codex must not:

- implement the whole project in one task;
- run long training jobs;
- install or upgrade NVIDIA drivers, CUDA toolkit, conda base, shell startup files, or system packages;
- download datasets unless explicitly instructed by the owner;
- create checkpoints in the repository;
- fabricate results;
- modify unrelated files;
- merge to `main`;
- edit files outside the repository unless explicitly instructed.

---


## Codex Task Completion Reporting

Codex must not finish a task with only `done`, `completed`, or a short informal sentence. Every Codex task must end with a clear report.

Reporting granularity:

- one report per Issue;
- one report per task file;
- one report per PR-style delivery;
- one Blocked Report if the task cannot be completed or validated.

Unnecessary reporting granularity:

- no separate report for every `ls` command;
- no separate report for every individual file save;
- no long narrative for trivial inspection commands.

Required Task Completion Report fields:

- Status: completed, partially completed, or blocked;
- Task or Issue;
- Branch or working directory;
- Agent name;
- Date;
- Summary of what changed;
- Files changed and why each file changed;
- Commands actually run;
- Validation results;
- Items not validated;
- `git status --short`;
- `git diff --stat`;
- Risks or known issues;
- Recommended next step;
- Owner decision needed, if any.

Rules for the report:

- Commands must be listed only if they were actually executed.
- Validation must not claim success without command output or a clear check.
- Unvalidated items must be explicitly listed.
- If no files changed, Codex must say so clearly.
- If only documentation changed, Codex must say that no code validation was required.
- If Git commands are unavailable, Codex must say that Git status and diff were not validated.

Required Blocked Report fields:

- Status: blocked;
- Task or Issue;
- Branch or working directory;
- Agent name;
- Date;
- What was attempted;
- Where it got blocked;
- Error messages or missing information;
- Files changed before blocking;
- Whether rollback is needed;
- Exact question or owner decision needed.

A task is not considered complete until Codex has produced the required report. Codex must not continue to the next Issue until the owner reviews the report and gives the next instruction.

For small tasks, such as replacing `AGENTS.md` or updating one template, Codex may skip editing `notes/agent_workflow_log.md` if the task file says so. The final Task Completion Report is still mandatory.

---

## ChatGPT Pro

Role:

Research Lead, PM, Reviewer, and AVI concept tutor.

ChatGPT Pro may:

- translate project goals into Issues;
- design acceptance criteria;
- explain SimCLR, NT-Xent, linear probe, baseline, and ablation;
- review Codex diffs and Work Logs;
- check tensor shapes and research validity;
- analyze real experiment outputs;
- help write README and final report sections;
- help build AVI glossary and future-project decision memos.

ChatGPT Pro must not:

- fabricate experiment results;
- claim unvalidated code is correct;
- replace the owner’s final merge decision;
- ignore experiment logs;
- expand scope beyond the latest short-term plan;
- use unverified sources as factual evidence.

Review focus:

- Issue scope.
- Unrelated file changes.
- Tensor shapes.
- NT-Xent positive-pair logic.
- Masking and temperature logic.
- Data leakage.
- Reproducibility.
- Tests.
- Documentation consistency.
- Whether the PR is safe to merge.

---

## Claude Code

Role:

Docs, QA, and Research Ops.

Claude Code may:

- organize `notes/agent_workflow_log.md`;
- organize `notes/errors_and_fixes.md`;
- draft learning logs;
- check README clarity;
- check document consistency;
- check whether large files were accidentally added;
- prepare QA checklists;
- summarize Work Logs.

Claude Code must not:

- replace Codex for core implementation;
- rewrite the whole repository without scope;
- delete failure records;
- modify experimental result values;
- claim commands were run if they were not run;
- merge to `main`.

---

## Issue, Branch, PR, and Work Log

Recommended branch names:

- `setup/init-repo`
- `env/gate-0-check`
- `data/two-crop-augmentation`
- `model/resnet18-projection-head`
- `loss/nt-xent`
- `train/simclr-smoke-test`
- `eval/linear-probe`
- `baseline/supervised-resnet18`
- `exp/no-projection-head`
- `exp/augmentation-ablation`
- `exp/batch-size-ablation`
- `docs/final-readme`

Recommended PR titles:

- `feat(data): add CIFAR-10 two-crop augmentation`
- `feat(model): add CIFAR ResNet18 encoder and projection head`
- `feat(loss): implement NT-Xent loss`
- `feat(train): add SimCLR smoke training loop`
- `docs(report): add final experiment summary`

Every implementation task must end with a Task Completion Report. Major tasks must also create or provide an Agent Work Log entry.

Required Work Log fields:

- Task:
- Issue:
- Branch:
- Agent:
- Date:
- Summary:
- Files Changed:
- Commands Run:
- Validation:
- Not Validated:
- Git Status:
- Git Diff Stat:
- Known Issues:
- Next Step:

Commands must be listed as commands actually run. Do not list planned commands as completed validation.

---

## Validation Gates

Gate 0: Environment

Required evidence:

- Python runs.
- Conda environment is identified.
- PyTorch imports.
- CUDA availability is recorded.
- GPU name is recorded.
- `torchvision` imports.
- `pytest` imports.
- CIFAR-10 data location is planned.
- Storage path mapping is checked.

Expected output:

- `experiments/exp00_environment_check.md`

Gate 1: Module checks

Required evidence:

- dataset output shape is correct;
- augmentation output shape is correct;
- model forward pass works;
- loss is scalar;
- backward pass works.

Expected tests:

- `tests/test_dataset.py`
- `tests/test_model_shapes.py`
- `tests/test_nt_xent.py`

Gate 2: Smoke training

Required evidence:

- training starts;
- loss is finite;
- checkpoint is saved to external model directory;
- small log is saved;
- run is documented.

Gate 3: Baselines

Required evidence:

- SimCLR pretraining runs;
- linear probe runs;
- supervised baseline runs;
- baseline table exists;
- commands, configs, seeds, and results are recorded.

Gate 4: Ablations

Required evidence:

- no projection head experiment;
- strong vs weak augmentation experiment;
- batch size experiment;
- each experiment has config, command, result, and interpretation.

Gate 5: Presentation

Required outputs:

- final `README.md`;
- `report/final_report.md`;
- `notes/agent_workflow_log.md`;
- `notes/errors_and_fixes.md`;
- `notes/avi_review/future_project_decision_memo.md`.

---

## Lightweight Validation Commands

Basic import check:

```bash
python -c "import sys; print(sys.version)"
python -c "import torch; print(torch.__version__)"
python -c "import torchvision; print(torchvision.__version__)"
python -m pytest -q
```

Environment and CUDA check:

```bash
python - <<'PY'
import torch
print("torch:", torch.__version__)
print("torch.version.cuda:", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("device:", torch.cuda.get_device_name(0))
PY
```

Storage check:

```bash
pwd
df -h .
ls -ld ~/research || true
readlink -f ~/research || true
df -h ~/research || true
```

Agents must only report commands as passed if they actually ran and passed.

---

## Experiment Record Policy

Every experiment file in `experiments/` should include:

- hypothesis;
- fixed conditions;
- changed variable;
- config path;
- commands actually run;
- seed;
- dataset path;
- checkpoint path;
- metrics;
- observations;
- interpretation;
- failure or limitation;
- next step.

Do not remove failed experiments. Failed experiments are part of the research record.

---

## README and Report Honesty Policy

README and report must not:

- claim state-of-the-art performance;
- hide failed runs;
- report results without commands and configs;
- imply Audio-SimCLR or audio-visual synchronization was implemented if it was only discussed;
- overstate what small CIFAR-10 results prove.

README and report should state:

- this is a small-scale research engineering project;
- results are constrained by dataset, compute, training length, and implementation choices;
- SimCLR is used as a foundation for later audio and audio-visual projects.

---

## Knowledge Base Boundary

The Obsidian KnowledgeVault and `F:\research` are external knowledge and source-material areas.

Agents working inside this repository must not:

- modify the Obsidian vault directly;
- move or delete source files in `F:\research`;
- copy original large source materials into the repository.

Agents may create project notes inside this repository that later help the owner update Obsidian manually.

---

## Daily Operating Rule

Daily workflow:

1. The owner chooses one main task.
2. ChatGPT Pro turns it into an Issue or task file.
3. Codex completes only that task.
4. The owner runs or verifies lightweight checks.
5. ChatGPT Pro reviews code, logic, and research validity.
6. The owner decides merge, revise, or hold.
7. Claude Code organizes logs and documentation.
8. The owner writes a short learning note.

Daily limit:

- one main Codex task;
- at most two Codex Issues if both are small;
- no long training unless explicitly planned by the owner.
