import base64
import json
import re
import requests
import cv2
from pathlib import Path
from datetime import datetime


def capture_frame():
    """Capture a single frame from the default USB camera."""

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise RuntimeError("Could not open camera.")

    for _ in range(30):
        success, frame = camera.read()

    camera.release()

    if not success:
        raise RuntimeError("Could not capture frame.")

    return frame


def save_frame(frame):

    """Save a captured frame as a JPEG image."""

    output_dir = Path("assets/captures")

    output_dir.mkdir(parents=True, exist_ok=True)

    filename = datetime.now().strftime("capture_%Y%m%d_%H%M%S.jpg")

    filepath = output_dir / filename

    cv2.imwrite(str(filepath), frame)

    return filepath


def estimate_brightness(frame):

    """Estimate the average brightness of an image.

    Returns:

        float: Average grayscale intensity (0–255).

    """

    # Turn to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    brightness = gray.mean()

    return float(brightness)


def observe_image(image_path: str, prompt: str) -> dict:
    """Generate a VLM observation of an image using Ollama.
    
    Args:
        image_path: Path to the image file.
        prompt: Prompt for the vision model.
    
    Returns:
        dict: Parsed JSON observation from the model, or None if parsing fails.
    """
    with open(image_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")

    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": prompt,
            "images": [image_b64],
            "stream": False,
        },
    )

    observation_text = res.json()["response"]
    match = re.search(r"\{.*\}", observation_text, re.DOTALL)

    if match:
        observation = json.loads(match.group())
    else:
        observation = None

    return observation