"""
audio_extract.py

Extract audio from a video file and save it as a WAV file.

Usage:
    python src/audio_extract.py path/to/video.mp4

Output:
    data/audio/<video_name>.wav
"""

from pathlib import Path
import subprocess
import sys


OUTPUT_DIR = Path("data/audio")


def extract_audio(video_path: Path) -> Path:
    """
    Extract audio from a video file using FFmpeg.

    Parameters
    ----------
    video_path : Path
        Input video file.

    Returns
    -------
    Path
        Path to the extracted WAV file.
    """

    if not video_path.exists():
        raise FileNotFoundError(
            f"Input video file does not exist:\n{video_path}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_path = OUTPUT_DIR / f"{video_path.stem}.wav"

    command = [
        "ffmpeg",
        "-y",                  # overwrite existing file
        "-i",
        str(video_path),
        "-vn",                 # no video
        "-acodec",
        "pcm_s16le",           # 16-bit PCM
        "-ar",
        "16000",               # 16 kHz
        "-ac",
        "1",                   # mono
        str(output_path),
    ]

    print("\n=== Audio Extraction ===")
    print(f"Input : {video_path}")
    print(f"Output: {output_path}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("FFmpeg extraction failed.")

    print("\n✓ Audio extraction complete")

    return output_path


def main() -> None:
    if len(sys.argv) != 2:
        print(
            "\nUsage:\n"
            "    python src/audio_extract.py <video_file>\n"
        )
        sys.exit(1)

    video_path = Path(sys.argv[1])

    try:
        output_path = extract_audio(video_path)

        print("\nGenerated:")
        print(output_path)

    except Exception as exc:
        print(f"\nERROR: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()