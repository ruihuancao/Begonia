#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/13 18:09
# @Author  : ruihuancao@gmail.com
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint
from flask_restful import Api
from app.api.poetry import PoemAPI, PoemAuthorAPI, PoetryAPI, PoetryAuthorAPI

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)
api.add_resource(PoemAPI, '/v1.0/poetry/poem/<int:id>/')
api.add_resource(PoemAuthorAPI, '/v1.0/poetry/poem/author/<int:id>')
api.add_resource(PoetryAPI, '/v1.0/poetry/<int:id>')
api.add_resource(PoetryAuthorAPI, '/v1.0/poetry/author/<int:id>')


