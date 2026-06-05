# Workflow Reproducibility Audit

Date: 2026-06-05

## Purpose

This is a workflow audit, not an experiment result.

No training, evaluation, tests, figure generation, checkpoint creation, code edit, config edit, result-table edit, or experiment-record edit was performed for this audit.

## Why This Audit Is Needed

Long ChatGPT and Codex conversations can lose context, expire uploaded files, or become hard to navigate. This project now has enough completed work to test whether the workflow can be restarted from repository files rather than chat memory.

The Human Owner also wants the collaboration pattern to transfer to future AI research coding projects. That requires a small, explicit, repo-based workflow record: task scope, status, decisions, errors, storage rules, result provenance, and conservative interpretation rules.

## Current Reusable Documentation Set

| Item | What it currently does | Sufficient for reproducibility? | Weakness or risk | Keep, improve, or finalize later |
|---|---|---|---|---|
| `AGENTS.md` | Defines roles, source-of-truth order, scope, storage rules, validation gates, and mandatory Codex reports. | Mostly sufficient. | It is project-specific and long; future projects need a trimmed template. | Keep now; adapt into a reusable template later. |
| `PROJECT_STATUS.md` | Gives current stage, current task, branch, next gate, blockers, and completed gate checklist. | Sufficient for restarting current work. | It can become stale if not updated every task; some older status rows may lag detailed records. | Keep and update every task. |
| `notes/task_registry.md` | Indexes tasks, dates, status, commits, summaries, and main files. | Sufficient for task history and commit lookup. | It is manually maintained and can drift if commit hashes are not filled in during the next task. | Keep; consider a template for future projects. |
| `notes/decision_log.md` | Records durable workflow and research decisions with rationale. | Sufficient for major decisions. | Minor decisions remain in experiment records or workflow logs; not every decision belongs here. | Keep; update only for durable decisions. |
| `notes/agent_workflow_log.md` | Stores detailed Codex task reports, commands, validation, and not-validated items. | Sufficient but bulky. | It is long and harder to scan after many tasks; new conversations should not rely on reading it end to end. | Keep; use with `PROJECT_STATUS.md` and task registry. |
| `notes/errors_and_fixes.md` | Records real errors, fixes, and lessons such as module-style CLI execution and no-full-CSV-log display. | Sufficient for known recurring errors. | Only useful if agents remember to append future failures. | Keep; update when real failures happen. |
| `notes/workflow_playbook_draft.md` | Captures a reusable project workflow: file set, Day 0/1 setup, gates, task lifecycle, review rules, storage rules. | Sufficient as a draft. | It is not finalized and does not yet include lessons from multiple ablations and final reporting. | Keep as draft; finalize later. |
| `notes/baseline_training_plan.md` | Defines short-baseline scope, run order, output rules, failure rules, and interpretation rules. | Sufficient for the baseline phase. | It is baseline-specific and should not be overused for later ablations. | Keep as historical plan. |
| `notes/ablation_plan.md` | Defines the first ablation stage, no-projection priority, output rules, and interpretation rules. | Sufficient for no-projection and near-term ablation planning. | It does not yet plan strong-vs-weak augmentation or batch-size details. | Keep; extend only in a new approved planning task. |
| `experiments/` | Stores per-task experiment and run records from environment check through Task 44 analysis. | Sufficient for current evidence provenance. | Records are numerous; future readers need `task_registry.md` to find the latest relevant one quickly. | Keep; continue one focused record per run or analysis task. |
| `results/tables/` | Stores small result CSVs and Markdown result tables for short baseline and no-projection ablation. | Sufficient for current reported metrics. | CSVs are small and useful, but final tables still need final-report synthesis later. | Keep; do not edit CSVs after recording. |
| `results/figures/` | Stores selected short-baseline figures generated from existing logs and result tables. | Sufficient for current visual evidence. | Figures are not yet complete final-report visuals and only cover short-baseline curves. | Keep; add future figures only in approved tasks. |
| `README.md` | Public project overview, current short-baseline results, figures, storage policy, limitations, and next steps. | Partially sufficient. | It is v0.2 and now behind the first ablation; updating it should be a separate approved docs task. | Keep; update later after reviewed ablation status. |
| Git commit history | Records task commits, branch lineage, and merge progress into `main`. | Sufficient when task registry commit hashes are current. | Requires consistent commit, merge, and push behavior by the Human Owner. | Keep; review before each new task. |
| GitHub remote | `origin` points to `git@github.com:Lumos56/SimCLR-Reproduction-and-Ablation.git`; first push has been recorded. | Sufficient for remote backup and future PR workflow. | GitHub PR workflow is not yet active; GitHub rendering was not visually checked. | Keep active; introduce PR workflow later if useful. |

