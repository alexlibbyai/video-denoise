"""
run_pipeline.py

Main project pipeline.

Usage:
    python run_pipeline.py

Pipeline:

    Video
      ↓
    Audio Extraction
      ↓
    RMS Feature Generation
      ↓
    RMS Visualisation
      ↓
    Metadata Export
"""

from pathlib import Path

from config import (
    INPUT_DIR,
    AUDIO_DIR,
    FEATURE_DIR,
    PLOT_DIR,
    METADATA_DIR,
    SPIKE_DIR,
    READOUT_DIR,
    OUTPUT_DIR,
    FREQUENCY_BANDS,
    MIN_FREQ,
    MAX_FREQ,
    ENCODER_TYPE
)

from src.metadata import save_metadata

from src.reservoir.reservoir import (
    run_reservoir,
)

from src.reservoir.plot_reservoir import (
    create_reservoir_plot,
)

from src.readout.readout import (
    generate_readout,
)

from src.readout.plot_readout import (
    create_readout_plot,
)

from src.audio.audio_extract import extract_audio

from src.features.plot_rms import create_rms_plot
from src.features.spike_generator import generate_spikes
from src.features.plot_raster import create_raster_plot

from src.encoding.rms_encoder import (
    load_audio,
    calculate_rms,
    calculate_band_rms,
    save_csv,
)

from src.reconstruction.reconstruct_signal import (
    reconstruct_signal,
)


SUPPORTED_VIDEO_TYPES = (
    "*.mp4",
    "*.mov",
    "*.avi",
    "*.mkv",
)


def discover_videos() -> list[Path]:
    """
    Find all supported video files.
    """

    videos = []

    for pattern in SUPPORTED_VIDEO_TYPES:
        videos.extend(INPUT_DIR.glob(pattern))

    return sorted(videos)


def process_video(video_file: Path) -> None:
    """
    Process a single video file.
    """

    print(f"Processing: {video_file.name}")
    
    #
    # Stage 1
    #
    audio_file = extract_audio(video_file)

    #
    # Stage 2
    #
    sample_rate, signal = load_audio(audio_file)

    if ENCODER_TYPE == "rms":

        rms_df = calculate_rms(
            signal,
            sample_rate,
        )

    elif ENCODER_TYPE == "band_rms":

        rms_df = calculate_band_rms(
            signal,
            sample_rate,
        )

    else:

        raise ValueError(
            f"Unsupported encoder type: "
            f"{ENCODER_TYPE}"
        )

    rms_file = save_csv(
        rms_df=rms_df,
        audio_path=audio_file,
    )

    #
    # Stage 3
    #
    plot_file = create_rms_plot(
        signal=signal,
        sample_rate=sample_rate,
        rms_df=rms_df,
        audio_path=audio_file,
    )

    #
    # Stage 4
    #
    spike_df, spike_file = generate_spikes(
        rms_df=rms_df,
        audio_path=audio_file,
    )

    raster_file = create_raster_plot(
        spike_df=spike_df,
        audio_path=audio_file,
    )

    #
    # Stage 6
    #
    reservoir_df, reservoir_file = (
        run_reservoir(
            spike_df=spike_df,
            audio_path=audio_file,
        )
    )

    #
    # Stage 7
    #
    reservoir_plot = (
        create_reservoir_plot(
            reservoir_df=reservoir_df,
            audio_path=audio_file,
        )
    )

    #
    # Stage 8
    #
    readout_df, readout_file = (
        generate_readout(
            reservoir_df=reservoir_df,
            audio_path=audio_file,
        )
    )

    #
    # Stage 9
    #
    readout_plot = (
        create_readout_plot(
            readout_df=readout_df,
            audio_path=audio_file,
        )
    )

    #
    # Stage 10
    #
    output_audio, reconstruction_stats = (
        reconstruct_signal(
            readout_df=readout_df,
            audio_path=audio_file,
            sample_rate=sample_rate,
        )
    )

    #
    # Stage 10
    #   
    save_metadata(
        video_file=video_file,
        audio_file=audio_file,
        rms_file=rms_file,
        plot_file=plot_file,
        sample_rate=sample_rate,
        spike_file=spike_file,
        raster_file=raster_file,
        signal=signal,
        rms_df=rms_df,
        spike_df=spike_df,
        reservoir_file=reservoir_file,
        reservoir_plot=reservoir_plot,
        reservoir_df=reservoir_df,
        readout_file=readout_file,
        readout_plot=readout_plot,
        readout_df=readout_df,
        output_audio=output_audio,
        reconstruction_stats=reconstruction_stats,
        frequency_bands=FREQUENCY_BANDS,
        min_frequency=MIN_FREQ,
        max_frequency=MAX_FREQ,
        encoder_type=ENCODER_TYPE,        
    )

    print("✓ Processing complete")



def main() -> None:

    print("\nVideo Denoise Pipeline v0.1")
    print("-" * 60)

    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    FEATURE_DIR.mkdir(parents=True, exist_ok=True)
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    SPIKE_DIR.mkdir(parents=True, exist_ok=True)
    READOUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    videos = discover_videos()

    if not videos:
        print(
            "\nNo videos found in:\n"
            f"{INPUT_DIR}"
        )
        return

    print(
        f"\nFound {len(videos)} "
        f"video(s) to process\n"
    )

    for video in videos:
        process_video(video)

    print("=" * 60)
    print("Pipeline complete")
    print("=" * 60)


if __name__ == "__main__":
    main()
