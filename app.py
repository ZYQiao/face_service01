# -*- coding: utf-8 -*-
"""

@time    : 2021/5/16 0:41
@author  : Yuqiao Zhao
@contact : zhaoyuqiao97@gmail.com
@file    : app.py
@software: PyCharm

"""


import flask
import configs


def create_app():
    app = flask.Flask(__name__)
    app.secret_key = configs.app_secret_key

    return app

app = create_app()