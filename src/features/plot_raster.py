"""
plot_raster.py

Generate a spike raster plot.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from config import PLOT_DIR


def create_raster_plot(
    spike_df,
    audio_path,
):
    """
    Generate spike raster PNG.
    """

    PLOT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = (
        PLOT_DIR /
        f"{audio_path.stem}_raster.png"
    )

    plt.figure(figsize=(12, 4))

    plt.scatter(
        spike_df["timestamp_ms"],
        spike_df["neuron_id"],
        marker="|",
        s=100,
    )

    plt.xlabel("Time (ms)")
    plt.ylabel("Threshold Neuron")
    plt.yticks(
        sorted(
            spike_df["neuron_id"].unique()
        )
    )

    plt.title(
        f"Spike Raster\n{audio_path.stem}"
    )

    plt.tight_layout()

    plt.savefig(output_file)

    plt.close()

    return output_file