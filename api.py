from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
import cv2
import numpy as np
from yolo_plate import hide_plate

app = FastAPI(
    title="License Plate Blur API",
    description="YOLO-based license plate hiding API",
    version="1.0"
)


@app.get("/")
def root():
    return {"status": "API işləyir ✅"}


@app.post("/process-image")
async def process_image(
    file: UploadFile = File(...),
    mode: str = Form("blur")
):
    if mode not in ["blur", "white"]:
        return JSONResponse(
            status_code=400,
            content={"error": "mode yalnız blur və ya white ola bilər"}
        )

    # File → bytes
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Şəkil oxunmadı"}
        )

    try:
        result = hide_plate(img, mode)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

    # OpenCV image → bytes
    success, encoded_img = cv2.imencode(".jpg", result)
    if not success:
        return JSONResponse(
            status_code=500,
            content={"error": "Şəkil encode edilə bilmədi"}
        )

    return StreamingResponse(
        iter([encoded_img.tobytes()]),
        media_type="image/jpeg"
    )
