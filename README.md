## Digit Recognizer: Draw and Predict

This Django project provides a simple web application that allows users to draw digits on a canvas and receive a prediction of the digit. The prediction is powered by a machine learning model trained on the MNIST dataset.

### Features

* **Interactive Canvas:** Users can draw digits directly on the canvas using their mouse or touch screen.
* **Prediction Engine:** A trained machine learning model analyzes the drawn image and predicts the digit.
* **Real-time Feedback:** The predicted digit is displayed immediately after the user finishes drawing.
* **CSRF Protection:**  The application includes CSRF protection to prevent malicious attacks.

### Getting Started

1. **Clone the repository:**
   ```bash
https://github.com/frecklehead/Digit-Predictor-MNIST-.git

2. **Install dependencies:**

```cd digit-recognize```

```pip install -r requirements.txt```

4. **Set up your environment:**


   * Create a virtual environment (recommended):
   
```python -m venv .venv```

5.**Activate the virtual environment:**

 # On Linux/macOS
 
````source .venv/bin/activae```

  # On Windows
  
```.venv\Scripts\activate```

6 **Run migrations:**

```python manage.py makemigrations```

```python manage.py migrate```

7.**Start the development server:**

```python manage.py runserver```

8 **Access the application:**

``` Open your web browser and navigate to http://127.0.0.1:8000/.```

##Project Structure
```
mnist_django/
├── digit_recognition/
│   ├── migrations/
│   ├── models/
│   │   └── mnist_model.h5
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
├── mnist_django/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
```
### Features

* **Interactive Canvas:** Users can draw digits directly on the canvas using their mouse or touch screen.
* **Prediction Engine:** A trained machine learning model analyzes the drawn image and predicts the digit.
* **Real-time Feedback:** The predicted digit is displayed immediately after the user finishes drawing.
* **CSRF Protection:**  The application includes CSRF protection to prevent malicious attacks.


# How it Works
## Backend (Django):
* **Models (models.py):** 
  The DigitModel class represents the machine learning model used for 
  prediction.
   It loads the trained model from a file (your_model.h5).
It provides a predict() method to process an image and return the predicted digit.
* **Views (views.py):** 
The predict() view handles POST requests from the frontend.
It retrieves the image data, processes it, and uses the DigitModel to predict the digit.
It returns a JSON response with the predicted digit.
* **URLs (urls.py):** 
Maps the URL /predict/ to the predict() view.
* **CSRF Protection:** 
Django's built-in CSRF protection is enabled.
The CSRF token is automatically included in forms and retrieved by the frontend JavaScript code.
## Frontend (HTML, CSS, JavaScript):
**HTML Structure (index.html):**
The HTML code provides the canvas, clear button, and heading to display the prediction.

 **CSS Styling (style.css):**
CSS styles the elements for a visually appealing design.

**JavaScript Functionality (script.js):**
- Handles user interaction with the canvas (drawing, clearing).
- Converts the canvas content to an image.
- Retrieves the CSRF token.
- Sends the image data and CSRF token to the server using fetch.
- Displays the prediction result from the server.

## Key Points
- The application leverages the power of machine learning to recognize digits drawn by users.
- Django provides a robust backend framework to handle the prediction logic and protect against CSRF attacks.
- JavaScript enables interactive elements like the canvas and dynamically updates the prediction result.
- The project demonstrates how to integrate machine learning models with web applications for practical use cases.

# Contributing
##Contributions are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to open an issue or submit a pull request.
