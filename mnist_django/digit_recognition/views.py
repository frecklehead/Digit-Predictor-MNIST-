from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64
import os

# Define the path to the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/mnist_model.h5')

# Load your trained model
model = tf.keras.models.load_model(MODEL_PATH)

def home(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        data = request.POST.get('image')
        image = Image.open(io.BytesIO(base64.b64decode(data.split(',')[1]))).convert('L')
        image = image.resize((28, 28))
        image = np.array(image)
        image = image / 255.0
        image = image.reshape(1, 28, 28)
        prediction = model.predict(image)
        digit = np.argmax(prediction)
        return JsonResponse({'digit': int(digit)})
