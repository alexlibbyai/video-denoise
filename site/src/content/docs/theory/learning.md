---
title: Learning Mechanisms
description: STDP, ReSuMe and biologically-inspired learning strategies employed within the network.
---

## Overview

Learning is one of the defining characteristics of biological nervous systems.

Rather than relying exclusively on global optimisation algorithms such as backpropagation, biological neural networks adapt through local interactions between neurons and synapses.

This project explores whether biologically-inspired learning mechanisms can contribute to the problem of audio denoising.

Two approaches are investigated:

- Spike-Timing-Dependent Plasticity (STDP)
- ReSuMe (Remote Supervised Method)

Together, these mechanisms provide a framework for both unsupervised and supervised learning within the spiking neural network.

---

## Why Not Backpropagation?

Most modern machine learning systems are trained using backpropagation.

While highly effective, backpropagation has several limitations when compared to biological nervous systems:

- Requires global error signals
- Depends on differentiable operations
- Is difficult to apply directly to spike-based computation
- Has limited biological plausibility

The objective of this project is not to compete directly with deep learning systems, but rather to investigate alternative approaches inspired by neuroscience.

---

## Learning Within The Architecture

Learning occurs primarily in two locations:

```text
Input Layer
      │
      ▼
LSM Reservoir
      │
      ▼
Readout Layer
```

Reservoir learning is performed using:

```text
STDP
```

Readout learning is performed using:

```text
ReSuMe
```

This separation allows the contribution of each learning mechanism to be evaluated independently.

---

## Spike-Timing-Dependent Plasticity

Spike-Timing-Dependent Plasticity (STDP) is a biologically-inspired learning rule observed in many neural systems.

The central idea is simple:

> The relative timing of spikes determines whether a connection is strengthened or weakened.

---

## Long-Term Potentiation

If a pre-synaptic neuron consistently fires shortly before a post-synaptic neuron:

```text
Pre Spike
      │
      ▼
Post Spike
```

the connection becomes stronger.

This process is known as:

```text
Long-Term Potentiation (LTP)
```

The network effectively learns that the activity of the first neuron helps predict activity in the second neuron.

---

## Long-Term Depression

If a post-synaptic neuron fires before the pre-synaptic neuron:

```text
Post Spike
      │
      ▼
Pre Spike
```

the connection becomes weaker.

This process is known as:

```text
Long-Term Depression (LTD)
```

Connections that do not contribute useful predictive information are gradually reduced.

---

## Conceptual STDP Curve

The behaviour of STDP can be visualised as:

```text
Weight Change

   +
   │\
   │ \
   │  \
   │   \
---┼----\------------- Time Difference
   │     \
   │      \
   │       \
   │        \
   -
```

Positive timing differences strengthen connections.

Negative timing differences weaken connections.

---

## STDP Within The Reservoir

When enabled, STDP allows the Liquid State Machine reservoir to adapt its internal structure over time.

Potential benefits include:

- Increased feature sensitivity
- Better temporal representations
- Adaptive connectivity
- Improved separation of signal and noise

The impact of STDP will be compared against a static-synapse baseline.

---

## Initial STDP Parameters

Early experiments will use conservative values:

| Parameter | Value |
|------------|--------|
| tau_plus | 20 ms |
| lambda | 0.005 |
| alpha | 1.0 |

These values provide a stable starting point while limiting excessive weight growth.

---

## ReSuMe Learning

While STDP is unsupervised, audio denoising ultimately requires a mechanism that can learn desired outputs.

For this purpose, the project employs:

```text
ReSuMe
```

or:

```text
Remote Supervised Method
```

---

## What Is ReSuMe?

ReSuMe is a supervised learning algorithm designed specifically for spiking neural networks.

The method compares:

```text
Desired Spike Train
```

with:

```text
Actual Spike Train
```

and adjusts synaptic weights accordingly.

The objective is to make the output neuron produce spikes that more closely match the target pattern.

---

## Training Strategy

The denoising problem requires paired data:

```text
Noisy Audio
```

and

```text
Clean Audio
```

The process is:

```text
Clean Audio
       │
       ▼
Encoder
       │
       ▼
Target Spike Train

Noisy Audio
       │
       ▼
Reservoir
       │
       ▼
Output Spike Train
```

ReSuMe attempts to minimise the difference between the output and target spike trains.

---

## Why ReSuMe?

Several characteristics make ReSuMe attractive for this project:

- Designed for spike-based learning
- Supports temporal information
- Biologically motivated
- Compatible with reservoir computing
- Produces interpretable spike outputs

It provides a more natural learning mechanism for SNNs than adapting conventional gradient-based techniques.

---

## Static Versus Adaptive Learning

The project investigates several configurations.

### Static Reservoir

```text
Fixed Weights
```

Advantages:

- Simplicity
- Reproducibility
- Fast experimentation

---

### STDP Reservoir

```text
Reservoir Weights Adapt
```

Advantages:

- Temporal adaptation
- Greater biological realism

---

### STDP + ReSuMe

```text
Adaptive Reservoir
+
Supervised Readout
```

Advantages:

- Feature extraction
- Output optimisation
- Improved reconstruction potential

---

## Experimental Comparisons

Several learning configurations will be evaluated.

| Experiment | STDP | ReSuMe |
|------------|------|---------|
| Baseline | No | No |
| A | Yes | No |
| B | No | Yes |
| C | Yes | Yes |

This enables the contribution of each learning mechanism to be measured independently.

---

## Evaluation Criteria

Learning effectiveness will be assessed using:

### Audio Metrics

- Signal-to-Noise Ratio (SNR)
- Segmental SNR
- RMSE
- Correlation

### Spike Metrics

- Victor-Purpura Distance
- van Rossum Distance

### Computational Metrics

- Runtime
- Memory Usage
- Training Stability

---

## Biological Plausibility

Neither STDP nor ReSuMe perfectly replicates biological learning.

However, both provide mechanisms that operate closer to biological principles than traditional backpropagation.

In combination with recurrent spiking dynamics, they allow the project to investigate how biologically-inspired learning influences audio reconstruction performance.

---

## Working Hypothesis

The central learning hypothesis of this project is:

> Combining adaptive reservoir dynamics through STDP with supervised readout training through ReSuMe will produce richer neural representations and improve audio reconstruction quality compared with static synaptic configurations.

The validity of this hypothesis will be evaluated through controlled experiments and quantitative performance measurements.