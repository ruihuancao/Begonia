#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 12:40
# @Author  : ruihuancao@gmail.com
# @File    : manager.py
# @Software: PyCharm
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
