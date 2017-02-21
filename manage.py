# coding: utf-8
from flask_skeleton import (create_app, db)
from flask_skeleton.models import users

app = create_app('config')


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
