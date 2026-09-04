---
title: Biological Inspiration
description: C. elegans-inspired design principles.
---

## Overview

This project investigates whether principles derived from biological nervous systems can be applied to the problem of video audio denoising.

Rather than relying solely on conventional deep learning approaches, the system explores a neuromorphic architecture based on:

- Spiking Neural Networks (SNNs)
- Liquid State Machines (LSMs)
- Excitatory and inhibitory neural populations
- Synaptic plasticity
- Temporal signal processing
- Connectome-inspired connectivity

The aim is not to perfectly reproduce a biological organism, but rather to investigate whether biologically-inspired computation can contribute to the recovery of useful audio from noisy recordings.

---

## Why Biology?

Many contemporary machine learning systems rely on large-scale optimisation through gradient descent and backpropagation.

Biological nervous systems solve a wide variety of temporal processing tasks using fundamentally different mechanisms:

- Sparse communication through spikes
- Local learning rules
- Recurrent connectivity
- Competition between neurons
- Dynamic network states
- Temporal memory

Auditory perception, sensory integration, and noise filtering occur naturally in biological systems despite severe constraints on energy consumption and computational resources.

This project explores whether some of these principles can be applied to the task of audio denoising.

---

## Why Spiking Neural Networks?

Spiking Neural Networks are often regarded as the third generation of neural network models.

Unlike traditional artificial neural networks, which exchange continuous numerical values between neurons, SNNs communicate using discrete spike events.

This provides several desirable properties:

- Temporal information is represented explicitly
- Computation can be event-driven
- Activity tends to be sparse
- Network dynamics naturally capture time-dependent patterns

These characteristics make SNNs particularly attractive for processing audio signals, which are inherently temporal in nature.

---

## Why Liquid State Machines?

Audio denoising is fundamentally a temporal problem.

The interpretation of a sound at a given moment often depends on events that occurred several milliseconds or even seconds earlier.

Liquid State Machines (LSMs) address this challenge through the use of a recurrent reservoir.

Input spikes stimulate a network of interconnected neurons, generating a rich and continuously evolving internal state known as the *liquid state*. Information is distributed throughout the reservoir and persists for a short period of time, creating a form of temporal memory.

This makes LSMs particularly well suited to:

- Speech processing
- Signal classification
- Event detection
- Temporal sequence modelling
- Audio reconstruction

For these reasons, an LSM was selected as the core computational architecture.

---

## Why C. elegans?

The nematode *Caenorhabditis elegans* is one of the most thoroughly studied organisms in neuroscience.

Several characteristics make it especially interesting from a computational perspective:

- Its nervous system contains approximately 302 neurons.
- The complete connectome has been mapped.
- Connectivity patterns are largely understood.
- The network demonstrates complex behaviour despite its small size.

The existence of a complete neural wiring diagram makes *C. elegans* an attractive source of inspiration for biologically-grounded network design.

However, it is important to acknowledge an important limitation.

---

## Biological Accuracy

This project is **not** a simulation of a *C. elegans* nervous system.

In fact, most neurons within *C. elegans* communicate using graded electrical signals rather than the action-potential-driven spiking behaviour commonly modelled by Spiking Neural Networks.

As a result, a conventional SNN cannot be considered a faithful recreation of the worm's nervous system.

Instead, this project adopts several broader design principles inspired by biological networks:

- Sparse connectivity
- Recurrent organisation
- Excitatory and inhibitory interactions
- Small-world connectivity patterns
- Distributed computation
- Temporal information processing

The project therefore uses *C. elegans* as an architectural inspiration rather than as a direct biological template.

---

## Biological Design Principles Used

The reservoir architecture incorporates several mechanisms commonly observed in biological neural systems.

### Excitatory and Inhibitory Populations

Most biological nervous systems contain a mixture of excitatory and inhibitory neurons.

To reflect this behaviour, the reservoir is divided into:

- Approximately 80% excitatory neurons
- Approximately 20% inhibitory neurons

This balance helps regulate activity and prevents runaway excitation.

### Lateral Inhibition

Lateral inhibition introduces competition between neighbouring neurons.

When one neuron becomes active, nearby neurons are temporarily suppressed.

This mechanism encourages:

- Sparse coding
- Feature selectivity
- Reduced redundancy

and may improve the separation of useful signal components from background noise.

### Synaptic Delays

Biological neural communication is not instantaneous.

The introduction of variable synaptic delays allows information to propagate through the reservoir over different timescales.

This creates additional temporal structure and increases the memory capacity of the network.

### Synaptic Plasticity

Real nervous systems continuously adapt to experience.

To investigate similar behaviour, this project explores:

- STDP (Spike-Timing-Dependent Plasticity)
- ReSuMe supervised learning

These mechanisms provide biologically-inspired alternatives to conventional backpropagation.

---

## Working Hypothesis

The central hypothesis of this project is:

> A biologically-inspired Liquid State Machine, incorporating excitatory and inhibitory populations, temporal spike encoding, synaptic plasticity, and connectome-inspired connectivity patterns, can learn useful representations of noisy audio signals and recover an improved audio waveform.

The remainder of this project explores that hypothesis through implementation, experimentation, and quantitative evaluation.