"""
plot_rms.py

Generate a waveform + RMS visualisation.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from config import PLOT_DIR


def create_rms_plot(
    signal,
    sample_rate,
    rms_df,
    audio_path,
):
    """
    Create waveform + RMS plot.

    Parameters
    ----------
    signal : np.ndarray
        Audio samples

    sample_rate : int
        Audio sample rate

    rms_df : pandas.DataFrame
        RMS dataframe

    audio_path : Path
        Source wav file

    Returns
    -------
    Path
        Path to generated PNG
    """

    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = (
        PLOT_DIR /
        f"{audio_path.stem}_rms.png"
    )

    duration = len(signal) / sample_rate

    waveform_time = np.linspace(
        0,
        duration,
        len(signal),
    )

    rms_time = rms_df["timestamp_ms"] / 1000

    plt.figure(figsize=(12, 6))

    plt.plot(
        waveform_time,
        signal,
        linewidth=0.5,
        alpha=0.5,
        label="Waveform"
    )

    plt.plot(
        rms_time,
        rms_df["rms"],
        linewidth=2,
        label="RMS"
    )

    plt.title(
        f"Waveform and RMS Envelope\n{audio_path.stem}"
    )

    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.legend()

    plt.tight_layout()

    plt.savefig(output_file)

    plt.close()

    return output_file