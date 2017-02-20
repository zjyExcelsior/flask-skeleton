# coding: utf-8
from flask_skeleton import app
from .ext import db
from .models import users


@app.cli.command()
def initdb():
    """Initialize the database."""
    db.create_all()


@app.cli.command()
def cleardb():
    """Drop all tables in database."""
    db.drop_all()
