import keras2onnx
import onnx
from tensorflow.keras.models import load_model

# Load the .h5 model
h5_model_path = 'plant_disease_prediction_model.h5'
model = load_model(h5_model_path)

# Convert to ONNX format
onnx_model_path = 'plant_disease_prediction_model.onnx'
onnx_model = keras2onnx.convert_keras(model, model.name)
onnx.save_model(onnx_model, onnx_model_path)
