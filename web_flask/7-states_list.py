#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.teardown_appcontext
def close():
    """function that call storage.close"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def body():
    """function that call storage.close"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)