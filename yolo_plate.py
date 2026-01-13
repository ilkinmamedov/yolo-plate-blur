import cv2
from ultralytics import YOLO

model = YOLO("license_plate_detector.pt")

def hide_plate(img, mode="blur"):
    results = model(img)[0]

    for box, conf in zip(results.boxes.xyxy, results.boxes.conf):
        if conf < 0.5:
            continue

        x1, y1, x2, y2 = map(int, box)
        plate = img[y1:y2, x1:x2]

        if plate.size == 0:
            continue

        if mode == "blur":
            plate = cv2.GaussianBlur(plate, (99, 99), 30)
        elif mode == "white":
            plate[:] = (255, 255, 255)

        img[y1:y2, x1:x2] = plate

    return img
