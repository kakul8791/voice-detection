from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import base64
import time
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Audio Authenticity API Running"}

@app.post("/detect")
async def detect_audio(file: UploadFile = File(...)):
    start = time.time()

    content = await file.read()
    if len(content) < 100:
        return {
            "success": False,
            "error": "Invalid or empty audio file"
        }

    # 🧠 MOCK ANALYSIS (REALISTIC)
    prediction = random.choice(["Real", "AI Generated"])
    confidence = round(random.uniform(0.82, 0.97), 2)

    return {
        "success": True,
        "prediction": prediction,
        "confidence": confidence,
        "time_taken": round(time.time() - start, 2)
    }
