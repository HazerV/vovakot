from flask import flask

app = Flask(__name__)

@app route('/')
def index():
    return "Привет мир!"
app.run(port='8000')
