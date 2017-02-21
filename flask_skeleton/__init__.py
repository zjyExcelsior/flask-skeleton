# coding: utf-8
from flask import Flask
from .ext import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)

    from .views import general
    app.register_blueprint(general.mod)

    return app
