#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/13 18:10
# @Author  : ruihuancao@gmail.com
# @File    : run.py
# @Software: PyCharm

from app import app


# release_app = create_app('config.release')
#
# app = DispatcherMiddleware(release_app, {'/test': debug_app})
#
# run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True)
app.run()
