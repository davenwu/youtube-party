import os

from flask import Flask

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/', methods=('GET', 'POST'))
    def index():
        return render_template('index.html')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
