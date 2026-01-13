import cv2
import os
from yolo_plate import hide_plate

INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"

MODE = input("blur yoxsa white? ")

if MODE not in ["blur", "white"]:
    MODE = "blur"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, filename)

    img = cv2.imread(input_path)
    if img is None:
        print(f"Oxuna bilmədi: {filename}")
        continue

    result = hide_plate(img, MODE)
    cv2.imwrite(output_path, result)

    print(f"Hazırdır: {filename}")

print("Bütün şəkillər emal olundu ✅")
