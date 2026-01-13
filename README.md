# 🚗 YOLO License Plate Blur Project

Bu layihə şəkillərdə avtomobil nömrələrini **YOLO (You Only Look Once)** modeli vasitəsilə avtomatik aşkar edir və onları **blur** və ya **ağ (white)** rənglə gizlədir.

Layihə əvvəlcə **lokal mühitdə test** olunmaq üçün hazırlanıb və sonradan asanlıqla **Telegram bot**, **API** və ya **web app**-ə çevrilə bilər.

---

## ✨ Xüsusiyyətlər

* 📷 Birdən çox şəkil ilə işləyir (batch processing)
* 🤖 YOLOv8 əsaslı nömrə aşkarlanması
* 🔒 Nömrəni gizlətmə modları:

  * `blur`
  * `white`
* 🎯 Confidence threshold (yalnız etibarlı tapıntılar)
* 🧩 Modular dizayn (Telegram-a hazır struktur)

---

## 📁 Folder Strukturu

```
yolo_plate_project/
│
├── yolo_plate.py              # Əsas YOLO logic
├── test_local.py              # Lokal test scripti
├── license_plate_detector.pt  # YOLO model faylı
├── input_images/              # Giriş şəkilləri
└── output_images/             # Nəticə şəkilləri
```

---

## ⚙️ Quraşdırma

### 1️⃣ Repository-ni klonla

```bash
git clone https://github.com/USERNAME/yolo-plate-blur.git
cd yolo-plate-blur
```

### 2️⃣ Virtual environment (tövsiyə olunur)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Lazımi paketləri yüklə

```bash
pip install ultralytics opencv-python
```

---

## ▶️ Lokal Test

1. `input_images/` qovluğuna şəkillər əlavə et
2. Terminalda çalışdır:

```bash
python test_local.py
```

3. Sorğu gələndə:

```
blur yoxsa white?
```

4. Nəticələr `output_images/` qovluğunda olacaq

---

## 🧠 Texniki Detallar

* **Model:** YOLOv8 (license plate trained)
* **Confidence threshold:** 0.5
* **Image processing:** OpenCV
* **Design approach:** Logic-first, platform-independent

---

## 🚀 Gələcək Planlar

* [ ] Telegram bot inteqrasiyası
* [ ] REST API (FastAPI)
* [ ] Öz dataset ilə re-training
* [ ] Docker support

---

## 👨‍💻 Müəllif

**Ilkin Mammadov**
UA / Data / AI / Computer Vision learner

---

## 📄 License

Bu layihə tədris və şəxsi istifadə üçün açıqdır.
