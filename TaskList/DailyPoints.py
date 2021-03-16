# -*- coding: utf-8 -*-
import requests
import logging
import traceback
import random
import time

#每日领取100定向积分
#位置: 发现 --> 定向积分 --> 领取定向积分兑爆款
def main(*i):
    client = i[0]
    data = {
        'from': random.choice('123456789') + ''.join(random.choice('0123456789') for i in range(10))
    }
    try:
        integral = client.post('https://m.client.10010.com/welfare-mall-front/mobile/integral/gettheintegral/v1', data=data)
        integral.encoding = 'utf-8'
        res = integral.json()
        logging.info("【100定向积分】: " + res['msg'])
        time.sleep(1)
    except Exception as e:
        print(traceback.format_exc())
        logging.error('【100定向积分】: 错误，原因为: ' + str(e))