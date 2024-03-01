"""To demo a simple web application in python"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    We'll use Flask to create a basic web application.

    """

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
