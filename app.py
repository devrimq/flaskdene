from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, devrim  World!'

@app.route('/new')
def new_route():
    return 'This is a new  devrim route!'
