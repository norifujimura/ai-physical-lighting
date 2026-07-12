# Development Sprints

This document tracks the development progress of the project.

---

## Sprint 0 — Project Setup
**Status:** ✅ Complete

### Goal
Create the initial project structure.

### Completed
- Created GitHub repository
- Added README
- Set up FastAPI
- Created frontend and backend folders

---

## Sprint 1 — FastAPI Basics
**Status:** ✅ Complete

### Goal
Understand the FastAPI application structure.

### Completed
- GET /
- GET /health
- Swagger UI (/docs)

### Lessons Learned
- FastAPI automatically converts Python dictionaries to JSON.
- Static files should be served separately from API endpoints.
- Keep endpoints small and focused.

---

## Sprint 2 — Analyse API
**Status:** ✅ Complete

### Goal
Create the first POST endpoint.

### Completed
- POST /analyse
- Return dummy scene analysis

---

## Sprint 3 — Frontend
**Status:** 🟡 In Progress

### Goal
Serve the frontend through FastAPI.

### Current Tasks
- Serve index.html
- Configure static files
- Connect JavaScript

---

## Sprint 4 — Frontend ↔ Backend

### Goal
Call the analyse endpoint from JavaScript.

---

## Sprint 5 — Camera

### Goal
Capture an image from the webcam.

---

## Sprint 6 — Scene Analysis

### Goal
Estimate scene brightness and dominant colour.

---

## Sprint 7 — Lighting Engine

### Goal
Convert scene analysis into lighting decisions.

---

## Sprint 8 — DMX Output

### Goal
Control a real lighting fixture.

---

## Sprint 9 — MVP Demo

### Goal
Complete the full interaction pipeline.

Camera
↓

Scene Analysis
↓

Lighting Decision
↓

DMX
↓

Physical Lighting