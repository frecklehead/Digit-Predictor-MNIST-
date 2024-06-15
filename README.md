Digit Recognizer: Draw and Predict
This Django project provides a simple web application that allows users to draw digits on a canvas and receive a prediction of the digit. The prediction is powered by a machine learning model trained on the MNIST dataset.
Features
Interactive Canvas: Users can draw digits directly on the canvas using their mouse or touch screen.
Prediction Engine: A trained machine learning model analyzes the drawn image and predicts the digit.
Real-time Feedback: The predicted digit is displayed immediately after the user finishes drawing.
Getting Started
Clone the repository:
git clone https://github.com/your-username/digit-recognizer.git
Use code with caution.
Bash
Install dependencies:
cd digit-recognizer
pip install -r requirements.txt
Use code with caution.
Bash
Set up your environment:
Create a virtual environment (recommended).
Activate the virtual environment.
Ensure you have a working database (e.g., PostgreSQL) and configure it in your settings.py file.
Install the required database libraries (e.g., psycopg2 for PostgreSQL).
Run migrations:
python manage.py makemigrations
python manage.py migrate
Use code with caution.
Bash
Start the development server:
python manage.py runserver
Use code with caution.
Bash
Access the application: Open your web browser and navigate to http://127.0.0.1:8000/.
Project Structure
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
Backend (Django)
Models (models.py):
The DigitModel class represents the machine learning model used for prediction.
The load_model() function from TensorFlow/Keras loads your trained model from a file (e.g., your_model.h5).
The predict() method takes an image as input, processes it (converts to grayscale, resizes, normalizes), feeds it to the model, and returns the predicted digit.
Views (views.py):
The predict() view handles POST requests from the frontend.
It retrieves the base64 encoded image data from the POST request.
It creates a DigitModel object and calls the predict() method to get the predicted digit.
It returns a JSON response containing the predicted digit.
URLs (urls.py):
Maps the URL /predict/ to the predict() view.
CSRF Protection:
Django's built-in CSRF protection mechanism is enabled, ensuring that the frontend can only send POST requests to the backend if they have the correct CSRF token.
The CSRF token is automatically added to forms in Django templates using the {% csrf_token %} tag.
The frontend code retrieves the CSRF token from the cookie using getCookie('csrftoken') and includes it in the fetch request header.
Frontend (HTML, CSS, JavaScript)
HTML Structure (index.html):
A canvas element is provided for drawing.
A clear button is included to reset the canvas.
A heading is used to display the prediction result.
CSS Styling (style.css):
Basic styling is applied to the elements for visual appearance.
JavaScript Functionality (script.js):
Canvas Drawing:
Event listeners are added to the canvas to handle mouse events (mousedown, mouseup, mousemove).
Functions are defined to draw on the canvas based on mouse coordinates.
Clear Button:
An event listener is added to the clear button to clear the canvas.
Prediction Logic:
When the user releases the mouse (mouseup), the canvas content is converted to a base64 encoded image.
The CSRF token is retrieved from the cookie.
A fetch request is sent to the /predict/ endpoint, sending the image data and CSRF token in the request headers.
The response from the server (a JSON object containing the predicted digit) is then displayed in the result heading.
Use code with caution.
Customization
Model: The project uses a pre-trained model. You can replace it with a different model or train your own model.
Frontend: The front-end code is written in HTML, CSS, and JavaScript. You can customize the design and functionality to your liking.
Backend: The backend code uses Django views and templates. You can add additional functionality or modify existing features.
Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to open an issue or submit a pull request.
License
This project is licensed under the MIT License.
