"""Generate short-baseline training and evaluation figures.

These plots are short-baseline visualizations for inspection and README v0.2
preparation. They are not final benchmark plots.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "results" / "figures"
FIGURE_SIZE = (6.4, 4.2)
DPI = 150
TITLE_SIZE = 12
LABEL_SIZE = 10
TICK_SIZE = 9
NOTE_SIZE = 8
ROLLING_WINDOW = 100


def read_metric_series(csv_path: Path, metric_column: str) -> tuple[list[int], list[float]]:
    """Read ``step`` and a numeric metric column from an existing CSV log."""

    steps: list[int] = []
    values: list[float] = []
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required_columns = {"step", metric_column}
        if reader.fieldnames is None or not required_columns.issubset(reader.fieldnames):
            raise ValueError(f"{csv_path} must contain columns {sorted(required_columns)}")

        for row in reader:
            steps.append(int(row["step"]))
            values.append(float(row[metric_column]))

    if not steps:
        raise ValueError(f"{csv_path} has no data rows")
    return steps, values


def rolling_mean(values: list[float], window: int = ROLLING_WINDOW) -> list[float]:
    """Compute a trailing rolling mean without changing the source data."""

    if window <= 0:
        raise ValueError("rolling window must be positive")

    means: list[float] = []
    running_sum = 0.0
    for index, value in enumerate(values):
        running_sum += value
        if index >= window:
            running_sum -= values[index - window]
            denominator = window
        else:
            denominator = index + 1
        means.append(running_sum / denominator)
    return means


def plot_loss_curve(
    csv_path: Path,
    metric_column: str,
    output_path: Path,
    title: str,
    ylabel: str,
    color: str,
) -> Path:
    """Plot one short-baseline training loss curve from an existing log."""

    steps, values = read_metric_series(csv_path, metric_column)
    smoothed_values = rolling_mean(values)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, axis = plt.subplots(figsize=FIGURE_SIZE, dpi=DPI)
    axis.plot(
        steps,
        values,
        color=color,
        linewidth=0.55,
        alpha=0.22,
        label="Raw logged loss",
    )
    axis.plot(
        steps,
        smoothed_values,
        color=color,
        linewidth=2.1,
        label=f"Rolling mean ({ROLLING_WINDOW} steps)",
    )
    axis.set_title(title, fontsize=TITLE_SIZE, pad=10)
    axis.set_xlabel("Training step", fontsize=LABEL_SIZE)
    axis.set_ylabel(ylabel, fontsize=LABEL_SIZE)
    axis.tick_params(axis="both", labelsize=TICK_SIZE)
    axis.grid(True, alpha=0.25)
    axis.legend(loc="upper right", frameon=False, fontsize=NOTE_SIZE)
    axis.text(
        0.99,
        0.02,
        "Short baseline, not final benchmark",
        transform=axis.transAxes,
        ha="right",
        va="bottom",
        fontsize=NOTE_SIZE,
        color="dimgray",
    )
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def read_eval_accuracy(csv_path: Path) -> dict[str, str | float]:
    """Read one-row short-baseline evaluation CSV output."""

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    if len(rows) != 1:
        raise ValueError(f"{csv_path} must contain exactly one result row")
    row = rows[0]
    required_columns = {"mode", "dataset", "dataset_split", "top1_accuracy", "correct", "total"}
    if not required_columns.issubset(row):
        raise ValueError(f"{csv_path} must contain columns {sorted(required_columns)}")

    return {
        "mode": row["mode"],
        "dataset": row["dataset"],
        "dataset_split": row["dataset_split"],
        "top1_accuracy": float(row["top1_accuracy"]),
        "correct": row["correct"],
        "total": row["total"],
    }


def plot_test_accuracy(
    supervised_eval_csv: Path,
    linear_probe_eval_csv: Path,
    output_path: Path,
) -> Path:
    """Plot short-baseline CIFAR-10 test Top-1 accuracy from result CSVs."""

    supervised = read_eval_accuracy(supervised_eval_csv)
    linear_probe = read_eval_accuracy(linear_probe_eval_csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    labels = ["Supervised\nshort", "SimCLR short\n+ linear probe"]
    values = [
        float(supervised["top1_accuracy"]),
        float(linear_probe["top1_accuracy"]),
    ]
    annotations = [
        f"{supervised['correct']} / {supervised['total']}",
        f"{linear_probe['correct']} / {linear_probe['total']}",
    ]

    fig, axis = plt.subplots(figsize=FIGURE_SIZE, dpi=DPI)
    bars = axis.bar(
        labels,
        values,
        width=0.55,
        color=["tab:blue", "tab:green"],
        alpha=0.9,
    )
    axis.set_title(
        "Short-baseline CIFAR-10 test accuracy\nnot final benchmark performance",
        fontsize=TITLE_SIZE,
        pad=10,
    )
    axis.set_ylabel("Top-1 accuracy", fontsize=LABEL_SIZE)
    axis.set_ylim(0.0, 1.0)
    axis.grid(axis="y", alpha=0.25)
    axis.tick_params(axis="both", labelsize=TICK_SIZE)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)

    for bar, value, annotation in zip(bars, values, annotations, strict=True):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.025,
            f"{value:.4f}\n{annotation}",
            ha="center",
            va="bottom",
            fontsize=NOTE_SIZE,
        )

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def generate_plots(output_dir: Path = DEFAULT_OUTPUT_DIR) -> list[Path]:
    """Generate all Task 36 short-baseline figures from existing CSV files."""

    output_dir = output_dir.expanduser()
    generated = [
        plot_loss_curve(
            csv_path=REPO_ROOT / "results" / "logs" / "cifar10_supervised_short.csv",
            metric_column="train_loss",
            output_path=output_dir / "supervised_short_loss_curve.png",
            title="Supervised short training loss",
            ylabel="Cross-entropy loss",
            color="tab:blue",
        ),
        plot_loss_curve(
            csv_path=REPO_ROOT / "results" / "logs" / "cifar10_simclr_short.csv",
            metric_column="loss",
            output_path=output_dir / "simclr_short_loss_curve.png",
            title="SimCLR short pretraining loss",
            ylabel="NT-Xent loss",
            color="tab:orange",
        ),
        plot_loss_curve(
            csv_path=REPO_ROOT / "results" / "logs" / "cifar10_linear_probe_short.csv",
            metric_column="train_loss",
            output_path=output_dir / "linear_probe_short_loss_curve.png",
            title="Linear probe short training loss",
            ylabel="Cross-entropy loss",
            color="tab:green",
        ),
        plot_test_accuracy(
            supervised_eval_csv=REPO_ROOT / "results" / "tables" / "supervised_short_eval.csv",
            linear_probe_eval_csv=REPO_ROOT / "results" / "tables" / "linear_probe_short_eval.csv",
            output_path=output_dir / "short_baseline_test_accuracy.png",
        ),
    ]
    return generated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate short-baseline training curve figures.")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory where PNG figures will be written.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    generated = generate_plots(output_dir=Path(args.output_dir))
    for path in generated:
        print(path.relative_to(REPO_ROOT))


if __name__ == "__main__":
    main()
