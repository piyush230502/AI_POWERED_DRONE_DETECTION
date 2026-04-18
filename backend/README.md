# AI Powered Drone Detection - Backend API ⚙️

This is the high-performance FastAPI backend for the Drone Detection project. It integrates a trained **YOLOv8** model to process images and identify drones with high precision.

## 🚀 Key Features
- **FastAPI Core**: Highly performant asynchronous API.
- **YOLOv8 Integration**: Uses the `ultralytics` framework for state-of-the-art object detection.
- **Auto-Docs**: Interactive Swagger UI available at `/docs`.
- **Decoupled Architecture**: Designed to work seamlessly with modern frontends (like React).

## 🛠️ Tech Stack
- **Language**: Python 3.12+
- **API Framework**: FastAPI
- **Model Framework**: Ultralytics (YOLO)
- **Image Processing**: Pillow, OpenCV

## 💻 Getting Started

### 1. Installation
Install the required Python packages:
```bash
uv pip install -r requirements.txt
```

### 2. Run the Server
From the project root directory, run:
```bash
python backend/main.py
```
The server will start at `http://123.0.0.1:8000`.

## 📍 API Endpoints
- `GET /`: Health check.
- `POST /predict`: Accepts an image file and returns the image with bounding boxes drawn over it.

## ☁️ Free Tier Deployment Guide

### Render (Recommended)
1. **GitHub Sync**: Push your code to GitHub.
2. **Create Web Service**: Select your repo on [Render](https://render.com).
3. **Settings**:
   - Runtime: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables: Ensure you add any required model paths or environment settings.

### Hugging Face Spaces
1. **Create a Space**: Select the **Docker** or **Streamlit/Gradio** SDK (or use a simple Python file).
2. **Upload `best.pt`**: Spaces is great because it handles large files and heavy model inference well on their free tier.
