# AI-Powered Drone Detection 🛸

The AI-Powered Drone Detection project is a full-stack, state-of-the-art solution that leverages artificial intelligence to detect drones in various environments. With the increasing use of drones, there is a growing need to identify unauthorized activity for security. This project addresses that challenge using advanced computer vision (YOLOv8) and a modern user interface.

## 🏗️ Architecture

The project is split into two main components:
1.  **Backend (API)**: A FastAPI server that handles image processing and YOLO inference.
2.  **Frontend (UI)**: A modern React.js dashboard where users can upload images and view detection results.

---

## 🛠️ Project Structure

-   `backend/`: Contains the FastAPI server, utility scripts, and detection logic.
-   `frontend/`: A React + Vite application for the user interface.
-   `model/`: Stores the trained YOLO weight files (e.g., `best.pt`).
-   `test_images/`: A collection of sample images for testing the detection capabilities.

---

## 🚀 Getting Started

To run the project locally, follow these steps:

### 1. Backend Setup
1.  Navigate to the project root.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Start the API: `python backend/main.py`.
4.  The API will be available at `http://localhost:8000`.

### 2. Frontend Setup
1.  Navigate to the `frontend/` directory.
2.  Install dependencies: `npm install`.
3.  Start the development server: `npm run dev`.
4.  Open the app in your browser at `http://localhost:5173`.

---

## ☁️ Deployment Guide (Free Tier)

For a free deployment, we recommend the following:

-   **Frontend**: Host on **Vercel** or **Netlify** (continuous deployment from GitHub).
-   **Backend**: Host on **Render** (via Docker or Python Web Service) or **Hugging Face Spaces** (highly recommended for AI models).

*Detailed deployment instructions can be found in the respective `frontend/` and `backend/` directories.*

---

## 🧠 Methodology and Achievements

-   **Model**: Fine-tuned **YOLOv8** for high-precision drone detection.
-   **Efficiency**: Decoupled architecture allows for independent scaling and real-time processing.
-   **Usability**: Simple drag-and-drop interface for end-users.

## 📜 Conclusion
This project demonstrates the synergy between deep learning and modern web technologies, providing a scalable and user-friendly tool for drone detection and security monitoring.
