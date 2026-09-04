---
title: Experiment Log
description: Chronological record of experiments, configurations, observations and findings.
---

# Experiment Log

## Overview

This page serves as the primary experimental record for the Video Denoise project.

All significant experiments, observations, design changes, successes, failures, and lessons learned are documented here.

The objective is to maintain a transparent and reproducible research process.

Experiments are recorded chronologically and include:

- Objectives
- Configurations
- Parameters
- Results
- Observations
- Conclusions
- Future actions

Where possible, links to code, data, figures, and supporting documentation will also be provided.

---

## Experiment Template

Future experiments should follow the structure below.

### Experiment ID

```text
EXP-XXX
```

### Objective

What question is being investigated?

### Configuration

Reservoir size, encoder settings, learning parameters, and experimental conditions.

### Metrics

Quantitative and qualitative measurements.

### Results

Observed outcomes.

### Observations

Interesting behaviour, anomalies, limitations, or unexpected findings.

### Conclusion

Summary of findings.

### Next Steps

Recommended follow-up experiments.

---

# Experiment Timeline

---

## EXP-000

### Title

Project Foundation

### Date

September 2026

### Objective

Establish the project infrastructure and documentation environment.

### Configuration

Development environment:

- Python virtual environment
- Astro + Starlight documentation site
- GitHub Pages deployment
- GitHub Actions continuous deployment
- Initial project documentation

### Results

Successfully established:

- Project repository
- Documentation structure
- Public website
- Automated deployment pipeline

### Observations

The initial setup phase identified several issues:

- MkDocs was evaluated and ultimately replaced with Astro/Starlight.
- Navigation configuration required restructuring during migration.
- GitHub Actions deployment required workflow debugging.
- Several deployment issues were traced to configuration and file naming errors.

### Conclusion

A stable documentation platform has been established.

The project now has a public-facing research site capable of documenting future development and experimentation.

### Next Steps

Begin implementation of the audio processing pipeline and RMS encoder.

---

## EXP-001

### Title

Encoder Design Investigation

### Status

Planned

### Objective

Define the architecture of the RMS-based audio encoder.

### Research Questions

- How many frequency bands should be used?
- How many threshold neurons are required?
- What spike generation strategy is most appropriate?
- What information is preserved during encoding?

### Proposed Configuration

```text
16 Frequency Bands
×
4 Threshold Neurons

=
64 Input Neurons
```

### Metrics

- Spike density
- Sparsity
- Encoding stability
- Computational cost

### Status

Awaiting implementation.

---

## EXP-002

### Title

Baseline Reservoir

### Status

Planned

### Objective

Evaluate a simple fixed-weight reservoir without learning mechanisms.

### Proposed Configuration

```text
500 Neurons

400 Excitatory
100 Inhibitory

Fixed Weights
Fixed Delays
```

### Metrics

- Reservoir activity
- Firing rate distribution
- Stability
- Reconstruction quality

### Status

Awaiting implementation.

---

## EXP-003

### Title

Variable Delay Reservoir

### Status

Planned

### Objective

Measure the impact of introducing heterogeneous synaptic delays.

### Research Question

Do variable delays improve temporal representation within the reservoir?

### Proposed Delay Range

```text
1 ms - 15 ms
```

### Metrics

- Reservoir richness
- Spike-train diversity
- Reconstruction quality

### Status

Awaiting implementation.

---

## EXP-004

### Title

STDP Reservoir

### Status

Planned

### Objective

Evaluate whether adaptive synapses improve reservoir performance.

### Configuration

```text
STDP Enabled
```

### Metrics

- Weight evolution
- Reservoir dynamics
- Reconstruction quality

### Status

Awaiting implementation.

---

## EXP-005

### Title

STDP + Lateral Inhibition

### Status

Planned

### Objective

Evaluate competition-based encoding within the reservoir.

### Configuration

```text
STDP
+
Lateral Inhibition
```

### Metrics

- Sparsity
- Selectivity
- Signal discrimination

### Status

Awaiting implementation.

---

## EXP-006

### Title

Full Architecture

### Status

Planned

### Objective

Evaluate the complete denoising system.

### Configuration

```text
RMS Encoder
+
LSM Reservoir
+
STDP
+
Variable Delays
+
Lateral Inhibition
+
ReSuMe
```

### Metrics

#### Audio Metrics

- Signal-to-Noise Ratio (SNR)
- Segmental SNR
- RMSE
- Correlation

#### Spike Metrics

- Victor-Purpura Distance
- van Rossum Distance

#### Performance Metrics

- Runtime
- Memory Usage
- Simulation Stability

### Success Criteria

Demonstrate measurable improvement in at least one objective audio quality metric.

### Status

Awaiting implementation.

---

# Open Questions

The following questions remain active areas of investigation.

## Encoding

- Is RMS encoding sufficient?
- Would auditory-inspired filterbanks provide superior representations?
- What is the optimal number of frequency bands?

## Reservoir

- What reservoir size is required?
- How sensitive is performance to connectivity structure?
- Does a small-world topology provide measurable benefits?

## Learning

- How much does STDP contribute?
- Is ReSuMe sufficient for reconstruction?
- Which mechanisms contribute most to denoising performance?

## Evaluation

- Which metrics best capture audio quality improvements?
- How closely do spike metrics correlate with reconstruction quality?

---

# Lessons Learned

This section captures important discoveries made throughout development.

## LL-001

### Documentation Early, Code Later

Establishing architecture and documentation before implementation improved clarity and highlighted several design decisions that might otherwise have emerged during coding.

### Outcome

Continue maintaining documentation alongside development.

---

## LL-002

### Infrastructure Matters

A reliable documentation and deployment pipeline significantly reduces friction when recording progress and sharing results.

### Outcome

Treat documentation as a first-class project component.

---

# Current Focus

The current development priority is:

```text
Audio Processing Pipeline
        ↓
RMS Encoder
        ↓
Spike Generation
```

These components form the sensory interface to the Liquid State Machine and represent the next major implementation milestone.
``