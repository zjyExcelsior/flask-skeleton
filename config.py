# coding: utf-8
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/flask_skeleton_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from local_settings import * # 导入本地配置
except ImportError:
    pass
