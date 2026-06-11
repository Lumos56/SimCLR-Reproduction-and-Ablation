# Reusable AI Research Project Workflow

Status note:

- This guide is distilled from the SimCLR-Reproduction-and-Ablation project.
- It is intended for future AI research coding projects.
- It is a practical workflow guide, not an experiment result.
- It should be adapted per project.

## Purpose

This workflow is meant to:

- make long AI-assisted research coding projects reproducible;
- reduce dependence on chat context;
- preserve Human Owner understanding and final decision authority;
- support collaboration between Human Owner, ChatGPT, Codex, and optional
  Claude Code.

## Core Principles

- Repository files are the source of truth.
- The Human Owner is the final decision maker.
- Agents work in scoped tasks.
- ChatGPT reviews and plans; Codex implements scoped tasks.
- Do not guess unseen files.
- Do not overclaim results.
- Commit, merge, and push only after review.

## Minimum File Set for a New Project

Start a new AI research coding project with at least:

- `AGENTS.md`
- `PROJECT_STATUS.md`
- `notes/task_registry.md`
- `notes/decision_log.md`
- `notes/agent_workflow_log.md`
- `notes/errors_and_fixes.md`
- `data/README.md`
- `experiments/`
- `results/tables/`
- `results/figures/`
- `README.md`

These files make task scope, status, decisions, failures, storage policy,
experiment evidence, and presentation state recoverable across conversations.

## New Project Day 0 / Day 1 Checklist

1. Choose the official repository path.
2. Create external dataset, checkpoint, and export storage.
3. Initialize Git.
4. Write `AGENTS.md`.
5. Write `PROJECT_STATUS.md`.
6. Create the `notes/` structure.
7. Create `data/README.md` before data download.
8. Commit the initial skeleton.
9. Do the environment gate before model code.

Day 0 / Day 1 should establish project boundaries, storage rules, and validation
gates before implementation starts.

## Task Lifecycle

1. Plan the task.
2. Create a branch.
3. Give Codex a narrow task.
4. Codex changes only allowed files.
5. Codex returns a Task Completion Report.
6. The Human Owner sends the report and relevant files to ChatGPT.
7. ChatGPT reviews actual files when needed.
8. The Human Owner commits.
9. The Human Owner merges to `main`.
10. The Human Owner pushes to GitHub.
11. The next task records the previous commit hash.

Do not start the next task until the current task is reviewed.

## Task Boundary Rules

- Do not casually renumber fixed tasks.
- Preflight belongs inside a run task unless explicitly planned otherwise.
- Status and log corrections do not automatically become new task numbers.
- Use one branch per scoped task.
- Do not start the next task before the current task is reviewed.
- Run tasks are owner-run and Codex-recorded.

## Run Task Template

Use this shape for owner-run training, evaluation, or artifact-generation tasks:

1. Internal preflight: verify config, data path, checkpoint path, output path,
   branch, and forbidden files.
2. Owner command: the Human Owner runs the approved command.
3. Concise log inspection: inspect logs with `wc`, `head`, and `tail` for large
   files.
4. Artifact safety check: verify checkpoints and large exports are outside the
   repository.
5. Codex result recording: record command, config, seed, paths, metrics,
   failures, and limitations.
6. Review: ChatGPT or the Human Owner reviews scope, evidence, and claims.
7. Commit, merge, and push: only after review.

## Codex Task Prompt Template

```text
Task:
Branch:

Context:

Read before working:
- AGENTS.md
- PROJECT_STATUS.md
- notes/task_registry.md
- notes/decision_log.md
- files directly related to this task

Allowed files:
- ...

Forbidden files:
- ...

Do not:
- run training unless explicitly requested
- run evaluation unless explicitly requested
- run tests unless explicitly requested
- edit code/config/result files outside scope
- create checkpoints in the repository
- fabricate metrics
- start the next task

Requirements:
- ...

Validation commands:
- ...

Acceptance criteria:
- ...

Completion report requirements:
- status
- task
- branch or working directory
- summary
- files changed and why
- commands actually run
- validation results
- not validated
- git status --short
- git diff --stat
- risks / known issues
- recommended next step
```

## Task Completion Report Template

```text
Status:
Task:
Branch or working directory:
Agent:
Date:

Summary of what changed:

Files changed and why:

Commands actually run:

Validation results:

Items not validated:

git status --short:

git diff --stat:

Risks / known issues:

Recommended next step:

Owner decision needed:
```

## Review Rules

- A Codex report is not enough for high-risk code changes.
- Upload or point to actual files for code-level review.
- When file uploads expire, ask for re-upload.
- When same-name files are re-uploaded, use the newest uploaded content.
- Do not guess unseen file content.
- Compare report claims against actual files when risk is high.

