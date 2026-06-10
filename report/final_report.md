# SimCLR Reproduction and Short Ablation Study on CIFAR-10

Status note: this is a Task 59 first draft. It expands the Task 58 scaffold into a coherent report narrative, but it should still be reviewed and polished before being treated as the final submitted report. All reported metrics are copied from existing result tables and experiment records. No new training, evaluation, or result generation is implied by this draft.

## 1. Abstract / Project Summary

This project implements a compact SimCLR-style contrastive learning pipeline on CIFAR-10 and uses it as a controlled research-engineering exercise. The implementation includes CIFAR-10 data loading, two-view image augmentation, a CIFAR-adapted ResNet18 encoder, a projection head, NT-Xent contrastive loss, SimCLR pretraining, frozen-encoder linear probe evaluation, and a supervised ResNet18 reference baseline.

The project focuses on reproducibility and honest result interpretation rather than paper-scale performance. After validating the implementation with fake-data tests and short smoke runs, the project runs a short baseline setting: 10 epochs of SimCLR pretraining followed by 5 epochs of linear probe training. Under this short setup, the supervised reference baseline reaches `0.873700` CIFAR-10 test Top-1 accuracy, while the SimCLR short baseline plus linear probe reaches `0.621400`.

Three short ablations are then performed on the SimCLR pipeline. Removing the projection head gives `0.594500` Top-1 accuracy, weak augmentation gives `0.356600`, and reducing SimCLR pretraining batch size from 128 to 64 gives `0.596100`. These results suggest that, in this short single-run setup, weak augmentation produces the largest degradation, while no projection head and batch size 64 are both slightly lower than the baseline. These observations are preliminary. They should not be interpreted as definitive conclusions about SimCLR in general because the experiments use CIFAR-10 only, short training schedules, one run per variant, no hyperparameter tuning, and no repeated seeds.

A second goal of the project is to build a reusable AI-assisted research coding workflow. The repository tracks tasks, decisions, experiment records, status updates, result tables, figures, and workflow audits so the project can be resumed across long ChatGPT/Codex conversations without relying only on chat memory.

## 2. Motivation and Background

Self-supervised representation learning aims to learn useful features from data without requiring manual labels for every training example. Contrastive learning is one important family of self-supervised methods. It trains a model to bring related views of the same input closer together in representation space while pushing unrelated examples apart. In image representation learning, this often means generating two augmented views of the same image and treating them as a positive pair.

SimCLR is a useful starting point for learning this paradigm because its pipeline is conceptually compact. It combines stochastic data augmentation, an encoder network, a small projection head, and a contrastive loss over positive and negative pairs. The method is also a practical bridge toward later work in audio and audio-visual intelligence. Many audio, audio-text, and audio-visual representation learning methods reuse the same high-level ideas: augment or pair inputs, encode them into embeddings, and train those embeddings to align across views or modalities.

This project uses CIFAR-10 because it is small enough for iterative experimentation while still large enough to exercise a realistic training and evaluation workflow. The goal is not to reproduce the full SimCLR paper result. Instead, the goal is to learn the research engineering loop: implement core components, test them, run short baselines, perform controlled ablations, record results, and interpret limitations carefully.

## 3. Method: SimCLR Pipeline

### 3.1 Data Augmentation and Two-View Construction

The contrastive pretraining stage uses two augmented views of each image. For each input image, the dataset pipeline returns two independently augmented crops. These two views form a positive pair. Other images in the same batch provide in-batch negative examples.

The baseline SimCLR configuration uses a stronger augmentation setting designed to produce varied but semantically related views. The ablation study also includes a weak augmentation variant. This is important because SimCLR-style learning depends heavily on view construction: if the two views are too similar, the task may become too easy and the model may learn less robust invariances; if the views are too distorted, the positive pair relationship may become too difficult. The current project tests this qualitatively by comparing the strong baseline against a weak augmentation run under the same short training schedule.

### 3.2 Encoder

The encoder is a CIFAR-adapted ResNet18. It maps a normalized CIFAR-10 image to a 512-dimensional representation. The encoder is used in three settings:

- supervised training, where a classifier head is trained directly with labels;
- SimCLR pretraining, where encoder features are fed through a projection head and optimized with a contrastive loss;
- linear probe training, where the encoder is frozen and a linear classifier is trained on CIFAR-10 labels.

