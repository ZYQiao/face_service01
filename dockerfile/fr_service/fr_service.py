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

import configs


def face_recognition(face1, face2):
    time.sleep(1.5)
    return 0.5


class Service:
    def __int__(self):
        self.INFO_KEY = configs.app_info_key
        self.RESPONSE_KEY = configs.app_response_key
        self.redis_host = configs.app_redis_hostname
        self.redis_port = configs.app_redis_port

    def start(self):
        while True:
            try:
                r = redis.Redis(host=self.redis_host, port=self.redis_port)
                info_str = r.lpop(self.INFO_KEY)
                # print(info_str)
                if not info_str:
                    time.sleep(configs.call_interval)
                    continue
                info = json.loads(info_str)

                score = face_recognition(info['face1'], info['face2'])

                ans = {
                    'id': info['id'],
                    'score': str(score)
                }

                ans_str = json.dumps(ans)
                print(ans_str)
                assert r.rpush(self.RESPONSE_KEY, ans_str)
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
