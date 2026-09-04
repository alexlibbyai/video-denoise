---
title: IAF PSC Alpha Neuron Model
description: Mathematical foundations, biological motivation and implementation details of the iaf_psc_alpha neuron model.
---

## Overview

At the heart of the Video Denoise system is the `iaf_psc_alpha` neuron model.

This model was selected because it provides a realistic compromise between biological plausibility and computational efficiency, making it well suited to large-scale spiking neural network simulations.

The model forms the basis of:

- Input populations
- Reservoir neurons
- Readout neurons
- Temporal information processing

throughout the denoising pipeline.

---

## What Is A Spiking Neuron?

Unlike conventional artificial neural networks, where neurons exchange continuous numerical values, spiking neural networks communicate through discrete events known as spikes.

A neuron integrates incoming signals over time.

When the membrane potential rises above a threshold value:

1. A spike is emitted
2. The membrane potential is reset
3. A refractory period begins

This produces behaviour that more closely resembles biological nervous systems.

---

## Integrate-And-Fire Models

The Integrate-And-Fire family of neuron models is among the most widely used approaches in computational neuroscience.

The basic principle is simple:

- Inputs arrive through synapses
- Membrane potential accumulates
- Threshold crossing triggers a spike
- The neuron resets

Despite its simplicity, this behaviour is capable of producing rich temporal dynamics when incorporated into recurrent networks.

---

## Why iaf_psc_alpha?

The project uses:

```text
iaf_psc_alpha
```

rather than a simpler Leaky Integrate-and-Fire implementation.

The key difference is the use of alpha-shaped post-synaptic currents.

Rather than producing an instantaneous effect, incoming spikes generate a current that:

- Gradually rises
- Peaks
- Decays smoothly

This creates more realistic temporal behaviour and improves the network's ability to process time-dependent signals such as speech and environmental sounds.

---

## Alpha-Shaped Post-Synaptic Currents

When a pre-synaptic neuron emits a spike, the resulting post-synaptic current follows an alpha-function profile.

Conceptually, the current behaves as:

```text
Spike
  │
  ▼

 Current
    /\
   /  \
  /    \
 /      \
/        \____

            Time
```

This behaviour more closely reflects the dynamics observed in biological synapses than an instantaneous impulse.

---

## Membrane Dynamics

The neuron continuously integrates incoming synaptic currents.

The membrane potential evolves according to:

```text
dV/dt
```

where:

- incoming excitatory inputs increase activity
- incoming inhibitory inputs suppress activity
- leakage gradually returns the neuron toward its resting state

If the membrane potential exceeds the firing threshold:

```text
V > V_threshold
```

the neuron generates a spike.

---

## Neuron Parameters

Initial experiments will use the following values:

| Parameter | Value |
|------------|--------|
| Membrane Time Constant | 20 ms |
| Threshold Voltage | -55 mV |
| Reset Voltage | -70 mV |
| Excitatory Synaptic Time Constant | 2 ms |
| Inhibitory Synaptic Time Constant | 5 ms |
| Refractory Period | 2 ms |

These values will serve as the baseline configuration during early development.

Future experiments may investigate parameter sensitivity and optimisation.

---

## Excitatory And Inhibitory Behaviour

The reservoir contains both:

### Excitatory Neurons

These neurons increase the probability of downstream activity.

Their role is to propagate information through the network.

### Inhibitory Neurons

These neurons suppress downstream activity.

Their role is to:

- Regulate firing rates
- Prevent runaway excitation
- Encourage sparse representations
- Support competition between neurons

A mixture of both populations is essential for stable reservoir behaviour.

---

## Advantages For Audio Processing

Audio signals are inherently temporal.

The state of a waveform at one moment depends strongly on previous activity.

The `iaf_psc_alpha` model offers several advantages:

- Explicit temporal dynamics
- Natural integration of incoming events
- Compatibility with synaptic delays
- Support for recurrent processing
- Efficient simulation in NEST

These characteristics align well with the requirements of audio denoising and signal reconstruction.

---

## Relationship To The Reservoir

Within the Liquid State Machine architecture, individual neuron accuracy is less important than collective dynamics.

The role of the neuron model is therefore to provide:

- Temporal integration
- Non-linear behaviour
- Event-based communication
- Rich internal dynamics

These interactions generate the liquid state that ultimately enables reconstruction of the target audio signal.

---

## Working Hypothesis

The working hypothesis for this project is:

> The temporal dynamics provided by iaf_psc_alpha neurons will improve the reservoir's ability to represent noisy audio signals and preserve information relevant to waveform reconstruction.

The impact of this design choice will be evaluated through objective audio metrics, spike-train analysis, and reconstruction quality measurements.
