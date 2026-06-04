# Experiment 18: Short Baseline Curves

## Purpose

Generate short-baseline visualization figures from existing CSV logs and result tables.

This is a visualization task only. No new training, evaluation, dataset download, checkpoint creation, figure from fabricated data, or ablation was run in Task 36.

## Input Files

| Input | Used for |
|---|---|
| `results/logs/cifar10_supervised_short.csv` | Supervised short training loss curve |
| `results/logs/cifar10_simclr_short.csv` | SimCLR short pretraining loss curve |
| `results/logs/cifar10_linear_probe_short.csv` | Linear probe short training loss curve |
| `results/tables/supervised_short_eval.csv` | Supervised short CIFAR-10 test Top-1 bar |
| `results/tables/linear_probe_short_eval.csv` | SimCLR short plus linear-probe CIFAR-10 test Top-1 bar |

## Output Figures

| Figure | Source |
|---|---|
| `results/figures/supervised_short_loss_curve.png` | `results/logs/cifar10_supervised_short.csv` |
| `results/figures/simclr_short_loss_curve.png` | `results/logs/cifar10_simclr_short.csv` |
| `results/figures/linear_probe_short_loss_curve.png` | `results/logs/cifar10_linear_probe_short.csv` |
| `results/figures/short_baseline_test_accuracy.png` | `results/tables/supervised_short_eval.csv`, `results/tables/linear_probe_short_eval.csv` |

The final loss figures show both the raw logged curve and a smoothed rolling-mean trend line. The rolling mean improves readability only; no underlying CSV values were changed.

## Command

```bash
/home/yeyee/miniconda3/envs/simclr/bin/python -m src.plot_training_curves
```

## Interpretation Limits

- These are short-baseline visualizations, not final benchmark plots.
- The loss curves show logged training loss from existing short-baseline runs.
- The loss curves include the raw curve as a secondary visual layer plus a rolling-mean trend line for readability.
- The test-accuracy bar chart shows the existing Task 33 and Task 34 CIFAR-10 test-set metrics.
- The figures do not add new evidence beyond the existing logs and result CSVs.
- The figures must not be used to claim final supervised or final SimCLR performance.
- The figures are suitable for README v0.2 as preliminary short-baseline visualizations.

## Not Run

- No training was run.
- No evaluation was run.
- No tests were run for this visualization task.
- No checkpoints or model files were created.
- Existing CSV logs and result tables were not edited.
- No data values were changed.

## Next Step

Review and commit Task 36, then decide whether to start README v0.2 update.
