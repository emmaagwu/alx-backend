#!/usr/bin/env python3
"""
0-app.py

This script sets up a basic Flask app with a
single route that renders an index page,
and configures Babel for internationalization.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    :return: Rendered HTML template for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
