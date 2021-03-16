# -*- coding: utf-8 -*-

import requests
import logging
import traceback
import time

#开宝箱，赢话费任务 100M 流量
#位置: 首页 --> 游戏 --> 每日打卡 --> 宝箱任务
def main(*i):
    client = i[0]
    client.headers.update({'referer': 'https://img.client.10010.com'})
    client.headers.update({'origin': 'https://img.client.10010.com'})
    data1 = {
        'thirdUrl': 'https://img.client.10010.com/shouyeyouxi/index.html#/youxibaoxiang'
    }
    data2 = {
        'methodType': 'reward',
        'deviceType': 'Android',
        'clientVersion': '8.0100',
        'isVideo': 'N'
    }
    param = '?methodType=taskGetReward&taskCenterId=187&clientVersion=8.0100&deviceType=Android'
    data3 = {
        'methodType': 'reward',
        'deviceType': 'Android',
        'clientVersion': '8.0100',
        'isVideo': 'Y'
    }
    try:
        #在分类中找到宝箱并开启
        box = client.post('https://m.client.10010.com/mobileService/customer/getShareRedisInfo.htm', data=data1)
        box.encoding='utf-8'
        time.sleep(1)
        #观看视频领取更多奖励
        watchAd = client.post('https://m.client.10010.com/game_box', data=data2)
        watchAd.encoding='utf-8'
        #等待随机秒钟
        time.sleep(1)
        #完成任务领取100M流量
        drawReward = client.get('https://m.client.10010.com/producGameTaskCenter' + param)
        time.sleep(1)
        watchAd = client.post('https://m.client.10010.com/game_box', data=data3)
        drawReward.encoding='utf-8'
        res = drawReward.json()
        if res['code'] == '0000':
            logging.info('【100M寻宝箱】: ' + '获得100M流量')
        else:
            logging.info('【100M寻宝箱】: ' + '任务失败')
        time.sleep(1)
        client.headers.pop('referer')
        client.headers.pop('origin')
    except Exception as e:
        print(traceback.format_exc())
        logging.error('【100M寻宝箱】: 错误，原因为: ' + str(e))
