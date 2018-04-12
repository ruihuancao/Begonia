#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 13:01
# @Author  : ruihuancao@gmail.com
# @File    : models.py
# @Software: PyCharm

from .. import db
from .. import ma


class PoemsAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    intro_l = db.Column(db.Text)


class Poems(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)


class HtmlData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(128))
    content = db.Column(db.Text)
    time = db.Column(db.Integer)


class PoemsSchema(ma.ModelSchema):
    class Meta:
        model = Poems


class PoemsAuthorSchema(ma.ModelSchema):
    class Meta:
        model = PoemsAuthor
