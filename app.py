from backend.vision import capture_frame, estimate_brightness, save_frame, observe_image
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pathlib import Path
from fastapi import FastAPI

DEFAULT_OBSERVATION_PROMPT = "Return JSON with the fields you need for the observation."

app = FastAPI(
    title="AI Physical Lighting",
    description="Minimal API for the AI for Physical Experience adaptive lighting prototype.",
    version="0.1.0",
)

app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static",
)


@app.get("/")
def root():
    return FileResponse(
        Path("frontend") / "index.html"
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyse")
def analyse():

    frame = capture_frame()

    filepath = save_frame(frame)

    brightness = estimate_brightness(frame)

    observation = observe_image(str(filepath), DEFAULT_OBSERVATION_PROMPT)

    return {
        "status": "success",
        "image": str(filepath),
        "scene": {
            "brightness": brightness,
            "dominant_color": "unknown",
            "observation": observation,
        },
    }