High-risk review includes tensor shapes, loss logic, data leakage, checkpoint
loading, evaluation logic, metric calculation, and result interpretation.

## Result Interpretation Rules

- Smoke metrics are not performance.
- Training-batch accuracy is not test accuracy.
- Final loss is not representation quality.
- A short baseline is preliminary.
- Ablation results are preliminary unless repeated and scaled.
- README and report files must avoid final benchmark claims unless evidence
  supports them.

Every real result should have a command, config, seed, dataset path, checkpoint
path, metric source, limitations, and not-validated items.

## Storage and Artifact Policy

- Datasets stay external.
- Checkpoints stay external.
- Exports stay external.
- Small logs, tables, figures, and docs may be committed.
- Do not commit `.pt`, `.pth`, `.ckpt`, or `.onnx` files.
- Do not commit large files.
- Always run repository safety checks after training or evaluation.

Recommended repository safety checks:

```bash
git status --short
find . -type f \( -name "*.pt" -o -name "*.pth" -o -name "*.ckpt" -o -name "*.onnx" \) -print
find . -type f -size +10M -print
```

## Log Display Rule

- Smoke logs may be printed with `cat` if tiny.
- Baseline, short-run, and long-run logs must use `wc`, `head`, and `tail`.
- Do not print thousands of CSV lines.

Use plotting or analysis scripts for deeper inspection after preserving raw logs.

## Git and GitHub Workflow

- `main` stays clean.
- Use one task branch.
- Prefer fast-forward merge when possible.
- Push `main` after merge.
- Use the GitHub remote for publication.
- GitHub rendered UI checks are separate presentation tasks.
- Do not force push unless explicitly approved.

Commit hashes are easiest to fill into the task registry during the next task
after review and merge.

## When to Use Extra Tools

- Use plotting only after CSV or result tables exist.
- Use GitHub tools only after the local workflow is stable.
- Use browser or computer-use tools only for safe UI and read-only checks.
- Do not use UI tools for destructive actions.

Extra tools should serve the current task; they should not expand scope.

## Cross-Conversation Restart Package

For continuing the same project in a new ChatGPT or Codex conversation, upload
or point to:

- `PROJECT_STATUS.md`
- `notes/task_registry.md`
- `notes/decision_log.md`
- `notes/workflow_playbook_draft.md` or this reusable workflow guide
- latest relevant experiment record
- latest result table if the task concerns results
- current target task description
- code/config files when code-level review is needed

If a file is not visible in the new conversation, the assistant should ask for
it rather than infer its contents.

## Agent Roles

- Human Owner: final decision maker, research PI, merge authority, and final
  validator of understanding and results.
- ChatGPT: research lead, planner, reviewer, tutor, and interpretation checker.
- Codex: scoped implementation or documentation agent that changes only allowed
  files and reports exact commands, validation, and gaps.
- Optional Claude Code: docs, QA, checklist, and log-organization support.

No agent replaces the Human Owner's final understanding, merge decision, or
responsibility for real experimental claims.

## Common Failure Modes and Fixes

| Failure mode | Practical fix |
|---|---|
| Stale status files | Update `PROJECT_STATUS.md`, task registry, and workflow log in the same scoped task. |
| Wrong branch | Stop, report branch state, and switch or recreate only after owner-approved scope is clear. |
| Codex report vs file mismatch | Compare report claims against actual files and diffs before review or merge. |
| Old uploaded file vs newest upload confusion | Use the newest uploaded file and ask for re-upload when uncertain. |
| Long CSV printed with `cat` | Use `wc`, `head`, and `tail`; record the log-display rule in errors or workflow notes. |
| Checkpoint accidentally in repo | Stop, remove from Git tracking if needed, move only with owner approval, and rerun safety checks. |
| Task numbering drift | Keep fixed task numbers stable and record corrections in status files rather than chat only. |
| Metrics overclaimed | Rewrite README/report language to state metric source, scope, limitations, and uncertainty. |

## What Remains Project-Specific

- Dataset paths.
- Model-specific configs.
- Experiment metrics.
- Domain-specific result interpretation.
- Paper-specific or project-specific claims.

The workflow structure can transfer, but scientific content and evidence must be
rewritten for each project.

## Current Limitations of This Workflow

- It is still manual.
- The task registry can drift.
- The agent workflow log can become long.
- The final workflow should still be adapted for each project.
- GitHub PR and issue workflow is not fully mature yet.

This guide reduces context loss, but it does not remove the need for review.

## Recommended Future Improvements

- Add a project-start checklist file.
- Add a task prompt template file.
- Add a task completion report template file.
- Add an optional GitHub issue/PR workflow.
- Add a possible lightweight script for status consistency checks.

## Verdict

This workflow is good enough to reuse as a starting template.

It is not a universal recipe.

It should be adapted and improved after each future project.