Using the same encoder family for supervised and contrastive paths makes the comparison easier to interpret at the project level, although the training objectives differ.

### 3.3 Projection Head

The default SimCLR model includes a projection head after the encoder. The projection head maps encoder features into the space where the contrastive loss is applied. The baseline uses this projection head during SimCLR pretraining, while the linear probe evaluates the frozen encoder representation rather than the projection output.

The no-projection ablation disables the projection head and applies the contrastive objective directly to the encoder representation. This ablation tests whether the projection head helps in the current short CIFAR-10 setup. The project records this as a short ablation only; it does not claim a definitive statement about projection heads in all SimCLR settings.

### 3.4 NT-Xent Loss

The contrastive objective is NT-Xent. For each image, two augmented views are encoded. The corresponding pair is treated as positive, while other views in the batch act as negatives. The model is trained so that positive pairs have high similarity while nonmatching examples have lower similarity.

In this project, the loss is implemented and tested independently before being used in training. This separation makes the workflow easier to audit: dataset utilities, model shape behavior, loss behavior, and integration behavior were validated before real CIFAR-10 training runs.

### 3.5 Linear Probe Evaluation

Linear probe evaluation freezes the pretrained encoder and trains a linear classifier on top of its features. This is a common way to estimate whether the learned representation contains useful information for downstream classification. The current project trains a short 5-epoch linear probe and evaluates it on the CIFAR-10 test split.

It is important to distinguish three types of values in the project records:

- contrastive training loss from SimCLR pretraining;
- last-batch training accuracy from supervised or linear-probe training logs;
- held-out CIFAR-10 test accuracy from evaluation runs.

Only the evaluation outputs are used as primary comparison metrics in the result tables.

## 4. Implementation Overview

The repository is organized to support reproducible task-level development:

- `src/` contains dataset, augmentation, model, loss, training, evaluation, and plotting code.
- `configs/` contains explicit configuration files for smoke runs, short baselines, evaluations, and ablations.
- `tests/` contains lightweight fake-data and unit tests for core behavior.
- `experiments/` contains task-by-task experiment and documentation records.
- `results/logs/` stores small CSV training logs.
- `results/tables/` stores small CSV and Markdown result tables.
- `results/figures/` stores selected lightweight visualization outputs.
- `notes/` stores workflow logs, task registry, decisions, planning documents, and reproducibility audits.

Datasets and model checkpoints are intentionally stored outside the Git repository. The project uses external research storage under paths such as:

```text
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation
```

This prevents large data files and model weights from polluting the repository. Small logs, result tables, figures, configs, and documentation are committed because they are necessary for review and reproducibility.

The project also uses a strict branch-per-task workflow. Each scoped task updates `PROJECT_STATUS.md`, `notes/task_registry.md`, and `notes/agent_workflow_log.md`, and most important decisions are recorded in `notes/decision_log.md`. This workflow proved useful when long AI assistant conversations lost context or when uploaded files expired.

## 5. Dataset and Experimental Setup

The project uses CIFAR-10. The completed short experiments use the following schedules:

| Stage | Schedule |
|---|---:|
| Supervised short baseline | 10 epochs |
| SimCLR short pretraining | 10 epochs |
| Linear probe training | 5 epochs |

The baseline SimCLR run uses strong augmentation, projection head enabled, and SimCLR pretraining batch size 128. The three ablations change one major factor at a time:

| Ablation | Changed factor | Baseline setting | Ablation setting |
|---|---|---|---|
| No projection | Projection head | Enabled | Disabled |
| Weak augmentation | Augmentation strength | Strong | Weak |
| Batch64 | SimCLR pretrain batch size | 128 | 64 |

For the batch size ablation, the linear probe batch size remains 128. This reduces confounding in the downstream probe stage. However, the comparison is fixed-epoch rather than fixed-optimizer-step. Since batch size 64 creates more optimizer steps per epoch than batch size 128, the batch-size ablation must be interpreted cautiously.

All current experiments are single-run, short-run experiments. There are no repeated seeds, no long training runs, and no hyperparameter sweeps.

## 6. Baseline Results

