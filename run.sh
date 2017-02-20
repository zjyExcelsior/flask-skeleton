#!/bin/sh
export FLASK_APP=flask_skeleton
export FLASK_DEBUG=true
pip install -e .
flask run