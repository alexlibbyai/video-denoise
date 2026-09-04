---
title: RMS Audio Encoding
description: Conversion of audio signals into spike-based representations using RMS-derived temporal encoding.
---

## Overview

Before audio can be processed by a Spiking Neural Network, it must first be transformed into a spike-based representation.

This process is known as *encoding*.

The purpose of the encoder is to convert a continuous audio waveform into temporally meaningful spike trains while preserving as much useful information as possible.

Within the Video Denoise system, the encoder acts as the artificial sensory system of the network.

---

## Why Encoding Is Necessary

Audio signals are typically represented as continuously varying amplitudes.

For example:

```text
Waveform
    │
    │    /\      /\
    │   /  \    /  \
    │__/    \__/    \____
    │
    └─────────────────── Time
```

Spiking Neural Networks, however, communicate using discrete spike events.

This creates a mismatch:

```text
Audio Signal
          ≠
Spike Train
```

The encoder bridges this gap by transforming waveform characteristics into spikes that can be processed by the reservoir.

---

## Design Goals

The encoder should:

- Preserve useful information
- Maintain temporal structure
- Produce sparse activity
- Be computationally efficient
- Support biological plausibility
- Integrate naturally with a Liquid State Machine

---

## Why RMS?

Root Mean Square (RMS) energy provides a measure of signal strength over time.

Rather than analysing individual sample values, RMS captures the average energy contained within a short window.

This produces a representation that is:

- More robust to noise
- Less sensitive to individual sample fluctuations
- Computationally inexpensive
- Suitable for spike generation

For audio denoising, signal energy often provides a useful indicator of meaningful sound events.

---

## Encoding Pipeline

The complete encoding process follows the pipeline below:

```text
Audio Waveform
       │
       ▼
Frame Segmentation
       │
       ▼
Frequency Analysis
       │
       ▼
RMS Extraction
       │
       ▼
Threshold Population Coding
       │
       ▼
Spike Generation
       │
       ▼
Input Spike Trains
```

---

## Audio Preprocessing

Input audio is first normalised and resampled.

Initial experiments will use:

| Parameter | Value |
|------------|--------|
| Sample Rate | 16 kHz |
| Channels | Mono |
| Bit Depth | 16 Bit |
| Format | WAV |

These settings provide sufficient quality for speech-focused denoising while reducing computational complexity.

---

## Frame Segmentation

The signal is divided into overlapping windows.

Initial configuration:

| Parameter | Value |
|------------|--------|
| Window Size | 20 ms |
| Hop Size | 10 ms |

This configuration balances:

- Temporal resolution
- Computational cost
- Feature stability

---

## Frequency Analysis

Audio will be separated into multiple frequency bands.

Rather than treating the waveform as a single signal, the encoder analyses energy across different parts of the spectrum.

Initial target:

```text
16 Frequency Bands
```

This approach provides significantly richer information than a single RMS value.

---

## RMS Extraction

For each frequency band and time window:

```text
Band
   │
   ▼
RMS Calculation
   │
   ▼
Energy Estimate
```

The resulting values describe how signal energy changes over time within each frequency region.

---

## Population Coding

Rather than assigning a single neuron to each RMS value, the encoder uses population coding.

Each frequency band is represented by multiple neurons operating at different thresholds.

Example:

| Neuron | Threshold |
|----------|----------|
| N1 | Very Low |
| N2 | Low |
| N3 | Medium |
| N4 | High |

Higher signal energy activates a larger proportion of the population.

This improves robustness and provides a more biologically-inspired representation.

---

## Input Layer Size

The initial encoder design uses:

```text
16 Frequency Bands
×
4 Threshold Neurons

=
64 Input Neurons
```

These neurons form the sensory interface to the reservoir.

---

## Spike Generation

Spike generation is event-driven.

When an RMS value exceeds a neuron's threshold:

```text
Energy > Threshold
```

a spike event is produced.

Conceptually:

```text
Energy
   │
   ▼
Threshold Test
   │
   ├── Below Threshold → No Spike
   │
   └── Above Threshold → Spike
```

The resulting spikes are forwarded into the input population.

---

## Output Representation

Encoded spikes are represented as:

```text
Neuron ID
Timestamp
```

pairs.

Example:

```text
Neuron 12 : 105 ms
Neuron 27 : 107 ms
Neuron 12 : 125 ms
Neuron 41 : 126 ms
```

This format is compatible with NEST simulations and HDF5 storage.

---

## Data Storage

Encoded spike trains will be saved within HDF5 files.

Example structure:

```text
/spikes/input

/neuron_ids
/timestamps
```

Associated metadata includes:

```text
sample_rate
window_size
hop_size
encoder_type
band_count
```

This allows complete reconstruction of the encoded representation for later analysis.

---

## Advantages

The proposed encoder offers several benefits:

- Low computational complexity
- Noise robustness
- Temporal awareness
- Compatibility with reservoir computing
- Biological plausibility
- Straightforward implementation

Most importantly, it provides a controlled and reproducible way to transform audio signals into spike-based representations.

---

## Limitations

The RMS encoder deliberately sacrifices detail in favour of stability.

Some information present in the original waveform will inevitably be lost during encoding.

The success of the project therefore depends on determining whether enough information survives to allow meaningful audio reconstruction.

This represents one of the primary research questions explored by the project.

---

## Working Hypothesis

The working hypothesis for the encoder is:

> An RMS-based population encoder can preserve sufficient temporal and spectral information to allow a Liquid State Machine reservoir to distinguish useful audio content from background noise and support successful waveform reconstruction.

The effectiveness of this hypothesis will be evaluated through audio reconstruction quality, Signal-to-Noise Ratio improvements, and spike-train similarity metrics.