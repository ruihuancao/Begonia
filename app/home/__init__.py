#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 12:23
# @Author  : ruihuancao@gmail.com
# @File    : __init__.py.py
# @Software: PyCharm


from flask import Blueprint

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/home'
)

from . import views
