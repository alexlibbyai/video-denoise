"""
spike_generator.py

Convert RMS features to multi-threshold spike trains.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from config import (
    SPIKE_DIR,
    THRESHOLD_COUNT,
    FREQUENCY_BANDS,
    THRESHOLDS_PER_BAND
)


def generate_spikes(
    rms_df: pd.DataFrame,
    audio_path: Path,
):
    """
    Generate spike events using multiple thresholds.
    """

    SPIKE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    spikes = []

    band_columns = [
        c
        for c in rms_df.columns
        if c.startswith("band_")
    ]

    all_band_values = (
        rms_df[band_columns]
        .to_numpy()
        .flatten()
    )

    min_rms = all_band_values.min()
    max_rms = all_band_values.max()

    thresholds = np.linspace(
        min_rms,
        max_rms,
        THRESHOLDS_PER_BAND + 1,
    )[1:]

    for _, row in rms_df.iterrows():

        timestamp = row["timestamp_ms"]

        for band in range(
            1,
            FREQUENCY_BANDS + 1
        ):

            band_value = row[
                f"band_{band}"
            ]

            for (
                threshold_index,
                threshold,
            ) in enumerate(
                thresholds,
                start=1,
            ):

                if (
                    band_value
                    > threshold
                ):

                    neuron_id = (
                        (band - 1)
                        * THRESHOLDS_PER_BAND
                    ) + threshold_index

                    spikes.append(
                        {
                            "timestamp_ms": timestamp,
                            "neuron_id": neuron_id,
                        }
                    )

    spike_df = pd.DataFrame(
        spikes
    )

    output_file = (
        SPIKE_DIR
        /
        f"{audio_path.stem}_spikes.csv"
    )

    spike_df.to_csv(
        output_file,
        index=False,
    )

    return (
        spike_df,
        output_file,
    )