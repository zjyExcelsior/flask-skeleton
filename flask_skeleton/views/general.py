# coding: utf-8
from flask import (current_app, Blueprint)

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    return 'index...'

@mod.route('/config/debug/')
def config_debug():
    return 'DEBUG: {}'.format(current_app.config.get('DEBUG'))
