from pymongo import MongoClient
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    username = request.form['username']
    password = request.form['password']

    # Check username and password, redirect to content page if successful
    if check_credentials(username, password):
        return redirect(url_for('content'))
    else:
        return "Invalid username or password"

@app.route('/signup', methods=['POST'])
def signup():
    new_username = request.form['newUsername']
    new_password = request.form['newPassword']
    history = request.form['history']

    # Store new user data in MongoDB
    store_user(new_username, new_password, history)

    # Redirect to content page
    return redirect(url_for('content'))

@app.route('/content')
def content():
    return "This is the content page"

def check_credentials(username, password):
    # Check username and password in the database
    # You need to implement this according to your database schema
    return True  # Placeholder for demonstration

def store_user(username, password, history):
    # Store new user data in MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['intelligent_tutoring']
    learners_collection = db['learners']
    learners_collection.insert_one({
        'username': username,
        'password': password,
        'history': history
    })

if __name__ == '__main__':
    app.run(debug=True)
