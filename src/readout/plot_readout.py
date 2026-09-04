"""
plot_readout.py

Visualise reservoir readout activity.
"""

import matplotlib.pyplot as plt

from config import PLOT_DIR


def create_readout_plot(
    readout_df,
    audio_path,
):
    """
    Generate activity plot.

    Parameters
    ----------
    readout_df : pandas.DataFrame
        Readout activity values.

    audio_path : Path
        Source audio file.

    Returns
    -------
    Path
        Generated PNG.
    """

    output_file = (
        PLOT_DIR
        / f"{audio_path.stem}_readout.png"
    )

    plt.figure(figsize=(12, 4))

    plt.plot(
        readout_df["timestamp_ms"],
        readout_df["activity"],
        linewidth=1.5,
    )

    plt.title(
        f"Readout Activity\n{audio_path.stem}"
    )

    plt.xlabel("Time (ms)")
    plt.ylabel("Activity")

    plt.tight_layout()

    plt.savefig(output_file)

    plt.close()

    return output_file