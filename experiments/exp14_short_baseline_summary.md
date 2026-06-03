# Experiment 14: Short Baseline Training Summary

## Purpose

Summarize the first completed short-baseline training stage and plan the next evaluation scaffold.

This is a summary and planning record. It is not a training run, not an evaluation run, and not a final performance report.

## Current Completed Short-Baseline Runs

The following short-baseline training records have been completed:

| Run | Task | Experiment Record |
|---|---|---|
| Supervised short baseline | Task 28 | `experiments/exp11_supervised_short_baseline.md` |
| SimCLR short pretrain | Task 29 | `experiments/exp12_simclr_short_pretrain.md` |
| Linear probe short on short SimCLR checkpoint | Task 30 | `experiments/exp13_linear_probe_short.md` |

## What Each Run Validates

### Supervised Short Baseline

- Validates that the supervised ResNet18 training path can run on real CIFAR-10 for the approved short-baseline scope.
- Validates that the short supervised config writes a small CSV log to the repository and a checkpoint to external model storage.
- Does not validate CIFAR-10 test-set accuracy.

### SimCLR Short Pretrain

- Validates that the SimCLR pretraining path can run on real CIFAR-10 for the approved short-baseline scope.
- Validates that the short SimCLR config writes a small CSV log to the repository and a checkpoint to external model storage.
- Does not validate representation quality.

### Linear Probe Short

- Validates that the linear probe training path can load the short SimCLR checkpoint and train the classifier head for the approved short-baseline scope.
- Validates that the short linear probe config writes a small CSV log to the repository and a checkpoint to external model storage.
- Does not validate CIFAR-10 test-set accuracy.

## Metrics Available Now

Current available metrics are training-log metrics only:

- Supervised short baseline: final logged training loss and final logged training-batch accuracy.
- SimCLR short pretrain: final logged contrastive training loss.
- Linear probe short: final logged training loss and final logged training-batch accuracy.

Detailed values are summarized in:

```text
results/tables/short_baseline_training_summary.md
```

## Metrics Still Missing

No CIFAR-10 test-set evaluation has been run yet.

The project does not yet have:

- supervised checkpoint test-set Top-1 accuracy;
- linear probe checkpoint test-set Top-1 accuracy;
- a comparable supervised-vs-linear-probe evaluation table;
- a formal baseline performance claim.

## Why Train-Batch Accuracy Is Not Enough

The supervised short baseline and linear probe short runs report the accuracy of the last logged training batch. That value is useful for checking that training is progressing, but it is not a test-set metric.

Training-batch accuracy can reflect memorization, optimizer state, augmentation behavior, class composition of the final batch, and other training-loop details. It does not measure generalization to held-out CIFAR-10 test data.

Therefore:

- supervised short baseline train accuracy is not test accuracy;
- linear probe short train accuracy is not test accuracy;
- SimCLR short pretrain loss is not representation quality;
- no CIFAR-10 test-set evaluation has been run yet.

## Next Task Decision: Implement Evaluation Scaffold

Task 32 should implement the evaluation scaffold before ablation.

Reasoning:

- The project now has training logs and checkpoints, but no test-set evaluation.
- The supervised short baseline and linear probe short need comparable test-set Top-1 metrics.
- Evaluation should be implemented and smoke-tested before any ablation, otherwise ablation results would not have a validated comparison path.

Task 32 should:

- implement evaluation scaffold;
- support supervised checkpoint evaluation;
- support linear probe checkpoint evaluation;
- compute CIFAR-10 test-set Top-1 accuracy;
- use fake-data tests first;
- avoid running real evaluation in Task 32.

## Risks And Limitations

- The current short-baseline numbers are training-log values, not final performance values.
- The supervised and linear probe training accuracies are last-batch training accuracies, not epoch averages.
- The SimCLR loss does not directly indicate representation quality.
- The current summary is not README-ready performance evidence.
- Any future evaluation result must record config, command, checkpoint path, dataset path, seed, metrics, and limitations.

## Next Steps

1. Review and commit this Task 31 summary.
2. Implement Task 32 evaluation scaffold with fake-data tests only.
3. After scaffold review, request owner approval before any real CIFAR-10 evaluation run.
