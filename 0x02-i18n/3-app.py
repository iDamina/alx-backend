#!/usr/bin/env python3
"""
A simple flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Summary

    Returns:
            type: description
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strick_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determine the best match for supported languages

    Returns:
            type: description
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    Summary
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
