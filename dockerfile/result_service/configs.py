# -*- coding: utf-8 -*-
"""

@time    : 2021/5/16 22:35
@author  : Yuqiao Zhao
@contact : zhaoyuqiao97@gmail.com
@file    : configs.py
@software: PyCharm

"""

app_redis_hostname = 'localhost'

app_redis_port = '6379'

app_info_key = 'INFO_KEY'

app_response_key = 'RESPONSE_KEY'

app_database_host = 'my_mongo' # if don't use docker, so this is 'localhost'
app_database_name = 'face_recognition'
app_database_user = 'xcy'
app_database_pwd  = 'xcy123456'
app_database_port = 27017

app_database_collection = 'face_list'

call_interval = 0.1

app_mongo_uri = "mongodb://{}:{}@{}:{}/{}?authMechanism=MONGODB-CR".format(
    app_database_user,
    app_database_pwd,
    app_database_host,
    app_database_port,
    app_database_name
)