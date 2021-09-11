#!/usr/bin/python3
"""Script that insert message in host=0.0.0.0 port=5000
and route /hbnb and /c/ with other variable"""

from flask import Flask


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
