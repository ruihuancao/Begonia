#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 12:29
# @Author  : ruihuancao@gmail.com
# @File    : views.py
# @Software: PyCharm

from flask import render_template
from . import home


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/index')
def index_home():
    return render_template('home/index.html')
