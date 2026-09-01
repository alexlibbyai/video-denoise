---
title: Home
description: Neuromorphic video audio denoising using Liquid State Machines, Spiking Neural Networks, and biologically-inspired learning.
---
 
# Neuromorphic Video Audio Denoising

> A biologically-inspired investigation into audio denoising using Spiking Neural Networks, Liquid State Machines, and C. elegans-inspired connectivity.

---

## Overview

**Video Denoise** is an experimental research project exploring whether biologically-inspired neural computation can be used to recover useful audio from noisy video recordings.

Unlike conventional denoising systems that rely on deep convolutional or transformer-based architectures, this project investigates a neuromorphic approach based on:

- Spiking Neural Networks (SNNs)
- Liquid State Machines (LSMs)
- Temporal spike encoding
- Spike-Timing-Dependent Plasticity (STDP)
- ReSuMe supervised learning
- Excitatory and inhibitory neural populations
- Variable synaptic delays
- Connectome-inspired connectivity patterns

The central question is simple:

> Can a biologically-inspired spiking neural network learn to separate foreground audio from background noise and reconstruct a cleaner waveform?

---

## Research Motivation

Modern audio enhancement systems routinely achieve impressive results using conventional deep learning techniques.

However, biological nervous systems solve temporal processing problems using sparse spikes, recurrent connectivity, competition, and local learning rules rather than backpropagation through massive networks.

This project explores whether those principles can be applied to a practical signal-processing problem:

### Input

Noisy video audio

### Processing

Temporal spike encoding and reservoir computation

### Output

Improved audio reconstructed through spike-based processing

---

## Proposed System Architecture

```text
Video File
    │
    ▼
Audio Extraction
    │
    ▼
RMS-Based Spike Encoding
    │
    ▼
Input Neuron Population
(iaf_psc_alpha)
    │
    ▼
Liquid State Machine Reservoir
    │
    ├── Excitatory Neurons
    ├── Inhibitory Neurons
    ├── STDP Learning
    └── Variable Delays
    │
    ▼
Readout Layer
(ReSuMe / Linear Decoder)
    │
    ▼
Waveform Reconstruction
    │
    ▼
Recovered Audio
    │
    ▼
Video Remuxing
    │
    ▼
Output Video