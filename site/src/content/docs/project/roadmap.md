---
title: Project Roadmap
description: Planned milestones, implementation phases and research objectives.
---

# Project Roadmap

## Overview

The Video Denoise project is being developed incrementally through a series of clearly defined milestones.

This staged approach allows each component of the system to be implemented, tested, documented, and evaluated independently before integration into the larger architecture.

The roadmap is structured around the complete lifecycle of the project:

```text
Research
    ↓
Architecture
    ↓
Implementation
    ↓
Experimentation
    ↓
Evaluation
    ↓
Publication
```

Each phase produces measurable deliverables that contribute to the final denoising system.

---

## Project Status

| Phase | Status |
|---------|---------|
| Repository Setup | ✅ Complete |
| Documentation Platform | ✅ Complete |
| Theory Documentation | ✅ Complete |
| Architecture Definition | 🚧 In Progress |
| RMS Encoder | ⏳ Planned |
| Reservoir Implementation | ⏳ Planned |
| Learning Mechanisms | ⏳ Planned |
| Audio Reconstruction | ⏳ Planned |
| Experimental Evaluation | ⏳ Planned |
| Final Release | ⏳ Planned |

---

## Phase 1: Project Foundation

### Objectives

Establish the project infrastructure and research framework.

### Deliverables

- Git repository
- Documentation website
- GitHub Pages deployment
- Initial project structure
- Research plan
- Architectural documentation

### Success Criteria

- Repeatable development environment
- Public documentation site
- Version-controlled project foundation

### Status

✅ Complete

---

## Phase 2: Audio Processing Pipeline

### Objectives

Develop the preprocessing pipeline responsible for extracting audio from video files.

### Deliverables

- Video ingestion
- Audio extraction
- WAV conversion
- Audio normalisation
- Dataset preparation

### Planned Technologies

- Python
- FFmpeg
- Librosa
- NumPy

### Success Criteria

- Reliable extraction of audio from video
- Consistent output format
- Reproducible preprocessing pipeline

### Status

🚧 In Progress

---

## Phase 3: RMS Encoder

### Objectives

Transform continuous audio signals into spike-based representations.

### Deliverables

- Frame segmentation
- Frequency-band analysis
- RMS feature extraction
- Population coding
- Spike generation
- HDF5 output

### Initial Configuration

```text
16 Frequency Bands
×
4 Threshold Neurons

=
64 Input Neurons
```

### Success Criteria

- Stable spike generation
- Reproducible encoding
- Visualisation of encoded data

### Status

⏳ Planned

---

## Phase 4: Input Layer Implementation

### Objectives

Develop the neural interface connecting encoded spikes to the reservoir.

### Deliverables

- Input neuron population
- iaf_psc_alpha implementation
- Encoder integration
- Spike injection mechanisms

### Success Criteria

- Successful transmission of encoded spikes
- Stable firing behaviour

### Status

⏳ Planned

---

## Phase 5: Reservoir Prototype

### Objectives

Create an initial Liquid State Machine implementation.

### Deliverables

- Recurrent connectivity
- Excitatory neurons
- Inhibitory neurons
- Basic monitoring and analysis tools

### Initial Configuration

```text
500 Reservoir Neurons

400 Excitatory
100 Inhibitory
```

### Success Criteria

- Stable reservoir dynamics
- Observable temporal memory
- Meaningful neural activity patterns

### Status

⏳ Planned

---

## Phase 6: Synaptic Delays And Inhibition

### Objectives

Introduce additional biological mechanisms.

### Deliverables

- Variable synaptic delays
- Lateral inhibition
- Activity regulation
- Competitive dynamics

### Success Criteria

- Sparse neural representations
- Controlled activity levels
- Improved reservoir diversity

### Status

⏳ Planned

---

## Phase 7: STDP Integration

### Objectives

Investigate unsupervised learning within the reservoir.

### Deliverables

- STDP synapses
- Weight adaptation
- Learning analysis
- Connectivity visualisation

### Success Criteria

- Stable learning behaviour
- Adaptation of synaptic structure
- Measurable changes in network dynamics

### Status

⏳ Planned

---

## Phase 8: Readout Layer And ReSuMe

### Objectives

Develop supervised learning for audio reconstruction.

### Deliverables

- Readout neurons
- ReSuMe training
- Target spike generation
- Performance monitoring

### Success Criteria

- Learnable output representation
- Improved reconstruction quality
- Convergent training behaviour

### Status

⏳ Planned

---

## Phase 9: Audio Reconstruction

### Objectives

Convert neural activity into a usable audio waveform.

### Deliverables

- Signal reconstruction
- Waveform generation
- Audio export pipeline

### Success Criteria

- Intelligible output audio
- Consistent reconstruction process
- Quantitative evaluation support

### Status

⏳ Planned

---

## Phase 10: End-To-End Video Processing

### Objectives

Integrate all components into a complete denoising system.

### Deliverables

```text
Video
    ↓
Audio Extraction
    ↓
Encoding
    ↓
Reservoir Processing
    ↓
Reconstruction
    ↓
Video Remuxing
```

### Success Criteria

- Process complete video files
- Generate enhanced output videos
- Reproducible execution pipeline

### Status

⏳ Planned

---

## Phase 11: Experimental Evaluation

### Objectives

Measure the effectiveness of the proposed architecture.

### Evaluation Metrics

#### Audio Metrics

- Signal-to-Noise Ratio (SNR)
- Segmental SNR
- Root Mean Square Error (RMSE)
- Correlation

#### Spike Metrics

- Victor-Purpura Distance
- van Rossum Distance

#### Computational Metrics

- Runtime
- Memory Usage
- Simulation Stability

### Success Criteria

- Complete experimental dataset
- Reproducible results
- Statistical comparison of configurations

### Status

⏳ Planned

---

## Phase 12: Public Release

### Objectives

Prepare the project for portfolio and research presentation.

### Deliverables

- Complete documentation
- Published results
- Architecture diagrams
- Experimental reports
- Source code release

### Success Criteria

- Fully documented repository
- Public GitHub Pages site
- Reproducible research workflow

### Status

⏳ Planned

---

## Planned Experimental Progression

The project will compare increasingly sophisticated reservoir configurations.

### Experiment 1

```text
Static Reservoir
```

Baseline performance.

### Experiment 2

```text
Static Reservoir
+
Inhibitory Population
```

Evaluate population balance.

### Experiment 3

```text
Static Reservoir
+
Variable Delays
```

Evaluate temporal dynamics.

### Experiment 4

```text
STDP Reservoir
```

Evaluate unsupervised adaptation.

### Experiment 5

```text
STDP
+
Lateral Inhibition
```

Evaluate sparse coding effects.

### Experiment 6

```text
STDP
+
Lateral Inhibition
+
ReSuMe
```

Full architecture.

---

## Definition Of Success

The project will be considered successful if it demonstrates:

- A functioning end-to-end denoising pipeline
- Stable reservoir dynamics
- Meaningful spike-based representations
- Quantitative improvements in at least one audio quality metric
- Reproducible experimental results
- Complete public documentation

The ultimate goal is not necessarily to outperform modern deep learning systems, but to investigate whether biologically-inspired computation can offer useful insights into practical audio processing problems.

---

## Looking Ahead

The immediate focus of development is the implementation of the audio processing pipeline and RMS encoder.

These components will form the sensory foundation of the entire neuromorphic system and provide the first opportunity to evaluate the transformation of audio into spike-based representations.
