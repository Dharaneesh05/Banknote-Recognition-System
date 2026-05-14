# Banknote Recognition System

A machine learning-based system for recognizing and detecting banknotes using computer vision and deep learning.

## Project Structure

```
banknote-recognition-system/
│
├── app/                    # Flask web application
│   ├── static/            # CSS, JS, images
│   ├── templates/         # HTML templates
│   ├── app.py            # Main Flask application
│   ├── detect.py         # Detection module
│   ├── webcam.py         # Webcam capture module
│   └── model.py          # Model utilities
│
├── model/                 # ML model and training
│   ├── dataset/          # Training dataset
│   ├── currency_yolo/    # YOLO model outputs
│   ├── yolov8n.pt       # YOLOv8 nano weights
│   ├── yolov8_currency.pt # Trained currency model
│   ├── currency_model.h5  # TensorFlow model
│   ├── train_yolo.py     # YOLO training script
│   └── download_images.py # Dataset download script
│
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md            # This file
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
cd app
python app.py
```

3. Access the web interface at `http://localhost:5000`

## Features

- Upload image for currency detection
- Live webcam detection
- Multi-currency recognition
- YOLOv8 and TensorFlow model support

## Requirements

- Python 3.8+
- Flask
- OpenCV
- TensorFlow
- PyTorch
- Ultralytics (YOLOv8)
- NumPy

## Usage

### Web Interface
- Upload an image to detect the banknote
- Use live camera feed for real-time detection

### Training
```bash
python model/train_yolo.py
```

### Download Dataset
```bash
python model/download_images.py
```

## Models

- **YOLOv8**: Real-time object detection
- **TensorFlow CNN**: Image classification model

## License

MIT License
