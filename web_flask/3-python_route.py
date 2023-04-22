#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function called with root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function called with /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Function called with /c/<text>"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Function called with /pyhton/(<text>)"""
    if text != 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
