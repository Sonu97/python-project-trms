# For any request not pertaining to a specific model.
from flask import render_template


def route(app):
    @app.route("/")
    def hello():
        return "Hello, World!"

    @app.route('/trms')
    def add_trms():
        return render_template('trms.html')
