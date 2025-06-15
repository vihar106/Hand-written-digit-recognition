from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import base64
from io import BytesIO
from PIL import Image

# Initialize Flask app
app = Flask(__name__)
model = load_model("mnist_model.keras")

@app.route('/')
def home():
    return render_template("canvas.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json.get('image')
        if not data:
            return jsonify({"error": "No image data received"})

        image_data = base64.b64decode(data.split(",")[1])
        image = Image.open(BytesIO(image_data)).convert('L')
        image = image.resize((28, 28))
        img_array = np.array(image) / 255.0
        img_array = img_array.reshape(1, 28, 28)

        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        return jsonify({"predicted_digit": int(predicted_digit)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
