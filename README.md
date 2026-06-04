# SimCLR Reproduction and Ablation

README version: v0.2

## Overview

This repository is a compact PyTorch SimCLR reproduction and ablation-preparation project on CIFAR-10.

It is also a first AI research coding project: the main goal is to practice reproducible implementation, validation, experiment tracking, and honest result interpretation. The project is intentionally small and is not intended to claim state-of-the-art performance.

## Research Direction

SimCLR is used here as a practical entry point into contrastive representation learning. The longer-term direction is to use the engineering workflow and representation-learning foundation from this project as a stepping stone toward later audio and audio-visual intelligence research.

This repository does not implement audio training, video processing, Audio-SimCLR, CLAP, AV-HuBERT, ImageBind, or audio-visual synchronization.

## Current Status

- CIFAR-10 dataset loading and two-crop augmentation are implemented.
- CIFAR-style ResNet18 encoder and projection head are implemented.
- NT-Xent contrastive loss is implemented.
- SimCLR fake smoke, real CIFAR-10 smoke, and short baseline pretraining have been completed.
- Linear probe scaffold, fake/real smoke runs, short training, and short CIFAR-10 test evaluation have been completed.
- Supervised baseline scaffold, fake/real smoke runs, short training, and short CIFAR-10 test evaluation have been completed.
- Short-baseline result tables and plots have been generated.
- Ablations and final reporting have not started yet.

## Short Baseline Results

These are preliminary short-baseline results on the CIFAR-10 test split. They are not final benchmark results and should not be compared directly with paper-scale SimCLR results.

| Method | Training setup | Dataset split | Top-1 accuracy | Correct / total |
|---|---|---|---:|---:|
| Supervised short baseline | Supervised ResNet18, 10 epochs | CIFAR-10 test | 0.873700 | 8737 / 10000 |
| SimCLR short + linear probe | SimCLR pretrain, 10 epochs; linear probe, 5 epochs | CIFAR-10 test | 0.621400 | 6214 / 10000 |

The supervised short baseline is currently higher than the short SimCLR plus linear-probe path. This is expected at this stage because the contrastive pretraining run is short, no hyperparameter tuning has been done, and no ablation has been run. The value of this stage is a controlled first comparison and a validated workflow, not final model performance.

Primary result records:

- `results/tables/short_baseline_results.md`
- `results/tables/supervised_short_eval.csv`
- `results/tables/linear_probe_short_eval.csv`
- `experiments/exp17_short_baseline_analysis.md`

## Figures

![Short baseline CIFAR-10 test accuracy](results/figures/short_baseline_test_accuracy.png)

![Supervised short loss curve](results/figures/supervised_short_loss_curve.png)

![SimCLR short loss curve](results/figures/simclr_short_loss_curve.png)

![Linear probe short loss curve](results/figures/linear_probe_short_loss_curve.png)

The loss figures show raw logged curves plus smoothed trend lines for readability. No CSV values were changed to create the figures.

## Repository Structure

```text
.
|-- README.md
|-- AGENTS.md
|-- environment.yml
|-- configs/
|-- src/
|-- tests/
|-- experiments/
|-- notes/
|-- results/
|   |-- figures/
|   |-- logs/
|   `-- tables/
|-- report/
`-- .github/
```

## Installation

Environment setup is controlled by the Human Owner. The project has been developed with a local conda environment at:

```text
/home/yeyee/miniconda3/envs/simclr
```

The placeholder `environment.yml` should not be treated as a complete lock file. Use the official PyTorch selector when recreating or changing the environment, especially for CUDA-compatible `torch` and `torchvision` versions.

## How To Reproduce Current Checks

Environment and storage verification is recorded in:

```text
experiments/exp00_environment_check.md
```

Run the current lightweight test suite:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m pytest -q tests/test_dataset.py tests/test_model_shapes.py tests/test_nt_xent.py tests/test_simclr_integration.py tests/test_train_simclr_smoke.py tests/test_linear_probe_smoke.py tests/test_supervised_smoke.py tests/test_evaluate_smoke.py
```

Regenerate the short-baseline figures from existing logs and result CSVs:

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.plot_training_curves
```

Long training and real evaluation commands are recorded in experiment notes and should not be treated as casual quick-start commands.

## Storage Policy

Datasets, checkpoints, model weights, and large exports are stored outside the Git repository.

Default external locations:

```text
Raw datasets:
/home/yeyee/research/03_datasets/SimCLR-Reproduction-and-Ablation

Models and checkpoints:
/home/yeyee/research/04_models/SimCLR-Reproduction-and-Ablation

Large exports:
/home/yeyee/research/05_exports/SimCLR-Reproduction-and-Ablation
```

The repository may contain source code, configs, tests, documentation, small CSV logs, small result tables, and selected lightweight figures. It must not contain datasets, `.pt`, `.pth`, `.ckpt`, `.onnx`, TensorBoard event files, W&B runs, or large generated artifacts.

## Agent Workflow

Project workflow and guardrails are tracked in:

- `AGENTS.md`
- `PROJECT_STATUS.md`
- `notes/task_registry.md`
- `notes/workflow_playbook_draft.md`
- `notes/agent_workflow_log.md`

Each task should stay scoped, record commands that were actually run, and distinguish implementation checks, smoke runs, short-baseline results, and final results.

## Limitations

- Current metrics are short-baseline results only.
- No ablation has been run yet.
- No final benchmark claim is made.
- No final report has been written yet.
- The current results should not be compared directly with paper-scale SimCLR results.
- This repository is a small CIFAR-10 research-engineering project, not a full reproduction of the original SimCLR paper.

## Next Steps

- Set up the GitHub remote and first push, if the owner chooses that gate next.
- Plan the ablation stage before running ablations.
- Run the no-projection-head ablation.
- Run the strong-vs-weak augmentation ablation.
- Run the batch-size ablation.
- Write the final report after baseline and ablation evidence is complete.

## References

- Chen, T., Kornblith, S., Norouzi, M., and Hinton, G. A Simple Framework for Contrastive Learning of Visual Representations.
- Official PyTorch installation selector.
