from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
@app.route('/name')
def index(name=''):
    return render_template('index.html', name=name)


# only local service
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/articles')
def articles():
    return render_template('articles.html')


@app.route('/details')
def details():
    return render_template('details.html')


if __name__ == '__main__':
    app.run(debug=True)
