# -*- coding: utf-8 -*-
import requests
import traceback
import logging
import time


#获取沃之树首页，得到领流量的目标值
def main(*i):
    client = i[0]
    index = client.post('https://m.client.10010.com/mactivity/arbordayJson/index.htm')
    index.encoding='utf-8'
    res = index.json()
    return res['data']['flowChangeList']

#沃之树任务
#位置: 首页 --> 游戏 --> 沃之树
def woTree_task(client):
    #领取4M流量*3
    try:
        flowList = get_woTree_glowList(client)
        num = 1
        for flow in flowList:
            takeFlow = client.get('https://m.client.10010.com/mactivity/flowData/takeFlow.htm?flowId=' + flow['id'])
            takeFlow.encoding='utf-8'
            res1 = takeFlow.json()
            if res1['code'] == '0000':
                logging.info('【沃之树-领流量】: 4M流量 x' + str(num))
            else:
                logging.info('【沃之树-领流量】: 已领取过 x' + str(num))
            #等待1秒钟
            time.sleep(1)
            num = num + 1
        client.post('https://m.client.10010.com/mactivity/arbordayJson/getChanceByIndex.htm?index=0')
        #浇水
        grow = client.post('https://m.client.10010.com/mactivity/arbordayJson/arbor/3/0/3/grow.htm')
        grow.encoding='utf-8'
        res2 = grow.json()
        logging.info('【沃之树-浇水】: 获得' + str(res2['data']['addedValue']) + '培养值')
        time.sleep(1)
    except Exception as e:
        print(traceback.format_exc())
        logging.error('【沃之树】: 错误，原因为: ' + str(e))