"""
plot_reservoir.py
"""

import matplotlib.pyplot as plt

from config import PLOT_DIR


def create_reservoir_plot(
    reservoir_df,
    audio_path,
):

    output_file = (
        PLOT_DIR
        /
        f"{audio_path.stem}_reservoir.png"
    )

    plt.figure(
        figsize=(12, 6)
    )

    plt.scatter(
        reservoir_df[
            "timestamp_ms"
        ],
        reservoir_df[
            "neuron_id"
        ],
        marker="|",
        s=50,
    )

    plt.title(
        f"Reservoir Activity\n"
        f"{audio_path.stem}"
    )

    plt.xlabel(
        "Time (ms)"
    )

    plt.ylabel(
        "Reservoir Neuron"
    )

    plt.tight_layout()

    plt.savefig(
        output_file
    )

    plt.close()

    return output_file