The supervised baseline provides a reference point for CIFAR-10 classification with labels. It is not a SimCLR ablation row. The SimCLR short + linear probe result is the baseline for the ablation comparisons.

| Run | CIFAR-10 test Top-1 | Correct / total | Role |
|---|---:|---:|---|
| Supervised short baseline | 0.873700 | 8737 / 10000 | Supervised reference context |
| SimCLR short + linear probe | 0.621400 | 6214 / 10000 | SimCLR ablation baseline |

The supervised short baseline is substantially higher than the SimCLR short + linear probe result. This is expected in a short training setup: supervised training directly optimizes the target labels, while SimCLR first learns representations through a self-supervised contrastive objective and only later trains a linear classifier. The SimCLR result should therefore be interpreted as a representation-learning baseline, not as a failure to match supervised training.

The value of this baseline stage is that it validates the full pipeline: pretraining, checkpointing, linear probing, evaluation, result recording, and comparison against a supervised reference all work under controlled conditions.

## 7. Ablation Studies

The completed ablations compare variants against the baseline SimCLR short + linear probe run. The table below consolidates the completed short ablations.

| Run / variant | Changed factor | Projection head | Augmentation strength | SimCLR pretrain batch size | Linear probe batch size | Pretrain epochs | Linear probe epochs | CIFAR-10 test Top-1 | Correct / total | Delta vs SimCLR baseline |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| SimCLR short + linear probe | Reference | Enabled | Strong | 128 | 128 | 10 | 5 | 0.621400 | 6214 / 10000 | 0.00 pp |
| No-projection SimCLR short + linear probe | Projection head disabled | Disabled | Strong | 128 | 128 | 10 | 5 | 0.594500 | 5945 / 10000 | -2.69 pp |
| Weak-augmentation SimCLR short + linear probe | Weak augmentation | Enabled | Weak | 128 | 128 | 10 | 5 | 0.356600 | 3566 / 10000 | -26.48 pp |
| Batch64 SimCLR short + linear probe | SimCLR pretrain batch size 64 | Enabled | Strong | 64 | 128 | 10 | 5 | 0.596100 | 5961 / 10000 | -2.53 pp |

### 7.1 Projection Head Ablation

The no-projection ablation disables the projection head and applies the contrastive objective directly to the encoder representation. The no-projection result is `0.594500`, which is `2.69` percentage points lower than the baseline SimCLR short + linear probe result of `0.621400`.

This is consistent with the idea that the projection head may help the encoder learn better representations by allowing the contrastive objective to operate in a separate projection space. However, the current evidence is not definitive. The run is short, uses one dataset, has no repeated seeds, and has no tuning.

### 7.2 Augmentation Strength Ablation

The weak augmentation ablation replaces the strong SimCLR augmentation setting with a weaker view-construction setting. The weak-augmentation result is `0.356600`, which is `26.48` percentage points lower than the strong-augmentation baseline.

This is the largest negative drop among the completed short ablations. It is consistent with SimCLR's reliance on strong augmentations to create useful contrastive views. In this setup, weak augmentation likely produces a less effective pretext task, resulting in weaker representations for the downstream linear probe.

The result should still be interpreted conservatively. It does not prove that strong augmentation is universally better in every setting. It only shows that, in the current short CIFAR-10 setup, the weak augmentation configuration performs much worse than the strong baseline.

### 7.3 Batch Size Ablation

The batch-size ablation changes the SimCLR pretraining batch size from 128 to 64 while keeping the linear probe batch size at 128. The batch64 result is `0.596100`, which is `2.53` percentage points lower than the batch128 SimCLR baseline.

This suggests that the baseline batch size 128 worked slightly better in the current short setup. However, this ablation has an important caveat: it uses fixed epochs rather than fixed optimizer steps. Because batch size 64 produces more optimizer steps per epoch than batch size 128, the two pretraining runs do not have matched optimization-step counts. This prevents a strong conclusion about batch size alone.

## 8. Main Observations

The completed short ablations show three main patterns.

First, weak augmentation produced the largest observed drop. Its `-26.48 pp` difference from the baseline is much larger than the differences from no-projection and batch64. This supports the practical expectation that strong view construction is central to SimCLR-style learning, at least in this short CIFAR-10 setup.