## Minimum Context Package For A New Conversation

When opening a new ChatGPT or Codex conversation for this project, the Human Owner should point the agent to these files first:

- `PROJECT_STATUS.md`
- `notes/task_registry.md`
- `notes/decision_log.md`
- `notes/workflow_playbook_draft.md`
- the latest relevant experiment record, for example `experiments/exp24_no_projection_ablation_analysis.md` after Task 44
- the current target task description, including allowed files, forbidden files, and do-not-run rules

For code-level review, also provide the actual source files under review. Summaries and Codex reports are not enough for high-risk code changes.

## Minimum Context Package For A New Project

For a future AI research coding project, copy or adapt this minimal workflow package:

- `AGENTS.md`
- `PROJECT_STATUS.md` template
- `notes/task_registry.md` template
- `notes/decision_log.md` template
- `notes/agent_workflow_log.md` template
- `notes/errors_and_fixes.md` template
- `data/README.md` storage policy
- `notes/workflow_playbook_draft.md`

The new project should rewrite project-specific paths, goals, scopes, model names, datasets, external storage directories, and validation gates before implementation begins.

## Task Numbering And Task Boundary Rules

- Do not change fixed task numbers casually.
- Preflight belongs inside run tasks unless explicitly planned otherwise.
- Every run task should include preflight, owner run, Codex record, review, commit, merge, and push.
- Status-only or log-only changes must not create extra task numbers unless the Human Owner approves them.
- The next task should fill in the previous task's commit hash after review and merge.
- A task should not start the next gate just because files for the next gate are easy to edit.

## When ChatGPT Should Ask For Files

- Code-level review requires uploading or pointing to the actual code files.
- If files are expired, unseen, or only summarized, ChatGPT must ask for them instead of guessing.
- Codex completion reports are useful for scope and command history, but they are not enough for high-risk code review.
- For tensor shape, loss logic, data leakage, checkpoint loading, or evaluation correctness, use actual source files and relevant tests.

## Result Interpretation Rules

- Smoke metrics are not baseline results.
- Training-batch accuracy is not test accuracy.
- Short baseline results are preliminary controlled-run evidence.
- Ablation results are preliminary unless repeated, scaled, and reviewed.
- README and report language must avoid final benchmark claims until final evidence exists.
- Experiment records must state command, config, seed, dataset path, checkpoint path, metric source, limitations, and what was not run.

## Large File And Storage Reproducibility

- Datasets stay outside the repository under `/home/yeyee/research/03_datasets/<project_name>`.
- Checkpoints and model weights stay outside the repository under `/home/yeyee/research/04_models/<project_name>`.
- Large exports stay outside the repository under `/home/yeyee/research/05_exports/<project_name>`.
- Small logs, tables, selected figures, documentation, and experiment records may stay in the repository.
- Never commit model weights, checkpoints, datasets, TensorBoard event files, W&B runs, or large generated artifacts.
- `data/README.md` is useful but currently has stale "Current Status" values; update it in a separate approved task if it becomes a reproducibility risk.

## Git And GitHub Workflow

- Use one local branch per scoped task.
- Review before commit.
- Merge reviewed task branches to `main`.
- Push `main` to `origin/main` after merge.
- GitHub remote is active: `origin` points to `git@github.com:Lumos56/SimCLR-Reproduction-and-Ablation.git`.
- Future GitHub pull request workflow can be introduced later after the current local branch, review, merge, and push workflow remains stable.
- Do not let GitHub workflow introduce premature CI, PR, or issue complexity before it adds clear value.

## Recommended Improvements

- Decide later whether to promote `notes/workflow_playbook_draft.md` to a finalized reusable guide.
- Consider adding a project-start checklist.
- Consider adding a task-completion-report template file.
- Consider adding a lightweight task prompt template with allowed files, forbidden files, do-not-run rules, and acceptance criteria.
- Consider adding GitHub issue and PR workflow after the current local workflow remains stable.
- Consider adding a short "new conversation restart" checklist to `PROJECT_STATUS.md` or a separate template.

## Current Verdict

The current workflow is reproducible enough to continue after a long or restarted conversation. A new agent can recover the current stage from `PROJECT_STATUS.md`, reconstruct history from `notes/task_registry.md`, understand durable decisions from `notes/decision_log.md`, and find evidence from `experiments/` and `results/tables/`.

The workflow is not yet finalized as a reusable template. The final reusable version should be written after more ablations and the final report, when the project has tested the workflow across setup, implementation, smoke, baseline, ablation, analysis, and presentation stages.
