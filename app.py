from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pathlib import Path
from fastapi import FastAPI

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

    return {

        "status": "success",

        "scene": {

            "brightness": "unknown",

            "dominant_color": "unknown",

        },

    }
