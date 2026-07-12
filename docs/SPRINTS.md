# Development Sprints

This document tracks the development progress of the project.

Each sprint delivers one small, testable improvement while keeping the software simple, modular, and maintainable.

---

# Sprint 0 — Project Setup

**Status:** ✅ Complete

## Goal

Create the initial project structure.

## Completed

- Created GitHub repository
- Added README
- Added project documentation
- Set up FastAPI
- Created frontend and backend folders

---

# Sprint 1 — FastAPI Basics

**Status:** ✅ Complete

## Goal

Understand the FastAPI application structure.

## Completed

- GET /
- GET /health
- Swagger UI (/docs)

## Lessons Learned

- FastAPI automatically converts Python dictionaries to JSON.
- API endpoints should remain small and focused.
- FastAPI provides interactive API documentation automatically.

---

# Sprint 2 — Analyse API

**Status:** ✅ Complete

## Goal

Create the first API endpoint for scene analysis.

## Completed

- POST /analyse
- Return dummy scene analysis JSON

---

# Sprint 3 — Serve Frontend

**Status:** ✅ Complete

## Goal

Serve the frontend from FastAPI.

## Completed

- Return index.html
- Configure StaticFiles
- Load CSS
- Load JavaScript

---

# Sprint 4 — Frontend ↔ Backend Communication

**Status:** ✅ Complete

## Goal

Connect the frontend to the backend.

## Completed

- Analyse button
- fetch() POST request
- Receive JSON response
- Update the browser UI

---

# Sprint 5 — Camera Capture

**Status:** ✅ Complete

## Goal

Capture a single frame from the USB webcam.

## Completed

- Create capture_frame()
- Integrate camera capture into /analyse
- Verify successful camera access

---

# Sprint 6 — Save Captured Frame

**Status:** ✅ Complete

## Goal

Save captured frames for debugging.

## Completed

- Create save_frame()
- Save images to assets/captures
- Display saved image path
- Verify captured images

## Lessons Learned

- USB cameras require several frames before auto exposure stabilises.
- Saving intermediate outputs greatly simplifies debugging.

---

# Sprint 7 — Brightness Estimation

**Status:** ⬜ Planned

## Goal

Estimate the average scene brightness.

## Planned

- Create estimate_brightness(frame)
- Return brightness in API response
- Display brightness in the frontend

---

# Sprint 8 — Dominant Colour Estimation

**Status:** ⬜ Planned

## Goal

Estimate the dominant scene colour.

## Planned

- Extract dominant RGB colour
- Return colour in API response
- Display colour in the frontend

---

# Sprint 9 — Lighting Engine

**Status:** ⬜ Planned

## Goal

Convert scene analysis into lighting decisions.

## Planned

- Create lighting.py
- Map brightness and colour to lighting state
- Return lighting state

---

# Sprint 10 — DMX Output

**Status:** ⬜ Planned

## Goal

Control a physical lighting fixture.

## Planned

- Connect DMX interface
- Send RGB values
- Verify fixture response

---

# Sprint 11 — MVP Demo

**Status:** ⬜ Planned

## Goal

Complete the first working prototype.

## Success Criteria

```
Camera
    ↓
Capture Frame
    ↓
Scene Analysis
    ↓
Lighting Decision
    ↓
DMX Output
    ↓
Physical Lighting
```

The system demonstrates the complete interaction pipeline using one USB camera and one DMX lighting fixture.