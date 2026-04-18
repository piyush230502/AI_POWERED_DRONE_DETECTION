import io
import os
from pathlib import Path

import numpy as np
import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image
from ultralytics import YOLO

# Environment setup for characters (legacy from original script)
os.environ['LANG'] = 'en_US.UTF-8'
os.environ['LC_ALL'] = 'en_US.UTF-8'

app = FastAPI(title="AI Powered Drone Detection API")

# Configure CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your React app's URL (e.g., ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Robust model path resolution
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "best.pt"

# Load the trained YOLO model
try:
    if not MODEL_PATH.exists():
        # Fallback to local 'best.pt' if not found in model/
        MODEL_PATH = Path('best.pt')
    
    model = YOLO(str(MODEL_PATH))
except Exception as e:
    print(f"Error loading model from {MODEL_PATH}: {e}")
    # Initialize without model for now to allow app to start, 
    # but actual predictions will fail
    model = None

@app.get("/")
async def root():
    return {"message": "Drone Detection API is running. use /predict for inference."}

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded. Check server logs.")

    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File uploaded is not an image.")

    try:
        # Read image
        contents = await image.read()
        img = Image.open(io.BytesIO(contents)).convert("RGB")

        # Perform inference
        results = model(img)
        
        # Get the first result and plot bounding boxes
        result = results[0]
        result_image = result.plot()  # BGR format from YOLO/OpenCV plotter

        # Convert BGR (OpenCV) to RGB (PIL) if necessary
        # result.plot() returns image in BGR format
        result_image_rgb = Image.fromarray(result_image[..., ::-1])

        # Save result to BytesIO
        output = io.BytesIO()
        result_image_rgb.save(output, format="JPEG")
        output.seek(0)

        return StreamingResponse(output, media_type="image/jpeg")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
