from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# only local service
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/vika')
def vika():
    return "<h2>My name Vika</h2>"


if __name__ == '__main__':
    app.run(debug=True)
