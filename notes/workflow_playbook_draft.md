# Workflow Playbook Draft

Historical note: Task 63 finalized the reusable workflow into
`notes/reusable_ai_research_project_workflow.md`. This draft remains as
historical development material.

Date: 2026-06-03

## Purpose

This is a reusable workflow draft, not a project result.

Its purpose is to make the SimCLR collaboration process reusable in future AI research coding projects while preserving the roles of the Human Owner, ChatGPT, Codex, and optional Claude Code. This draft should stay lightweight until the SimCLR project finishes.

## Workflow Reproducibility Audit

Task 45 adds a workflow reproducibility audit at `notes/workflow_reproducibility_audit.md`. Use that audit with this draft when restarting this project in a new conversation or adapting the workflow to a future AI research coding project.

The audit should not replace this draft yet. It records what is currently sufficient, what remains risky, and what should be finalized later.

## Minimal Reusable File Set

For a new project, keep this small file set from the start:

- `AGENTS.md`
- `PROJECT_STATUS.md`
- `notes/task_registry.md`
- `notes/decision_log.md`
- `notes/agent_workflow_log.md`
- `notes/errors_and_fixes.md`
- `data/README.md`
- `experiments/`

These files make task scope, status, storage policy, decisions, failures, and evidence visible across conversations and tools.

## New Project Day 0 / Day 1

1. Choose the official repository location.
2. Create the WSL project directory.
3. Create external F-drive research directories.
4. Initialize Git.
5. Create `AGENTS.md` and `PROJECT_STATUS.md`.
6. Create the minimal notes and experiments structure.
7. Write `data/README.md` before downloading or generating data.
8. Create an initial commit before implementation starts.

Day 0 / Day 1 should establish workflow and storage rules, not model code.

## Storage And Large File Policy

- Source code stays in the WSL repository.
- Datasets stay under `/home/yeyee/research/03_datasets/<project_name>`.
- Checkpoints and models stay under `/home/yeyee/research/04_models/<project_name>`.
- Large exports stay under `/home/yeyee/research/05_exports/<project_name>`.
- Never commit datasets, checkpoints, weights, TensorBoard event files, W&B runs, or large generated artifacts.
- Small Markdown records and selected small CSV logs may be committed when they are useful evidence.

## Agent Roles

- Human Owner: final decision maker; runs important commands; approves commits and merges; verifies final understanding and real results.
- ChatGPT: planning, task design, review, debugging support, research reasoning, and interpretation checks.
- Codex: scoped implementation or documentation tasks only; must report exact changes, commands, validation, and gaps.
- Claude Code: optional docs, QA, checklist, and log cleanup support.

No agent replaces the Human Owner's final understanding or merge decision.

## Task Lifecycle

1. Plan the task.
2. Create one scoped branch.
3. Give Codex a narrow task with allowed and forbidden files.
4. Codex completes only that task.
5. Codex returns a Task Completion Report.
6. Human Owner sends the report and relevant files to ChatGPT for review.
7. ChatGPT reviews scope, logic, evidence, and risk.
8. Human Owner commits after review.
9. Human Owner merges to `main` when safe.
10. The next task updates status and registry with the previous task's commit hash.

Do not continue into the next task until the current task has been reviewed.

## Gate System

Use gates to prevent premature training or reporting:

- Gate 0: environment and storage verification.
- Gate 1: dataset, model, loss, and module tests.
- Gate 2: smoke training.
- Gate 3: evaluation or supervised scaffold and smoke.
- Later gates: baseline training, ablation, reporting, and final presentation.

Each gate should have explicit evidence before moving forward.

## When Not To Write New Code

Do not write new code when:

- The environment is not verified.
- Storage paths are not verified.
- The current task status is unclear.
- The current branch is not clean or contains unexplained changes.
- Codex's previous report is incomplete.
- A smoke result has not been recorded.
- A training plan has not been written.
- The task would expand beyond the latest owner-approved scope.

In these cases, inspect, report, and ask for the next owner decision.

## Commit And Merge Rules

- `main` must stay clean.
- Use one task branch per scoped task.
- Do not create a separate future commit only to fill in the current task hash.
- Fill in the current task commit hash during the next task.
- Status-only updates are allowed only at gate transitions or when they reduce confusion.
- Do not merge to `main` from an agent response alone; the Human Owner decides.

## Review Rules

- Do not rely only on Codex reports for code tasks.
- Upload files when ChatGPT needs code-level review.
- If ChatGPT cannot see a file, it must ask for the file instead of guessing.
- Smoke logs are not real performance results.
- Any reported metric needs command, config, seed, dataset path, checkpoint path, and limitations.

## Smoke Vs Baseline Vs Final Result

- Smoke run: validates that a pipeline can start, run briefly, log, and respect storage rules.
- Short baseline: preliminary controlled run used before longer training.
- Final baseline: planned config plus documented interpretation, failure records, and review.
- README must not overclaim smoke or short-baseline results as final performance.

## Log Display Rule

- For smoke logs with only a few lines, printing the whole CSV with `cat` is acceptable.
- For short-baseline, baseline, or long-run CSV logs, never print the whole file with `cat`.
- Use `wc -l <log.csv>`, `head -n 5 <log.csv>`, and `tail -n 10 <log.csv>` for terminal inspection.
- Use scripts or plotting tools for deeper analysis.

## When To Use Extra Codex Capabilities

- Plotting: use after CSV logs and result tables exist.
- GitHub connection: use after local workflow is stable and the first baseline stage is ready.
- Computer use: use only for UI, README, or GitHub page checks, not for dangerous actions or long training.
- Browser tools: use only when a browser-based check is explicitly useful and safe.

## Lessons Learned From This SimCLR Project So Far

- `PROJECT_STATUS.md` prevents task confusion across long conversations.
- External storage policy prevents system disk and repository pollution.
- Owner-run commands create trustworthy provenance for real smoke records.
- Codex must report what it actually did, not what it intended to do.
- ChatGPT should not guess unseen files.
- Commit hashes are easier to record in the next task after merge.
- Smoke records should state clearly that train accuracy is not performance.
- When task numbering changes, update all planning/status files in the same task instead of leaving only chat-level corrections.

## Next Use Of This Playbook

- Use this draft as a template for the next AI research coding project.
- Keep it lightweight until the SimCLR project finishes.
- Write the final version after baseline and ablation stages.
