#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 16:18
# @Author  : ruihuancao@gmail.com
# @File    : poetry.py
# @Software: PyCharm
from flask_restful import Resource, reqparse, fields, marshal_with
from app.api.models import Poems, PoemsSchema, PoemsAuthor, PoemsAuthorSchema
from flask import jsonify


def make_response(data={}, status=200):
    reponse = {
        'data': data,
        'status': status
    }
    return jsonify(reponse)


class PoemAPI(Resource):
    def get(self, id):
        poem = Poems.query.get(id)
        poem_author = PoemsAuthor.query.get(id)
        poem_schema = PoemsSchema()
        poem_author_schema = PoemsAuthorSchema()
        return make_response({
            'author': poem_author_schema.dump(poem_author).data,
            'poem': poem_schema.dump(poem).data
        })


class PoemAuthorAPI(Resource):
    def get(self, id):
        poem_author = PoemsAuthor.query.get(id)
        poem_author_schema = PoemsAuthorSchema()
        return make_response({
            'author': poem_author_schema.dump(poem_author).data
        })

class PoetryAPI(Resource):
    def get(self, id):
        pass


class PoetryAuthorAPI(Resource):
    def get(self, id):
        pass
