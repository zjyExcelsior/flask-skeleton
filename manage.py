# coding: utf-8
from flask_skeleton import (create_app, db)
from flask_skeleton.models import users
from config import configs
import os

app_env = os.getenv('FLASK_ENV') or 'default'
app = create_app(configs[app_env])


@app.cli.command()
def initdb():
    """Initialize the database."""
    db.create_all()


@app.cli.command()
def cleardb():
    """Drop all tables in database."""
    db.drop_all()

if __name__ == '__main__':
    app.run(debug=True)
