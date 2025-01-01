from flask import Flask, render_template, request, send_file
from ultralytics import YOLO
import os
from PIL import Image
import io
import numpy as np
import cv2

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from main_utils.utils import decodeImage
from prediction.predict import DroneNon

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')



app = Flask(__name__)

# Load the trained YOLO model (update the path to your model)
model = YOLO('best.pt')

# Route to serve the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return {"error": "No image file found in request"}, 400

    uploaded_file = request.files['image']
    image = Image.open(uploaded_file)

    # Perform inference
    results = model(image)

    # Get the first result (YOLO returns a list of results)
    result = results[0]

    # Convert the result to a numpy array (this is the bounding-boxed image)
    result_image = result.plot()  # Get the image with bounding boxes

    # Convert numpy array to a PIL Image
    result_image_pil = Image.fromarray(result_image)

    # Save the result to a BytesIO object
    output = io.BytesIO()
    result_image_pil.save(output, format="JPEG")
    output.seek(0)

    # Return the processed image
    return send_file(output, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
