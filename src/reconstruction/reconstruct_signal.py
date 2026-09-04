"""
reconstruct_signal.py

Convert reservoir readout activity into a crude audio waveform.

Version:
    Reconstruction MVP v0.1

Purpose:
    Complete the end-to-end prototype by generating a WAV file
    from reservoir activity.

Notes:
    This is NOT intended to perform denoising yet.

    The goal is simply:

        Audio
          ↓
        RMS
          ↓
        Spikes
          ↓
        Reservoir
          ↓
        Readout
          ↓
        WAV

    so that we have a complete system which can later be improved
    through experiments and learning.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.io.wavfile import write

from config import OUTPUT_DIR


def reconstruct_signal(
    readout_df: pd.DataFrame,
    audio_path: Path,
    sample_rate: int,
):
    """
    Generate a crude waveform from reservoir activity.

    Parameters
    ----------
    readout_df : pandas.DataFrame
        Reservoir readout activity.

    audio_path : Path
        Original WAV file.

    sample_rate : int
        Audio sample rate.

    Returns
    -------
    tuple
        (output_file, reconstruction_stats)
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_file = (
        OUTPUT_DIR
        / f"{audio_path.stem}_reconstructed.wav"
    )

    # ------------------------------
    # Validation
    # ------------------------------

    if readout_df.empty:

        print(
            "WARNING: Readout dataframe is empty."
        )

        silent_audio = np.zeros(
            sample_rate,
            dtype=np.int16,
        )

        write(
            output_file,
            sample_rate,
            silent_audio,
        )

        return (
            output_file,
            {
                "reconstruction_method":
                    "activity_interpolation_v1",
                "status":
                    "empty_readout",
                "output_duration_seconds":
                    1.0,
            },
        )

    # ------------------------------
    # Clean Data
    # ------------------------------

    readout_df = (
        readout_df
        .dropna()
        .sort_values(
            "timestamp_ms"
        )
        .copy()
    )

    timestamps = (
        readout_df["timestamp_ms"]
        .to_numpy(dtype=float)
        / 1000.0
    )

    activity = (
        readout_df["activity"]
        .to_numpy(dtype=float)
    )

    # ------------------------------
    # Handle Single Sample
    # ------------------------------

    if len(activity) == 1:

        activity = np.array(
            [activity[0], activity[0]]
        )

        timestamps = np.array(
            [0.0, 0.01]
        )

    # ------------------------------
    # Normalise
    # ------------------------------

    activity_max = np.max(activity)

    if activity_max > 0:

        activity = (
            activity
            / activity_max
        )

    else:

        activity = np.zeros_like(
            activity
        )

    # ------------------------------
    # Duration
    # ------------------------------

    duration = float(
        timestamps.max()
    )

    duration = max(
        duration,
        0.1,
    )

    sample_count = int(
        duration * sample_rate
    )

    sample_count = max(
        sample_count,
        sample_rate // 10,
    )

    # ------------------------------
    # Interpolate
    # ------------------------------

    output_times = np.linspace(
        0,
        duration,
        sample_count,
    )

    reconstructed = np.interp(
        output_times,
        timestamps,
        activity,
    )

    # ------------------------------
    # Light smoothing
    # ------------------------------

    if len(reconstructed) > 5:

        kernel = np.ones(5) / 5

        reconstructed = np.convolve(
            reconstructed,
            kernel,
            mode="same",
        )

    # ------------------------------
    # Convert to int16
    # ------------------------------

    reconstructed = np.clip(
        reconstructed,
        -1.0,
        1.0,
    )

    audio_data = (
        reconstructed * 32767
    ).astype(np.int16)

    write(
        output_file,
        sample_rate,
        audio_data,
    )

    stats = {
        "reconstruction_method":
            "activity_interpolation_v1",

        "output_duration_seconds":
            round(
                duration,
                3,
            ),

        "output_sample_count":
            int(len(audio_data)),

        "max_activity":
            float(activity_max),

        "status":
            "success",
    }

    return (
        output_file,
        stats,
    )