Second, disabling the projection head lowered performance by `2.69 pp`. This is a modest but consistent drop in the current run. It suggests that preserving the projection head is reasonable for this project, but it does not prove the projection head is always necessary.

Third, batch size 64 was `2.53 pp` lower than batch size 128 in the current fixed-epoch comparison. This result is close in magnitude to the no-projection difference, but it is harder to interpret because changing batch size also changes the number of optimizer steps per epoch.

Overall, the strongest project-level observation is that weak augmentation substantially hurts the current short SimCLR pipeline. The other two ablations show smaller negative shifts. All conclusions remain preliminary.

## 9. Limitations

The current project has several important limitations:

- CIFAR-10 only.
- 10-epoch SimCLR pretraining.
- 5-epoch linear probe training.
- Single run per variant.
- No repeated seeds.
- No long training.
- No hyperparameter tuning.
- Batch-size ablation uses fixed epochs, not fixed optimizer steps.
- The supervised reference is a short baseline, not final supervised performance.
- The SimCLR results are not paper-scale SimCLR benchmark results.
- The project does not compare against external implementations or published CIFAR-10 SimCLR numbers.

These limitations are intentional for the current course/research-training scope. The project prioritizes a controlled, reproducible implementation and ablation workflow over large-scale benchmark performance.

## 10. Reproducibility and Workflow

The project uses a task-based workflow to keep the research process auditable. Each task is scoped, recorded, reviewed, and committed separately. The main workflow artifacts are:

- `PROJECT_STATUS.md`, which records the current stage and next gate;
- `notes/task_registry.md`, which tracks tasks and commit hashes;
- `notes/decision_log.md`, which records durable project decisions;
- `notes/agent_workflow_log.md`, which records task reports and validations;
- `experiments/`, which stores task-specific experiment records;
- `results/tables/`, which stores small result tables;
- `results/logs/`, which stores small training logs;
- `notes/workflow_reproducibility_audit.md`, which audits whether the project can be resumed across long or restarted AI-assistant conversations.

This workflow matters because the project was developed through iterative collaboration between the Human Owner, ChatGPT, and Codex. In this setup, the Human Owner makes final decisions and runs important commands, ChatGPT plans and reviews tasks, and Codex performs scoped implementation or documentation work. The repository files are designed to reduce dependence on any single chat context.

The project also enforces a storage policy. Datasets and checkpoints stay outside the repository, while small configs, logs, figures, result tables, documentation, and experiment records are committed. This makes the repository lightweight but still reproducible enough to audit the experiments.

## 11. Future Work

The most immediate next step is to polish the final report and README, then perform a project checkpoint review. Potential technical extensions include longer SimCLR pretraining, repeated seeds, a fixed-step batch-size comparison, stronger representation diagnostics, and embedding visualizations.

A longer-term research direction is to transfer this contrastive-learning workflow toward audio and audio-visual intelligence. SimCLR provides a useful foundation because many audio and multimodal representation learning methods rely on related ideas: constructing multiple views, aligning embeddings, evaluating learned representations, and carefully interpreting downstream metrics.

Possible next projects include:

- Audio-SimCLR on spectrograms;
- a lightweight CLAP-style audio-text representation project;
- audio-visual synchronization or retrieval;
- spatial audio representation learning.

These directions should be treated as future projects, not as claims made by the current CIFAR-10 image-only experiment.

## 12. Appendix / File Index

Key project files:

- `README.md`: project-display overview and current status.
- `report/final_report.md`: final report draft.
- `results/tables/short_baseline_results.md`: supervised and SimCLR short baseline results.
- `results/tables/combined_ablation_results.md`: combined short ablation table.
- `results/tables/no_projection_ablation_results.md`: projection head ablation table.
- `results/tables/augmentation_ablation_results.md`: augmentation strength ablation table.
- `results/tables/batch_size_ablation_results.md`: batch-size ablation table.
- `experiments/`: task-by-task experiment and documentation records.
- `notes/task_registry.md`: task history and commit index.
- `notes/decision_log.md`: durable decisions.
- `notes/agent_workflow_log.md`: detailed agent task reports.
- `notes/workflow_reproducibility_audit.md`: workflow restartability audit.
- `AGENTS.md`: agent rules and project guardrails.
