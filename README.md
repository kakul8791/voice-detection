# 🎧 Audio Authenticity Detector

A full-stack web application that analyzes uploaded audio files and predicts whether the audio is **REAL or FAKE**, along with a confidence score.

This project includes a **working REST API backend** and a **simple frontend UI**, making it suitable for hackathons, demos, and evaluation platforms.

---

## 🚀 Features

- Upload audio files (`.mp3`, `.wav`)
- Detect audio authenticity (REAL / FAKE)
- Confidence score for prediction
- REST API using FastAPI
- Simple frontend for testing
- Easily deployable on Render / Railway

---

## 🧠 How It Works (Logic)

1. User uploads an audio file from the frontend
2. Frontend sends the file to backend using `multipart/form-data`
3. Backend validates the file and reads audio bytes
4. Audio is analyzed using authenticity logic
5. API returns:
   - Prediction (REAL / FAKE)
   - Confidence score
   - Processing time

> ⚠️ Note  
> This version uses **mock analysis logic** for stability and smooth deployment.  
> The architecture is designed so real ML / DeepFake detection models can be plugged in later.

---

## 📁 Project Structure

