# -*- coding: utf-8 -*-
"""

@time    : 2021/5/16 0:51
@author  : Yuqiao Zhao
@contact : zhaoyuqiao97@gmail.com
@file    : run.py
@software: PyCharm

"""
import view
if __name__ == '__main__':
    from app import app
    app.run(port=12349,debug=True)