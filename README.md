# SimCLR Reproduction and Ablation

## Overview

This repository is a small-scale research-engineering project for reproducing the core SimCLR workflow on CIFAR-10 and studying targeted ablations.

The repository is currently in the setup stage. No dataset pipeline, model, loss, training loop, evaluation code, or experiment result has been implemented or validated yet.

## Motivation

The goal is to build a clean, reproducible, and explainable contrastive learning foundation project. The project emphasizes clear implementation boundaries, traceable experiments, and honest reporting over benchmark scale.

## Connection to Audio-Visual Intelligence

SimCLR is used here as a practical entry point into contrastive representation learning. The longer-term direction is to use this foundation to reason about audio representation learning and audio-visual intelligence systems such as Audio-SimCLR, CLAP-like contrastive learning, and audio-visual synchronization.

## Current Status

- Stage: Day 1 / Sprint 0 setup.
- Scope completed in this version: repository skeleton and documentation templates.
- Scope not completed: all implementation, environment verification, training, evaluation, and real experiments.

## Repository Structure

```text
.
|-- README.md
|-- AGENTS.md
|-- environment.yml
|-- configs/
|-- src/
|-- tests/
|-- scripts/
|-- experiments/
|-- notes/
|-- results/
|-- report/
`-- .github/
```

## Installation

Environment setup is controlled by the Human Owner. The placeholder `environment.yml` intentionally does not guess PyTorch or CUDA wheel versions.

Use the official PyTorch selector before adding exact `torch` and `torchvision` dependencies.

## Quick Start

At this stage, there is no runnable SimCLR training command.

Lightweight repository checks:

```bash
pwd
git status --short
python -c "import pathlib; print('repo files visible:', pathlib.Path('.').exists())"
```

## Planned Experiments

- Gate 0: environment check.
- Gate 1: core module shape and loss checks.
- Gate 2: smoke pretraining.
- Gate 3: SimCLR baseline and supervised baseline.
- Gate 4: ablations for projection head, augmentation strength, and batch size.

## Agent Workflow

Agent responsibilities and guardrails are defined in `AGENTS.md`. Each scoped task should end with an Agent Work Log in `notes/agent_workflow_log.md` or in the task response.

## Limitations

- No real experiment has been run.
- No accuracy, loss curve, embedding visualization, or table is available yet.
- The environment has not been verified.
- CIFAR-10 data policy is not yet validated.

## Future Work

- Complete Gate 0 environment verification.
- Add CIFAR-10 data loading and SimCLR augmentations.
- Implement the encoder, projection head, and NT-Xent loss.
- Add smoke tests before any full training.
- Prepare a future decision memo for audio/audio-visual follow-up work.

## References

- Chen, T., Kornblith, S., Norouzi, M., and Hinton, G. A Simple Framework for Contrastive Learning of Visual Representations.
- Official PyTorch installation selector.
