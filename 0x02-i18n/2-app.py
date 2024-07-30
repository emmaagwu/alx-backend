#!/usr/bin/env python3
"""
0-app.py

This script sets up a basic Flask app with a single route that
renders an index page, configures Babel for internationalization, and
selects the best language based on request headers.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, localeselector


class Config:
    """
    Config class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    :return: Rendered HTML template for the index page.
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with the supported languages based on the
    request's Accept-Language header.

    :return: The best matched locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
