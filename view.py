# -*- coding: utf-8 -*-
"""

@time    : 2021/5/16 0:42
@author  : Yuqiao Zhao
@contact : zhaoyuqiao97@gmail.com
@file    : view.py
@software: PyCharm

"""
import json

from flask import request
from app import app
import redis
import configs

import uuid

@app.route('/face_service',methods=['GET'])

def user_call_face_service():

    ans = {'status':200,'err_msg':''}
    try:
        face1 = request.args.get('face1')
        face2 = request.args.get('face2')
        info = {
            'id' : str(uuid.uuid1()),
            'face1' : face1,
            'face2' : face2
        }
        info_str = json.dumps(info)


        r = redis.Redis(configs.app_redis_hostname,configs.app_redis_port)
        r.rpush(configs.app_info_key,info_str)


        ans['id'] = info['id']
    except Exception as e:
        ans['status'] = 500
        ans['err_msg'] = str(e)

    return ans
