#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 14:38
# @Author  : ruihuancao@gmail.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

main = Blueprint('main',
                 __name__,
                 template_folder='templates',
                 static_folder='static')

from app.main import views