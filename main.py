from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    n = random.randint(0, 1000)
    k = random.randint(100, 5000)
    return render_template('index.html', n=n, k=k)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/vika')
def vika():
    return "<h2>My name Vika</h2>"


if __name__ == '__main__':
    app.run(debug=True)
