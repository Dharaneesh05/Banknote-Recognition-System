import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

MODEL_PATH = "currency_model.h5" 
DATASET_PATH = "dataset" 
if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(f"Dataset path '{DATASET_PATH}' not found. Please check the dataset location.")
datagen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    zoom_range=0.2
)

train_data = datagen.flow_from_directory(
    DATASET_PATH, target_size=(224, 224), batch_size=32, class_mode='categorical', subset='training')
val_data = datagen.flow_from_directory(
    DATASET_PATH, target_size=(224, 224), batch_size=32, class_mode='categorical', subset='validation')
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),  
    Dense(len(train_data.class_indices), activation='softmax')  
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_data, validation_data=val_data, epochs=15)


model.save(MODEL_PATH)
print("Model saved successfully!")