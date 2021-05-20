# -*- coding: utf-8 -*-
"""

@time    : 2021/5/16 21:44
@author  : Yuqiao Zhao
@contact : zhaoyuqiao97@gmail.com
@file    : fr_service.py
@software: PyCharm

"""

import time
import traceback
import redis
import json
import pymongo
import configs


def face_recognition(face1, face2):
    time.sleep(1.5)
    return 0.5


class Service:
    def __int__(self):
        self.RESPONSE_KEY = configs.app_response_key
        self.redis_host = configs.app_redis_hostname
        self.redis_port = configs.app_redis_port
        self.mongo_uri = configs.app_mongo_uri
        self.mongo_db = configs.app_database_name
    def start(self):
        while True:
            try:
                r = redis.Redis(host=self.redis_host, port=self.redis_port)
                response_str = r.lpop(self.RESPONSE_KEY)
                # print(info_str)
                if not response_str:
                    time.sleep(configs.call_interval)
                    continue
                response = json.loads(response_str)
                print(response)
                now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
                response['collected_time'] = now_time
                myclient = pymongo.MongoClient(self.mongo_uri)
                mydb = myclient[self.mongo_db]
                my_collection = mydb[configs.app_database_collection]
                my_collection.insert_one(response)
                print(response)


            except Exception as e:
                # print(e)
                time.sleep(configs.call_interval)
                traceback.print_exc()
                continue

    def stop(self):
        pass


if __name__ == '__main__':
    service = Service()
    service.__int__()
    service.start()
