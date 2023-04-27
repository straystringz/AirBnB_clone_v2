#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: display 'Hello HBNB!'.
    /hbnb: display 'HBNB'.
    /c/<text>: display 'C' then the value of <text>.
    /python/(<text>): display 'Python' then the value of <text>.
    /number/<n>: display 'n is a number' only if <n> is an integer.
    /number_template/<n>: display an HTML page only if <n> is an integer.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display 'C' then the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """display 'Python' then the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
