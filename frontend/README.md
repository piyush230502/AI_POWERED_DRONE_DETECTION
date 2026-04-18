# AI Powered Drone Detection - Frontend 🛸

This is the modern React.js frontend for the Drone Detection project. It provides a beautiful, responsive user interface for uploading images and viewing AI detection results in real-time.

## 🚀 Key Features
- **Modern UI**: Styled with sleek gradients and interactive buttons.
- **Fast Performance**: Built with **Vite** for near-instant development.
- **Real-time Feedback**: Connects to a FastAPI backend to show YOLO detection results instantly.

## 🛠️ Tech Stack
- **Framework**: React.js
- **Build Tool**: Vite
- **API Client**: Axios

## 💻 Getting Started

### 1. Prerequisites
Ensure you have [Node.js](https://nodejs.org/) installed on your machine.

### 2. Installation
Navigate to the frontend directory and install the dependencies:
```bash
npm install 
```

### 3. Run the Development Server
Start the app locally:
```bash
npm run dev
```
The app will be available at `http://localhost:5173`.

## 🌐 Connecting to the Backend
By default, the frontend is configured to talk to the backend at `http://localhost:8000/predict`. Ensure your backend server is running!

## ☁️ Free Tier Deployment Guide

### Vercel / Netlify (Recommended)
1. **Push your code** to a GitHub repository.
2. **Connect your repo** to [Vercel](https://vercel.com) or [Netlify](https://www.netlify.com).
3. **Configure the Project**:
   - Framework Preset: `Vite`
   - Build Command: `npm run build`
   - Output Directory: `dist`
4. **Environment Variables**: If your backend URL changes, you should store it in a `.env` file (e.g., `VITE_API_URL=https://your-backend.com`).
