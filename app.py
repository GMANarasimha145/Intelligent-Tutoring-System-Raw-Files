from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f"Name: {name}<br>Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)
