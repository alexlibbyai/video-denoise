"""
rms_encoder.py

Compute RMS energy from a WAV file and save the results as CSV.

Usage:
    python src/rms_encoder.py data/audio/example.wav

Output:
    data/features/example_rms.csv
"""

import sys
import numpy as np
import pandas as pd

from pathlib import Path
from scipy.io import wavfile
from scipy.signal import spectrogram

from config import (
    WINDOW_MS, 
    HOP_MS,
    FREQUENCY_BANDS, 
    MIN_FREQ, 
    MAX_FREQ
)


OUTPUT_DIR = Path("data/features")


def calculate_rms(signal: np.ndarray, sample_rate: int) -> pd.DataFrame:
    """
    Calculate RMS values using a sliding window.

    Parameters
    ----------
    signal : np.ndarray
        Audio waveform.
    sample_rate : int
        Samples per second.

    Returns
    -------
    pd.DataFrame
        Timestamp/RMS pairs.
    """

    window_size = int(sample_rate * WINDOW_MS / 1000)
    hop_size = int(sample_rate * HOP_MS / 1000)

    timestamps = []
    rms_values = []

    for start in range(0, len(signal) - window_size, hop_size):
        end = start + window_size

        frame = signal[start:end]

        rms = np.sqrt(np.mean(frame.astype(np.float64) ** 2))

        timestamp_ms = (start / sample_rate) * 1000

        timestamps.append(round(timestamp_ms, 2))
        rms_values.append(rms)

    return pd.DataFrame(
        {
            "timestamp_ms": timestamps,
            "rms": rms_values,
        }
    )


def load_audio(audio_path: Path) -> tuple[int, np.ndarray]:
    """
    Load WAV audio.

    Returns
    -------
    sample_rate, signal
    """

    sample_rate, signal = wavfile.read(audio_path)

    # Convert stereo to mono if necessary
    if signal.ndim > 1:
        signal = signal.mean(axis=1)

    return sample_rate, signal


def save_csv(rms_df: pd.DataFrame, audio_path: Path) -> Path:
    """
    Save RMS values as CSV.
    """

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / f"{audio_path.stem}_rms.csv"

    rms_df.to_csv(output_file, index=False)

    return output_file


def calculate_band_rms(
    signal,
    sample_rate,
):
    """
    Calculate RMS energy per frequency band.
    """

    frequencies, times, spectrum = spectrogram(
        signal,
        fs=sample_rate,
        nperseg=int(sample_rate * 0.02),
        noverlap=int(sample_rate * 0.01),
    )

    band_edges = np.linspace(
        MIN_FREQ,
        MAX_FREQ,
        FREQUENCY_BANDS + 1,
    )

    data = {
        "timestamp_ms": times * 1000,
    }

    for i in range(FREQUENCY_BANDS):

        low = band_edges[i]
        high = band_edges[i + 1]

        mask = (
            (frequencies >= low)
            &
            (frequencies < high)
        )

        band_power = spectrum[mask]

        rms = np.sqrt(
            np.mean(
                band_power ** 2,
                axis=0
            )
        )

        data[f"band_{i+1}"] = rms

    return pd.DataFrame(data)


def main() -> None:
    if len(sys.argv) != 2:
        print(
            "\nUsage:\n"
            "    python src/rms_encoder.py <audio.wav>\n"
        )
        sys.exit(1)

    audio_path = Path(sys.argv[1])

    if not audio_path.exists():
        print(f"\nERROR: File not found:\n{audio_path}")
        sys.exit(1)

    print("\n=== RMS Encoding ===")
    print(f"Input: {audio_path}")

    sample_rate, signal = load_audio(audio_path)

    print(f"Sample Rate: {sample_rate:,} Hz")
    print(f"Samples: {len(signal):,}")

    rms_df = calculate_band_rms(signal, sample_rate)

    output_file = save_csv(rms_df, audio_path)

    print(f"Frames: {len(rms_df):,}")
    print(f"Output: {output_file}")
    print("✓ RMS encoding complete")


if __name__ == "__main__":
    main()