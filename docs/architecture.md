# Architecture

## Overview

This project follows a simple modular architecture designed for rapid prototyping.

The frontend provides a lightweight user interface.

FastAPI acts as the application server and coordinates communication between the frontend and backend modules.

The long-term goal is to connect computer vision with physical lighting through a clear and maintainable pipeline.

---

## Current Architecture

```text
Browser
    │
    ▼
FastAPI (app.py)
    │
    ├── GET /
    ├── GET /health
    └── POST /analyse
```

At the current stage, the `/analyse` endpoint returns a fixed JSON response.

The camera, scene analysis and DMX output will be added incrementally in later sprints.

---

## Planned Interaction Pipeline

```text
Camera
    │
    ▼
Scene Analysis
    │
    ▼
Lighting Engine
    │
    ▼
DMX Output
    │
    ▼
Physical Lighting
```

This interaction pipeline represents the overall direction of the project rather than the current implementation.

---

## Project Structure

```text
ai-physical-lighting/

├── app.py                  # FastAPI application
├── backend/
│   ├── vision.py
│   ├── lighting.py
│   └── dmx.py
│
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
│
├── docs/
│   ├── architecture.md
│   ├── sprints.md
│   └── mvp.md
│
├── README.md
└── requirements.txt
```

---

## Module Responsibilities

### Frontend

Responsible for:

- User interface
- User interaction
- Sending API requests
- Displaying analysis results

---

### FastAPI

Responsible for:

- Routing
- API endpoints
- Coordinating backend modules
- Returning responses to the frontend

---

### Vision

Responsible for:

- Capturing images
- Scene analysis
- Feature extraction

(Currently under development.)

---

### Lighting Engine

Responsible for converting scene analysis into lighting decisions.

(Currently under development.)

---

### DMX

Responsible only for communicating with physical lighting hardware.

(Currently under development.)

---

## Design Principles

The architecture follows the project-wide principles:

- Keep modules independent.
- Prefer simple implementations.
- Avoid unnecessary abstractions.
- Build incrementally.
- Keep hardware-specific code isolated.
- Treat AI as one component of a larger interactive system.

---

## Future Expansion

Future versions are expected to include:

- Continuous camera capture
- OpenCV-based scene analysis
- AI-assisted lighting decisions
- Multiple lighting fixtures
- Moving-head fixtures
- Real-time interaction

These features will be added without changing the overall architecture.