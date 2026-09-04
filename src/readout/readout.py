"""
readout.py

Generate a simple activity readout from the reservoir.
"""

from pathlib import Path

import pandas as pd

from config import READOUT_DIR


def generate_readout(
    reservoir_df: pd.DataFrame,
    audio_path: Path,
):
    """
    Generate readout activity by counting reservoir spikes
    per timestamp.

    Parameters
    ----------
    reservoir_df : pandas.DataFrame
        Reservoir spike events.

    audio_path : Path
        Source audio file.

    Returns
    -------
    tuple
        (readout_df, readout_file)
    """

    READOUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    readout_df = (
        reservoir_df
        .groupby("timestamp_ms")
        .size()
        .reset_index(name="activity")
    )

    output_file = (
        READOUT_DIR
        / f"{audio_path.stem}_readout.csv"
    )

    readout_df.to_csv(
        output_file,
        index=False,
    )

    return (
        readout_df,
        output_file,
    )