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
    Generate spike events.

    Supports:

    - Single RMS encoding
    - Multi-band RMS encoding
    """

    SPIKE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    spikes = []

    #
    # -----------------------------
    # Single RMS Encoder
    # -----------------------------
    #
    if "rms" in rms_df.columns:

        min_rms = rms_df["rms"].min()
        max_rms = rms_df["rms"].max()

        thresholds = np.linspace(
            min_rms,
            max_rms,
            THRESHOLD_COUNT + 1,
        )[1:]

        for _, row in rms_df.iterrows():

            timestamp = row["timestamp_ms"]
            rms_value = row["rms"]

            for neuron_id, threshold in enumerate(
                thresholds,
                start=1,
            ):

                if rms_value > threshold:

                    spikes.append(
                        {
                            "timestamp_ms": timestamp,
                            "neuron_id": neuron_id,
                        }
                    )

    #
    # -----------------------------
    # Band RMS Encoder
    # -----------------------------
    #
    else:

        band_columns = [
            column
            for column in rms_df.columns
            if column.startswith("band_")
        ]

        if not band_columns:

            raise ValueError(
                "Expected RMS or band_* columns. "
                f"Found: {rms_df.columns.tolist()}"
            )

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
                FREQUENCY_BANDS + 1,
            ):

                band_name = f"band_{band}"

                if band_name not in rms_df.columns:
                    continue

                band_value = row[band_name]

                for (
                    threshold_index,
                    threshold,
                ) in enumerate(
                    thresholds,
                    start=1,
                ):

                    if band_value > threshold:

                        neuron_id = (
                            (
                                band - 1
                            )
                            * THRESHOLDS_PER_BAND
                        ) + threshold_index

                        spikes.append(
                            {
                                "timestamp_ms": timestamp,
                                "neuron_id": neuron_id,
                            }
                        )

    spike_df = pd.DataFrame(spikes)

    output_file = (
        SPIKE_DIR
        / f"{audio_path.stem}_spikes.csv"
    )

    spike_df.to_csv(
        output_file,
        index=False,
    )

    return (
        spike_df,
        output_file,
    )