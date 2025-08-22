



# 🎓 Face Recognition Attendance System  

A **Python + OpenCV + Tkinter + MySQL** based project for managing student attendance using Face Recognition. ✨  
This system detects faces, trains a model, and marks attendance automatically.  

---

## 🚀 Features  

- ✅ **Student Management** (Add, Update, Delete in MySQL)  
- ✅ **Capture & store student images** in `data/`  
- ✅ **Train LBPH Face Recognizer** → generates `classifier.xml`  
- ✅ **Real-time Face Recognition** with OpenCV  
- ✅ **Attendance saved** in `Ajay.csv` (Name, ID, Time, Date, Status)  
- ✅ **Beautiful Tkinter GUI** (Help, Developer, Attendance, Exit buttons)  

---

## 🗄️ Database Setup  

   ```sql
   >>>>>>> 6f90ecb
             CREATE DATABASE IF NOT EXISTS face_recognizer;
             USE face_recognizer;

       CREATE TABLE IF NOT EXISTS student (
       Dep VARCHAR(50),
       Course VARCHAR(50),
       Year VARCHAR(20),
       Semester VARCHAR(20),
       Student_id INT PRIMARY KEY,
       Name VARCHAR(100),
       Division VARCHAR(10),
       Roll VARCHAR(20),
       Gender VARCHAR(10),
       Dob VARCHAR(20),
       Email VARCHAR(100),
       Phone VARCHAR(20),
       Address VARCHAR(255),
       Teacher VARCHAR(100),
       PhotoSample VARCHAR(10)
       );
   ```

---
## 📂 Project Structure  

```
📁 Face-Recognition-Attendance-System  
│── main.py  
│── student.py  
│── train.py  
│── face_recognition.py  
│── attendance.py  
│── developer.py  
│── help.py  
│── requirements.txt  
│── haarcascade_frontalface_default.xml  
│── classifier.xml   (auto-generated)  
│── Ajay.csv         (attendance file)  
│
├── 📁 data/             # Captured student images  
├── 📁 college_images/   # GUI related images  
```  

---

## 📂 Tech Stack  

- **Language:** Python 3.x  
- **Libraries:** OpenCV, NumPy, face_recognition, dlib, pandas  
- **Database:** CSV / MySQL  
- **GUI (optional):** Tkinter   

---

## 💻 Getting Started  

### 1️⃣ Clone the repository  
     
   git clone https://github.com/ajayp9/face-recognition-attendance.git
             cd face-recognition-attendance

---
## ▶️ How to Run  

### 1️⃣ Create virtual environment & install requirements:  
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Run the application:  
```bash
python main.py
```

---

## 📖 Usage Flow  

1. 🔹 **Student Details** → Enter & Save  
2. 🔹 **Take Photo Sample** → Captures 100 images → stored in `data/`  
3. 🔹 **Train Data** → Generates `classifier.xml`  
4. 🔹 **Face Detector** → Real-time recognition → Attendance in `Ajay.csv`  
5. 🔹 **Attendance** → Import/Export CSV  

---

## 📸 Project Snapshots  
📸 Project Snapshots

🏠 Home Page
## 🎬 Demo
![Face Recognition Demo](college_images/main.png)


👨‍🎓 Student Management
## 🎬 Demo
![Face Recognition Demo](college_images/wp2551980.jpg)


📊 Attendance Sheet
## 🎬 Demo
![Face Recognition Demo](college_images/Attendance.png)


🎥 Face Recognition in Action
## 🎬 Demo
![Face Recognition Demo](college_images/face.png)
=======
