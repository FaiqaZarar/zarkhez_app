import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import sys
import os

# Load Model
model = tf.keras.models.load_model(os.path.join(os.getcwd(), "model", "wheat_disease_model.keras"))

# Class Labels (must match your training order)
class_labels = [
    'Black Rust', 'Blast', 'Brown Rust', 'Fusarium Head Blight', 'Healthy Wheat',
    'Leaf Blight', 'Mildew', 'Mite', 'Septoria', 'Smut',
    'Stem fly', 'Tan spot', 'Yellow Rust'
]

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]

    print(f"Predicted Class: {predicted_class}")

# Example usage (you can call this from CLI)
if __name__ == "__main__":
    img_path = sys.argv[1]
    predict_image(img_path)
