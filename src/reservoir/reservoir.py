"""
reservoir.py

Tiny reservoir MVP.
"""

from pathlib import Path

import numpy as np
import pandas as pd

from config import (
    RESERVOIR_DIR,
    RESERVOIR_SIZE,
    INPUT_CONNECTIVITY,
    RESERVOIR_CONNECTIVITY,
    NEURON_THRESHOLD,
)


def run_reservoir(
    spike_df: pd.DataFrame,
    audio_path: Path,
):
    """
    Run a simple reservoir simulation.

    Returns
    -------
    reservoir_df, output_file
    """

    RESERVOIR_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Reservoir state

    potentials = np.zeros(
        RESERVOIR_SIZE
    )

    # Input weights

    input_weights = np.random.rand(
        RESERVOIR_SIZE
    )

    input_mask = (
        np.random.rand(RESERVOIR_SIZE)
        < INPUT_CONNECTIVITY
    )

    input_weights *= input_mask

    # Reservoir weights

    reservoir_weights = np.random.rand(
        RESERVOIR_SIZE,
        RESERVOIR_SIZE,
    ) * 0.2

    reservoir_mask = (
        np.random.rand(
            RESERVOIR_SIZE,
            RESERVOIR_SIZE
        )
        < RESERVOIR_CONNECTIVITY
    )

    reservoir_weights *= reservoir_mask

    reservoir_spikes = []

    previous_spikes = np.zeros(
        RESERVOIR_SIZE
    )

    grouped = spike_df.groupby(
        "timestamp_ms"
    )

    for timestamp, _ in grouped:

        potentials += input_weights

        potentials += (
            reservoir_weights
            @ previous_spikes
        )

        current_spikes = (
            potentials >= NEURON_THRESHOLD
        ).astype(int)

        active_neurons = np.where(
            current_spikes == 1
        )[0]

        for neuron_id in active_neurons:
            reservoir_spikes.append(
                {
                    "timestamp_ms": timestamp,
                    "neuron_id": int(neuron_id),
                }
            )

        potentials[
            current_spikes == 1
        ] = 0

        previous_spikes = (
            current_spikes
        )

    reservoir_df = pd.DataFrame(
        reservoir_spikes
    )

    output_file = (
        RESERVOIR_DIR
        /
        f"{audio_path.stem}_reservoir.csv"
    )

    reservoir_df.to_csv(
        output_file,
        index=False,
    )

    return (
        reservoir_df,
        output_file,
    )