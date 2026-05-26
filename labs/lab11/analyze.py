import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import datetime


sns.set_theme(style="whitegrid")

CHARTS_DIR = "charts"
os.makedirs(CHARTS_DIR, exist_ok=True)


def load_events(filepath: str) -> pd.DataFrame:
    """Load newline-delimited JSON events from `filepath` into a DataFrame.

    The function looks for `resultTime`, `event_time` or `timestamp` fields
    and converts them to a unified `timestamp` column. It also extracts
    hour, day_of_week, date and minute when timestamp is available.
    """
    records = []
    with open(filepath, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            records.append(rec)

    df = pd.DataFrame(records)
    if df.empty:
        return df

    if "resultTime" in df.columns:
        df["timestamp"] = pd.to_datetime(df["resultTime"], errors="coerce")
    elif "event_time" in df.columns:
        df["timestamp"] = pd.to_datetime(df["event_time"], errors="coerce")
    elif "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    if "timestamp" in df.columns:
        df["hour"] = df["timestamp"].dt.hour
        df["day_of_week"] = df["timestamp"].dt.day_name()
        df["date"] = df["timestamp"].dt.date
        df["minute"] = df["timestamp"].dt.minute

    return df


def plot_events_per_hour(df: pd.DataFrame) -> None:
    """Plot number of events per hour and save the figure to CHARTS_DIR.

    Expects `df` to contain an `hour` column (integers 0-23). If not,
    the function will attempt to create it from a `timestamp` column.
    """
    if df.empty:
        print("DataFrame is empty — nothing to plot.")
        return

    if "hour" not in df.columns:
        if "timestamp" in df.columns:
            df = df.copy()
            df["hour"] = pd.to_datetime(df["timestamp"], errors="coerce").dt.hour
        else:
            print("No 'hour' or 'timestamp' column found — cannot plot.")
            return

    hourly = (
        df.groupby("hour")
        .size()
        .reset_index(name="event_count")
        .sort_values("hour")
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=hourly, x="hour", y="event_count", color="blue", ax=ax)
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Number of Events")
    ax.set_title("Motion Events by Hour of Day")
    fig.tight_layout()

    out_path = os.path.join(CHARTS_DIR, "events_per_hour.png")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Saved plot to {out_path}")


def plot_latency_distribution(df: pd.DataFrame) -> None:
    """Plot the distribution of `pipeline_latency_ms` and save the figure.

    If the required column is missing the function will print a message and exit.
    """
    if "pipeline_latency_ms" not in df.columns:
        print("Skipping latency chart: 'pipeline_latency_ms' column not found.")
        return

    if df.empty:
        print("DataFrame is empty — nothing to plot.")
        return

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(data=df, x="pipeline_latency_ms", kde=True, color="green", ax=ax)
    ax.set_xlabel("Pipeline Latency (ms)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Pipeline Latency")
    fig.tight_layout()

    out_path = os.path.join(CHARTS_DIR, "latency_distribution.png")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Saved latency distribution plot to {out_path}")


def plot_heatmap(df: pd.DataFrame) -> None:
    """Create a day×hour heatmap of event counts and save it to CHARTS_DIR.

    Expects `df` to contain `day_of_week` and `hour` columns (or `timestamp`).
    """
    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    if df.empty:
        print("DataFrame is empty — nothing to plot.")
        return

    if "day_of_week" not in df.columns or "hour" not in df.columns:
        if "timestamp" in df.columns:
            tmp = df.copy()
            tmp["day_of_week"] = pd.to_datetime(tmp["timestamp"], errors="coerce").dt.day_name()
            tmp["hour"] = pd.to_datetime(tmp["timestamp"], errors="coerce").dt.hour
            df = tmp
        else:
            print("Skipping heatmap: required 'day_of_week' or 'hour' column not found.")
            return

    pivot = (
        df.groupby(["day_of_week", "hour"])  # type: ignore[arg-type]
        .size()
        .reset_index(name="count")
    )

    heat = pivot.pivot(index="day_of_week", columns="hour", values="count")
    heat = heat.fillna(0)

    # Ensure rows are ordered by day_order and columns are 0..23
    heat = heat.reindex(day_order).fillna(0)
    all_hours = list(range(24))
    # convert columns to int if they are not
    heat.columns = [int(c) for c in heat.columns]
    heat = heat.reindex(columns=all_hours, fill_value=0)

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(
        heat.astype(int),
        cmap="YlOrRd",
        annot=True,
        fmt="d",
        linewidths=0.5,
        ax=ax,
    )
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("")
    ax.set_title("Motion Events: Hour × Day of Week")
    fig.tight_layout()

    out_path = os.path.join(CHARTS_DIR, "heatmap_hour_day.png")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Saved heatmap to {out_path}")


def plot_latency_over_time(df: pd.DataFrame) -> None:
    """Scatter plot of `pipeline_latency_ms` over time and save the figure.

    The function requires both `pipeline_latency_ms` and `timestamp` columns.
    """
    if "pipeline_latency_ms" not in df.columns or "timestamp" not in df.columns:
        print("Skipping latency-over-time chart: required columns not found.")
        return

    if df.empty:
        print("DataFrame is empty — nothing to plot.")
        return

    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(
        df["timestamp"],
        df["pipeline_latency_ms"],
        alpha=0.5,
        s=15,
        color="purple",
    )
    ax.set_xlabel("Time")
    ax.set_ylabel("Pipeline Latency (ms)")
    ax.set_title("Pipeline Latency Over Time")
    plt.xticks(rotation=45)
    fig.tight_layout()

    out_path = os.path.join(CHARTS_DIR, "latency_over_time.png")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Saved latency-over-time plot to {out_path}")


def plot_events_over_time(df: pd.DataFrame) -> None:
    """Plot event counts over time (by minute) and save the figure.

    This is a lightweight time-series plot aggregating events per minute.
    """
    if "timestamp" not in df.columns:
        print("Skipping events-over-time chart: 'timestamp' column not found.")
        return

    if df.empty:
        print("DataFrame is empty — nothing to plot.")
        return

    tmp = df.copy()
    tmp["timestamp"] = pd.to_datetime(tmp["timestamp"], errors="coerce")
    tmp = tmp.dropna(subset=["timestamp"])
    if tmp.empty:
        print("No valid timestamps — skipping events-over-time chart.")
        return

    # Aggregate by minute
    tmp["ts_min"] = tmp["timestamp"].dt.floor("T")
    series = tmp.groupby("ts_min").size().reset_index(name="count")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(series["ts_min"], series["count"], marker="o", linestyle="-", color="tab:blue")
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of Events")
    ax.set_title("Events Over Time (per minute)")
    plt.xticks(rotation=45)
    fig.tight_layout()

    out_path = os.path.join(CHARTS_DIR, "events_over_time.png")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Saved events-over-time plot to {out_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "data/motion_events.jsonl"

    print(f"Loading events from: {filepath}")
    df = load_events(filepath)
    print(f"Loaded {len(df)} events")

    if df.empty:
        print("No data found — please run the pipeline first.")
        sys.exit(1)

    plot_events_per_hour(df)
    plot_latency_distribution(df)
    plot_events_over_time(df)
    plot_heatmap(df)
    plot_latency_over_time(df)

    print(f"All charts saved to {CHARTS_DIR}")
