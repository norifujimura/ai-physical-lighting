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