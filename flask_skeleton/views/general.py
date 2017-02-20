# coding: utf-8
from flask import Blueprint

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    return 'index...'
