#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ display Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ display HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ display a char C then the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ display Python, then the value of the text variable,
    with default value of text: is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Number route """
    return '{} is number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ displays an HTML page only if n is an integer """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Show if the number is even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
