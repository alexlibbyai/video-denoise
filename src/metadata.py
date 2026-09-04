"""
metadata.py

Generate and save metadata describing a pipeline run.
"""

from pathlib import Path
from datetime import datetime
import json

from config import (
    METADATA_DIR,
    WINDOW_MS,
    HOP_MS,
    THRESHOLD_COUNT,
    FREQUENCY_BANDS,
    MIN_FREQ,
    MAX_FREQ,
    ENCODER_TYPE
)


def save_metadata(
    video_file: Path,
    audio_file: Path,
    rms_file: Path,
    plot_file: Path,
    sample_rate: int,
    spike_file: Path,
    raster_file: Path,
    signal,
    rms_df,
    spike_df,
    reservoir_file: Path,
    reservoir_plot: Path,
    reservoir_df,
    readout_file: Path,
    readout_plot: Path,
    readout_df,
    output_audio: Path,
    reconstruction_stats: dict,
    frequency_bands: int,
    min_frequency: int,
    max_frequency: int,
    encoder_type: str,
) -> None:
    """
    Save processing metadata to a JSON file.

    Parameters
    ----------
    video_file : Path
        Original input video.

    audio_file : Path
        Extracted WAV audio file.

    rms_file : Path
        Generated RMS CSV file.

    plot_file : Path
        RMS plot image.

    sample_rate : int
        Audio sample rate in Hz.

    spike_file : Path
        Generated spike CSV file.

    raster_file : Path
        Spike raster plot image.

    signal : numpy.ndarray
        Audio waveform samples.

    rms_df : pandas.DataFrame
        RMS feature data.

    threshold : float
        Spike generation threshold.

    spike_df : pandas.DataFrame
        Generated spike events.
    """

    METADATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    metadata = {
        # Files
        "source_video": video_file.name,
        "audio_file": audio_file.name,
        "rms_file": rms_file.name,
        "plot_file": plot_file.name,
        "spike_file": spike_file.name,
        "raster_file": raster_file.name,
        "readout_file": readout_file.name,
        "readout_plot": readout_plot.name,
        "reservoir_file": reservoir_file.name,
        "reservoir_plot": reservoir_plot.name,
        "readout_file": readout_file.name,
        "readout_plot": readout_plot.name,        

        # Pipeline
        "pipeline_version": "0.1",
        "generated": datetime.now().isoformat(),

        # Audio Settings
        "sample_rate": sample_rate,
        "window_ms": WINDOW_MS,
        "hop_ms": HOP_MS,

        # Audio Statistics
        "duration_seconds": round(
            len(signal) / sample_rate,
            3,
        ),
        "sample_count": int(len(signal)),

        # RMS Statistics
        "frame_count": int(len(rms_df)),
        "min_rms": float(rms_df["rms"].min()),
        "max_rms": float(rms_df["rms"].max()),
        "mean_rms": float(rms_df["rms"].mean()),
        "median_rms": float(rms_df["rms"].median()),

        # Spike Statistics
        "spike_count": len(spike_df),
        "threshold_count": THRESHOLD_COUNT,
        "active_neurons": int(
            spike_df["neuron_id"].nunique()
        ),

        # Readout Statistics
        "readout_samples": len(readout_df),

        "max_activity": int(
            readout_df["activity"].max()
        ),

        "mean_activity": float(
            readout_df["activity"].mean()
        ),

        "median_activity": float(
            readout_df["activity"].median()
        ),

        # Reservoir Statistics
        "reservoir_size": 20,

        "reservoir_spike_count": len(
            reservoir_df
        ),

        "active_reservoir_neurons": int(
            reservoir_df["neuron_id"].nunique()
        ),

        # Reconstruction

        "reconstructed_audio":
            output_audio.name,

        "reconstruction_method":
            reconstruction_stats[
                "reconstruction_method"
            ],

        "output_duration_seconds":
            reconstruction_stats[
                "output_duration_seconds"
            ],

        "output_sample_count":
            reconstruction_stats[
                "output_sample_count"
            ],

        "reconstruction_status":
            reconstruction_stats[
                "status"
            ],   

        "frequency_bands": FREQUENCY_BANDS,
        "min_frequency": MIN_FREQ,
        "max_frequency": MAX_FREQ,                 

        "encoding_method": "band_rms_v1",    

        # Encoding

        "encoding_method": encoder_type,
        "frequency_bands": frequency_bands,
        "min_frequency": min_frequency,
        "max_frequency": max_frequency,         
    }

    output_file = (
        METADATA_DIR /
        f"{video_file.stem}_metadata.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            metadata,
            file,
            indent=4,
        )