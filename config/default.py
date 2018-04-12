#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 16:26
# @Author  : ruihuancao@gmail.com
# @File    : default.py
# @Software: PyCharm

#默认值，适用于所有的环境或交由具体环境进行覆盖
DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:caoruihuan@localhost/test?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS=False