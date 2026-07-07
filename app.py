from fastapi import FastAPI

app = FastAPI(
    title="AI Physical Lighting",
    description="Minimal API for the AI for Physical Experience adaptive lighting prototype.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "AI Physical Lighting",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
