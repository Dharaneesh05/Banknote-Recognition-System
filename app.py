import os
import base64
import cv2
import numpy as np
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def load_model():
    return "Currency Model Loaded" 

model = load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    detected_currency = "Detected: 50 Rupee Note" 

    return jsonify({'currency': detected_currency, 'image_path': file_path})

@app.route('/detect_live', methods=['POST'])
def detect_live():
    image_data = request.form['image']
    image_data = image_data.replace('data:image/jpeg;base64,', '')
    image_bytes = base64.b64decode(image_data)
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    detected_currency = "Live Detected: 100 Rupee Note" 

    return jsonify({"currency": detected_currency})

if __name__ == '__main__':
    app.run(debug=True)
