# AI Physical Lighting UX

## Vision

AI Physical Lighting is an AI-assisted lighting design system that helps people explore meaningful relationships between space, light, and human activity.

The goal is not to automate lighting, but to create a creative partner that observes a space, proposes interpretations, and inspires new lighting ideas.

---

# Target Users

## Lighting Designers

### Goals

- Explore new lighting ideas.
- Quickly test alternative lighting behaviours.
- Discover unexpected interpretations of a space.

### Success

"I found an idea I would not have created myself."

---

## Artists & Creative Technologists

### Goals

- Prototype interactive installations.
- Explore AI as an observer rather than a controller.
- Create feedback loops between physical space and AI.

### Success

"The AI became part of the artwork."

---

## Venue Technicians

### Goals

- Configure the system quickly.
- Operate it reliably during rehearsals or exhibitions.

### Success

"The system is easy to operate."

---

# Core Design Principles

## AI is a creative collaborator.

The AI should inspire ideas rather than replace the designer.

---

## Humans remain the creative director.

The designer decides which observations and lighting proposals are meaningful.

---

## The AI explains observations.

The system should expose how it interprets the current space.

---

## Interaction should encourage exploration.

The interface should invite experimentation rather than optimisation.

---

# User Journey

## Step 1 — Observe

The camera captures the current space.

↓

The AI generates an observation.

Example:

- The room feels calm.
- Attention is concentrated near the entrance.
- Two people appear to be interacting.

---

## Step 2 — Interpret

The designer reviews the observation.

Possible actions:

- Accept
- Edit
- Ignore
- Ask the AI to observe differently

---

## Step 3 — Define Intention

The AI proposes a lighting intention.

Examples:

- Support concentration
- Increase tension
- Encourage gathering
- Calm the atmosphere

The user can modify or replace this intention.

---

## Step 4 — Render

The lighting engine converts the intention into light.

Initially:

- Screen Renderer

Later:

- DMX
- Smart Lighting
- Projection

---

## Step 5 — Observe Again

The AI observes the updated space.

The system becomes a continuous feedback loop.

---

# Human–AI Conversation

Unlike conventional lighting software, interaction is primarily conversational.

The designer does not directly manipulate RGB values.

Instead, they collaborate with the AI through observations and intentions.

Examples:

Designer

> Observe only audience behaviour.

AI

> Most visitors remain near the entrance.

Designer

> Ignore the audience. Focus on the architecture.

AI

> The ceiling structure dominates the visual scene.

Designer

> Suggest lighting that supports quiet contemplation.

AI

> A slow transition towards cool, low-intensity light may reinforce that atmosphere.

---

# Functional Requirements

The UX suggests the following core features.

## Observation

- Camera input
- AI observation
- Observation history

---

## Prompt Workspace

- Prompt presets
- Prompt editor
- Additional instructions

---

## Lighting Intention

- AI-generated intention
- Human editing
- Version history

---

## Renderer

- Screen Renderer
- DMX Renderer
- Future output devices

---

## Feedback Loop

- Continuous observation
- Continuous interpretation
- Continuous lighting adaptation

---

# MVP

The first MVP should demonstrate one complete interaction loop.

```
Camera
    ↓
AI Observation
    ↓
Lighting Intention
    ↓
Screen Renderer
    ↓
Camera
```

The objective is not technical completeness, but to demonstrate a meaningful collaboration between AI, humans, and physical space.

---

# Future Questions

This project intentionally leaves several questions open.

- What should the AI observe?
- What kinds of observations inspire designers?
- Should different observation styles exist?
- How should users edit AI observations?
- When should the AI explain its reasoning?
- How can feedback loops remain surprising without becoming repetitive?

These questions are considered part of the creative research rather than implementation details.

# MVP

The first implementation validates one complete interaction loop.

Camera

↓

Observation

↓

Lighting Intention

↓

Screen Renderer

↓

Camera