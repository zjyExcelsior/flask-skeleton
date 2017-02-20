# coding: utf-8
from flask import Flask
from .ext import db

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

from .cmds import initdb
from .views import general

app.register_blueprint(general.mod)
