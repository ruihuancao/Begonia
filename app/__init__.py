#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/13 18:06
# @Author  : ruihuancao@gmail.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.default')
    app.config.from_pyfile('config.py')  # 从instance文件夹中加载配置
    # app.config.from_envvar('APP_CONFIG_FILE')
    return app

app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.home import home as home_bp
from app.main import main as main_bp
from app.api import api_bp

app.register_blueprint(home_bp)
app.register_blueprint(main_bp)
app.register_blueprint(api_bp)