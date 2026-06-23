import tensorflow as tf
import numpy as np
from PIL import Image
from config import MODEL_PATH

# Load the trained CNN model
model = tf.keras.models.load_model(MODEL_PATH)

# Disease labels (change according to your dataset)
labels = [
    "Acne",
    "Eczema",
    "Melanoma",
    "Psoriasis",
    "Healthy Skin"
]


def preprocess_image(image_path):

    img = Image.open(image_path).convert("RGB")

    img = img.resize((224, 224))   # model input size

    img_array = np.array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def predict_image(image_path):

    img = preprocess_image(image_path)

    prediction = model.predict(img)

    predicted_index = np.argmax(prediction)

    disease = labels[predicted_index]

    confidence = float(np.max(prediction))

    return disease, round(confidence * 100, 2)