from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
import re
import tensorflow as tf
import numpy as np
import cv2
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras
from cv2 import dnn
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SECRET_KEY'] = 'bibek_kumar_21'

DB_HOST="localhost"
DB_NAME="frdb"
DB_USER="postgres"
DB_PASS="bibek20"

conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)


# Load the trained model
model = tf.keras.models.load_model("Real_fake_prediction_model_1.h5")
img_size = 128  # Adjust according to your model's input size

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def preprocess_image(filepath):
    image = Image.open(filepath).convert('RGB')  # Ensure 3 channels
    image = image.resize((img_size, img_size))  # Resize to model input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/',methods=['GET','POST'])
def index():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Perform server-side validation (optional)
        if not name or not email or not message:
            flash('Please fill in all required fields (name, email, and message).', 'error')
            return render_template('index.html')
        
        try:
            # Insert data into the database
            cursor.execute("INSERT INTO contact(name, email,  message) VALUES (%s, %s, %s)", 
                           (name, email, message))
            conn.commit()
            flash('Thanks for reaching out! We’ll get back to you soon.', 'success')
        except Exception as e:
            conn.rollback()  # Rollback the transaction on error
            flash('An error occurred while sending your message. Please try again.', 'error')
            print(str(e))  # Debugging, print the error to the console

    return render_template('index.html')

# Login Page
@app.route('/login',methods=['GET','POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Fetch the account by username (assuming the username is unique)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            password_rs = account['password']  # The hashed password stored in the database
            print(password_rs)
            
            # Check if the entered password matches the stored hashed password
            if check_password_hash(password_rs, password):
                session['loggedin'] = True
                session['username'] = account['username']
                return redirect(url_for('predict'))
            else:
                flash('Incorrect password', 'error')
        else:
            flash('Account does not exist or incorrect username!', 'error')
        
    return render_template('login.html')

#Signup page
@app.route('/signupform',methods=['GET', 'POST'])
def signup():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        _hashed_password=generate_password_hash(password)
        if not username or not email or not password or not confirm_password:
            flash('Please fill out all fields!', 'error')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+$', email):
            flash('Invalid email address!', 'error')
        elif not re.match(r'[A-Za-z0-9]+$', username):
            flash('Username must contain only letters and numbers!', 'error')
        elif password != confirm_password:
            flash('Passwords do not match!', 'error')
        else:
            # Check if account already exists
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            account = cursor.fetchone()

            if account:
                flash('Account already exists!', 'error')
            else:
                # Hash the password and store the account
                hashed_password = generate_password_hash(password)
                cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                               (username, email, hashed_password))
                conn.commit()
                flash('You have successfully registered!', 'success')
            return redirect(url_for('signup'))  # Redirect after success

    return render_template('signup.html')


@app.route('/predict',methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('predict.html', error="No file uploaded.")

        file = request.files['file']
        if file.filename == '':
            return render_template('predict.html', error="No selected file.")

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Preprocess the image
            image = preprocess_image(filepath)

            # Make prediction
            prediction = model.predict(image)[0][0]  # Assuming binary classification
            result = "Real Face" if prediction > 0.5 else "Fake Face"

            return render_template('predict.html', result=result, filepath=filepath)

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
