# Deepfake Detection Using Deep Learning

A deep learning–based system to detect **fake vs real images and videos** using **transfer learning (ResNet18)**.  
The project leverages computer vision and deep learning techniques and provides a **Flask-based web application** for real-time deepfake detection.

---

## 📌 Project Overview

Deepfake technology enables the creation of highly realistic manipulated media, posing serious threats to digital security and misinformation.  
This project aims to **identify deepfake images and videos** by analyzing facial features using a deep learning model.

The system uses a **pretrained ResNet18 model**, fine-tuned for binary classification (Real/Fake), and is deployed via a web interface for easy user interaction.

---

## 🧠 Key Features

- Deepfake detection using **ResNet18 (Transfer Learning)**
- Face extraction using **Haar Cascade**
- Image preprocessing and data augmentation
- Real-time prediction via **Flask REST API**
- Web interface for uploading images/videos
- Supports both **image and video inputs**

---

## 🏗️ System Architecture

1. User uploads an image or video via web interface  
2. Backend processes the file using Flask  
3. Frames are extracted (for videos)  
4. Faces are detected using Haar Cascade  
5. Preprocessed faces are passed to the ResNet18 model  
6. Model predicts **Real / Fake**  
7. Result is displayed on the frontend  

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Deep Learning & Computer Vision
- PyTorch
- Torchvision
- Transfer Learning (ResNet18)
- OpenCV
- Haar Cascade Face Detection

### Web Technologies
- Flask
- HTML
- CSS
- JavaScript

### Dataset
- FaceForensics++ (FF++)

---

## 📊 Model Details

- **Model:** ResNet18 (pretrained on ImageNet)
- **Task:** Binary Classification (Real vs Fake)
- **Input Size:** 224 × 224
- **Evaluation Metrics:**  
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  
  - Confusion Matrix  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/deepfake-detection.git
cd deepfake-detection

![WhatsApp Image 2025-11-17 at 16 04 00_bb75d39d](https://github.com/user-attachments/assets/a59d252b-0c9b-4a25-a017-91d368b55d0a)

