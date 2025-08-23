# Face Recognition Attendance System

A desktop application to manage student records and mark attendance using **real-time face recognition**. Built with **Python (Tkinter GUI)**, **OpenCV (LBPH)**, and **MySQL** for persistence. The app includes dedicated modules for **Student**, **Train**, **Face Recognition**, **Attendance**, **Developer**, and **Help**.

---

## ✨ Features

* **Student Management:** Add, update, delete, and search student profiles with photos.
* **Dataset Capture:** Capture multiple face images per student with webcam.
* **Model Training:** Train an **LBPH** face recognizer from the captured dataset.
* **Real-Time Recognition:** Detect and recognize students live and auto-mark attendance.
* **Attendance Log:** Save attendance with date/time; export to CSV.
* **Tkinter UI:** Simple, multi-window interface with buttons for each module.
* **MySQL Backend:** Store student and attendance data in a relational database.
* **Lightweight & Offline:** Runs locally; works without internet after setup.

---

## 🧱 Tech Stack

* **Language:** Python ≥ 3.9
* **GUI:** Tkinter
* **Computer Vision:** OpenCV (Haar Cascade + LBPH)
* **Database:** MySQL (InnoDB)
* **ORM/Driver:** `mysql-connector-python` (or `pymysql`)
* **Other:** `Pillow`, `numpy`, `pandas`

---

## 📁 Project Structure (Suggested)

```
face-recognition-attendance/
├─ app.py                      # Main Tkinter launcher
├─ config.py                   # DB config & constants
├─ requirements.txt
├─ .env                        # DB creds (not committed)
├─ resources/
│  ├─ haarcascades/haarcascade_frontalface_default.xml
│  └─ icons/ ...
├─ data/
│  ├─ dataset/                 # Captured face images (per-ID)
│  ├─ trainer/                 # Trained model file (trainer.yml)
│  └─ attendance/              # Attendance CSV exports
├─ modules/
│  ├─ student.py               # CRUD for students
│  ├─ train.py                 # Training pipeline (LBPH)
│  ├─ face_recognition.py      # Live recognition & marking
│  ├─ attendance.py            # View/export attendance
│  ├─ developer.py             # Developer/about window
│  └─ help.py                  # Help & troubleshooting UI
└─ utils/
   ├─ db.py                    # MySQL connection helpers
   ├─ camera.py                # Webcam helpers
   ├─ detection.py             # Haar cascade detect helpers
   └─ io.py                    # CSV/image I/O utilities
```

> Your existing modules (Student, Train, Face Recognition, Attendance, Developer, Help) map directly to `modules/` above.

---

## 🗄️ Database Schema (MySQL)

```sql
CREATE DATABASE IF NOT EXISTS fr_attendance CHARACTER SET utf8mb4;
USE fr_attendance;

CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  roll_no VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(100) NOT NULL,
  dept VARCHAR(100),
  year VARCHAR(20),
  phone VARCHAR(20),
  email VARCHAR(120),
  photo_count INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS attendance (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  status ENUM('Present','Absent','Late') DEFAULT 'Present',
  marked_at DATETIME NOT NULL,
  session_date DATE NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;
```

---

## 🔧 Installation

### 1) Prerequisites

* Python 3.9+ (3.10 recommended)
* MySQL Server 8.0+
* A working webcam
* OS: Windows 10/11 or Linux (Ubuntu 20.04+)

### 2) Clone & Create Virtual Environment

```bash
git clone <your-repo-url> face-recognition-attendance
cd face-recognition-attendance
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 3) Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**requirements.txt (sample):**

```
opencv-python
numpy
pillow
pandas
mysql-connector-python
python-dotenv
```

### 4) Configure Environment

Create a `.env` file in project root:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=fr_attendance
```

### 5) Initialize Database

* Create the database and tables using the SQL above.
* Update `.env` with your credentials.

### 6) Run the App

```bash
python app.py
```

---

## 🧠 How It Works (Pipeline)

1. **Register Student →** Enter student details (roll no, name, dept...).
2. **Capture Dataset →** App opens webcam and saves \~50–200 cropped face images for that student under `data/dataset/<roll_no>/`.
3. **Train Model →** Read all datasets, compute **LBPH** embeddings, and write model to `data/trainer/trainer.yml`.
4. **Recognize & Mark →** Live camera detects face, predicts ID using LBPH. On confident match (e.g., confidence ≤ 60), marks **Present** with timestamp.
5. **Review Attendance →** View logs by date/student; export CSV.

