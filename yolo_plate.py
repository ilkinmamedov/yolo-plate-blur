import cv2
import os
from ultralytics import YOLO

# =========================
# CONFIG
# =========================
MODEL_PATH = "license_plate_detector.pt"
CONF_THRESHOLD = 0.6
PADDING = 5

# =========================
# MODEL LOAD (SAFE)
# =========================
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "Model faylı tapılmadı: license_plate_detector.pt"
    )

model = YOLO(MODEL_PATH)


# =========================
# MAIN FUNCTION
# =========================
def hide_plate(img, mode="blur"):
    results = model(img)[0]

    # Əgər heç nə tapılmayıbsa
    if results.boxes is None or len(results.boxes) == 0:
        return img

    for box, conf in zip(results.boxes.xyxy, results.boxes.conf):
        if conf < CONF_THRESHOLD:
            continue

        x1, y1, x2, y2 = map(int, box)

        # Padding (accuracy boost)
        x1 = max(0, x1 - PADDING)
        y1 = max(0, y1 - PADDING)
        x2 = min(img.shape[1], x2 + PADDING)
        y2 = min(img.shape[0], y2 + PADDING)

        plate = img[y1:y2, x1:x2]

        if plate.size == 0:
            continue

        if mode == "blur":
            h, w = plate.shape[:2]
            k = max(15, (w // 2) | 1)  # adaptive kernel
            plate = cv2.GaussianBlur(plate, (k, k), 30)

        elif mode == "white":
            plate[:] = (255, 255, 255)

        img[y1:y2, x1:x2] = plate

    return img
