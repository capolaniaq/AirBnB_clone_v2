#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function that return message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """function that return message in route /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_message(text):
    """function that return message in route /c/
    with variable inside"""
    string = text
    string = string.replace('_', ' ')
    return "C {}".format(string)


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python_message(text):
    """Function that send the message with the defaul value"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def int_route(n):
    """print route with number"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>')
def template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
