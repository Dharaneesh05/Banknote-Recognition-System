from ultralytics import YOLO
import os
import torch  
DATASET_YAML = "dataset/dataset.yaml" 
if not os.path.exists(DATASET_YAML):
    raise FileNotFoundError(f"Dataset YAML file '{DATASET_YAML}' not found.")
model = YOLO("yolov8n.pt")
model.train(
    data=DATASET_YAML,  
    epochs=50, 
    imgsz=640,  
    batch=16,  
    workers=4,  
    device="cuda" if torch.cuda.is_available() else "cpu", 
    project="currency_yolo",  
    name="yolov8_currency",  
    save=True  
)
MODEL_PATH = "yolov8_currency.pt"
model.export(format='torchscript', path=MODEL_PATH)
print(f"Training complete. Model saved as {MODEL_PATH}")
