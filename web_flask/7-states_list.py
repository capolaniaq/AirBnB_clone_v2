
from flask.templating import render_template
from models import storage
from flask import Flask

app = Flask(__name__)

@app.teardown_appcontext
def close():
    """function that call storage.close"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def body():
    state = storage.all()
    return render_template('7-states_list.html', state=state)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)