#!/usr/bin/env python3
""" set up a basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> Any:
    """
    Renders the index page with a welcome message.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
