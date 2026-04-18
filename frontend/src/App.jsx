import { useState } from 'react'
import axios from 'axios'

function App() {
  const [file, setFile] =useState(null)
  const [resultImage, setResultImage] = useState(null)

  const handleUpload = async () => {
    // 1. Pack the image into a "Box" (FormData)
    const formData = new FormData()
    formData.append('image', file)

     // 2. Mail the box to the kitchen (Backend)
     const response = await axios.post('http://localhost:8000/predict', formData,{
      responseType: 'blob'
     })

     // 3. Update our result variable
     setResultImage(URL.createObjectURL(response.data))
     
  }

  return (
    <div 
      style={{ 
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #1f1c2c, #928dab)',
        color: '#fff',
        fontFamily: 'Arial, sans-serif',
        padding: '40px'
      }}
    >
      <h1 style={{ fontSize: '3rem', marginBottom: '20px' }}>🛸 Drone Detector</h1>
      
      <div 
        style={{ 
          backgroundColor: 'rgba(255,255,255,0.1)',
          padding: '30px',
          borderRadius: '12px',
          boxShadow: '0 8px 20px rgba(0,0,0,0.3)',
          textAlign: 'center',
          width: '400px',
          maxWidth: '90%'
        }}
      >
        <input 
          type="file" 
          onChange={(e) => setFile(e.target.files[0])} 
          style={{ 
            margin: '20px 0',
            padding: '10px',
            borderRadius: '8px',
            border: 'none',
            backgroundColor: '#fff',
            color: '#333',
            cursor: 'pointer',
            width: '100%'
          }}
        />

        <button 
          onClick={handleUpload}
          style={{ 
            padding: '12px 25px',
            borderRadius: '8px',
            border: 'none',
            background: 'linear-gradient(135deg, #ff6a00, #ee0979)',
            color: '#fff',
            fontSize: '1rem',
            fontWeight: 'bold',
            cursor: 'pointer',
            transition: 'transform 0.2s ease, box-shadow 0.2s ease'
          }}
          onMouseOver={(e) => {
            e.target.style.transform = 'scale(1.05)';
            e.target.style.boxShadow = '0 6px 15px rgba(0,0,0,0.3)';
          }}
          onMouseOut={(e) => {
            e.target.style.transform = 'scale(1)';
            e.target.style.boxShadow = 'none';
          }}
        >
          🚀 Upload and Predict
        </button>
      </div>

      {resultImage && (
        <div 
          style={{ 
            marginTop: '40px',
            textAlign: 'center',
            backgroundColor: 'rgba(255,255,255,0.1)',
            padding: '20px',
            borderRadius: '12px',
            boxShadow: '0 6px 15px rgba(0,0,0,0.3)',
            width: '500px',
            maxWidth: '90%'
          }}
        >
          <h2 style={{ marginBottom: '15px' }}>✨ Result:</h2>
          <img 
            src={resultImage} 
            alt="Result" 
            style={{ 
              maxWidth: '100%', 
              borderRadius: '12px',
              border: '3px solid #fff'
            }} 
          />
        </div>
      )}
    </div>
  );

}

export default App
