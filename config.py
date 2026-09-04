"""
config.py

Central project configuration.
"""

from pathlib import Path

# ----------------------------------
# Directories
# ----------------------------------

BASE_DIR = Path(__file__).parent

INPUT_DIR = BASE_DIR / "data" / "input"
AUDIO_DIR = BASE_DIR / "data" / "audio"
FEATURE_DIR = BASE_DIR / "data" / "features"

PLOT_DIR = BASE_DIR / "results" / "plots"
METADATA_DIR = BASE_DIR / "data" / "metadata"

SPIKE_DIR = BASE_DIR / "data" / "spikes"

READOUT_DIR = BASE_DIR / "data" / "readout"

# ----------------------------------
# Audio Settings
# ----------------------------------

SAMPLE_RATE = 16000
CHANNELS = 1

# ----------------------------------
# RMS Encoder
# ----------------------------------

WINDOW_MS = 20
HOP_MS = 10
ENCODER_TYPE = "rms"

# -------------------------------------------------
# Spectral Encoding
# -------------------------------------------------

FREQUENCY_BANDS = 16

MIN_FREQ = 50
MAX_FREQ = 8000
THRESHOLDS_PER_BAND = 4

# ----------------------------------
# Reservoir
# ----------------------------------

RESERVOIR_DIR = BASE_DIR / "data" / "reservoir"

RESERVOIR_SIZE = 20

INPUT_CONNECTIVITY = 0.5
RESERVOIR_CONNECTIVITY = 0.2

NEURON_THRESHOLD = 1.0

EXCITATORY_RATIO = 0.8
INHIBITORY_RATIO = 0.2

CONNECTION_PROBABILITY = 0.10

MIN_DELAY_MS = 1
MAX_DELAY_MS = 15

# ----------------------------------
# Spike Encoding
# ----------------------------------

THRESHOLD_COUNT = 4

# -------------------------------------------------
# Reconstruction
# -------------------------------------------------

OUTPUT_DIR = BASE_DIR / "data" / "output"