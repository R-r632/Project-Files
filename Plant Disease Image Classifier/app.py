import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import numpy as np
import tensorflow as tf

# Set working directory and model path
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/plant_disease_prediction_model.h5"
class_indices_path = f"{working_dir}/class_indices.json"

# Load the TensorFlow model
model = tf.keras.models.load_model(model_path)

# Load class indices
with open(class_indices_path, 'r') as f:
    class_indices = json.load(f)

# Flask app
app = Flask(__name__)
CORS(app)

# Image preprocessing function
def preprocess_image(image, target_size=(224, 224)):
    img = Image.open(image).convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array.astype('float32') / 255.0  # Normalize
    return img_array

# Prediction function
def predict_image_class(model, image, class_indices):
    preprocessed_img = preprocess_image(image)
    predictions = model.predict(preprocessed_img)
    predicted_class_idx = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_idx)]
    return predicted_class_name

# Route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files['file']
        if file:
            class_name = predict_image_class(model, file, class_indices)
            return jsonify({'class_name': class_name})
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