---

## ▶️ Usage

* **Student Module:** Add/edit/delete students, capture photos.
* **Train Module:** Click *Train* to regenerate `trainer.yml` after any dataset change.
* **Face Recognition:** Start camera → app overlays name/roll no → attendance auto-logs.
* **Attendance Module:** Filter by date/roll no → export to CSV in `data/attendance/`.
* **Developer/Help:** About info and common fixes.

---

## ⚙️ Key Configuration (config.py)

```python
HAAR_CASCADE = 'resources/haarcascades/haarcascade_frontalface_default.xml'
DATASET_DIR = 'data/dataset'
TRAINER_FILE = 'data/trainer/trainer.yml'
ATTENDANCE_DIR = 'data/attendance'
LBPH_PARAMS = dict(radius=1, neighbors=8, grid_x=8, grid_y=8)
RECOG_THRESHOLD = 60  # lower is stricter; tune based on lighting/camera
CAMERA_INDEX = 0
```

---

## 🧪 Sample Code Snippets

🏠 Home Page
## 🎬 Demo
![Face Recognition Demo](college_images/main.png)


👨‍🎓 Student Management
## 🎬 Demo
![Face Recognition Demo](college_images/wp2551980.jpg)


📊 Attendance Sheet
## 🎬 Demo
![Face Recognition Demo](college_images/Attendance.png)

🎥 fill attendance Manually
## 🎬 Demo
![Face Recognition Demo](college_images/app.png)


🎥 Face Recognition in Action
## 🎬 Demo
![Face Recognition Demo](college_images/face.png)

### Face Detection (Haar)

```python
face_cascade = cv2.CascadeClassifier(HAAR_CASCADE)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    roi = gray[y:y+h, x:x+w]
```

### LBPH Training

```python
recognizer = cv2.face.LBPHFaceRecognizer_create(**LBPH_PARAMS)
recognizer.train(images, np.array(labels))
recognizer.save(TRAINER_FILE)
```

### Prediction → Attendance

```python
label, conf = recognizer.predict(roi)
if conf <= RECOG_THRESHOLD:
    mark_attendance(student_id=label)
```

---

## 📊 Attendance CSV Format

```
roll_no,name,status,marked_at,session_date
CS23-001,Ananya Gupta,Present,2025-08-23 10:04:11,2025-08-23
```

---

## 🔐 Privacy & Security

* Store only necessary student data; avoid sensitive identifiers.
* Keep dataset images and `trainer.yml` private.
* Use strong DB password; restrict DB user privileges.
* Consider consent forms for data collection.

---

## 🛠️ Troubleshooting

* **`cv2.error: (-215:Assertion failed) camera...`** → Wrong `CAMERA_INDEX`; try 0/1; ensure camera not used by other apps.
* **`ModuleNotFoundError`** → Activate venv and reinstall `pip install -r requirements.txt`.
* **Images saved but not recognized** → Capture more images (vary angles/lighting); retrain; adjust `RECOG_THRESHOLD`.
* **MySQL `Access denied`** → Check `.env` credentials and user grants.
* **Haar cascade not found** → Verify path in `config.py`.

---

## 🚀 Performance Tips

* Capture 100–200 images per student across lighting/angles.
* Ensure face is centered and well-lit during capture.
* Periodically retrain after adding new students.
* Consider **CLAHE**/histogram equalization on grayscale frames.

---

## 🗺️ Roadmap

* [ ] Multi-camera support
* [ ] Admin login & roles
* [ ] Attendance dashboard with charts
* [ ] CSV import for students
* [ ] Model versioning & backups
* [ ] Optional: Deep-learning embedding (e.g., FaceNet) with SVM classifier

---

## 🤝 Contributing

1. Fork the repo
2. Create feature branch: `git checkout -b feat/my-feature`
3. Commit: `git commit -m "feat: add my-feature"`
4. Push: `git push origin feat/my-feature`
5. Open a PR



---

## 🙏 Acknowledgements

* OpenCV community & docs
* Haar cascade from OpenCV
* Inspiration from standard LBPH attendance demos

---

## 📎 Appendix: Quick Start Commands (Windows)

```bat
py -3 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
set DB_HOST=localhost
set DB_USER=root
set DB_PASSWORD=your_password
set DB_NAME=fr_attendance
python app.py
```

> Replace placeholders as needed. If you already have modules and UI, you can paste this README into your repo and tweak the **Project Structure** and **Config** values accordingly.
