# -*- coding: utf-8 -*-
import requests
import traceback
import logging
import time


#每日1G流量日包领取
#位置: 签到 --> 免费领 -->  免费领流量
def dayOneG_Task(client):
        try:
            #观看视频任务
            client.post('https://act.10010.com/SigninApp/doTask/finishVideo')
            #请求任务列表
            getTaskInfo = client.post('https://act.10010.com/SigninApp/doTask/getTaskInfo')
            getTaskInfo.encoding = 'utf-8'
            getPrize = client.post('https://act.10010.com/SigninApp/doTask/getPrize')
            getPrize.encoding = 'utf-8'
            client.post('https://act.10010.com/SigninApp/doTask/getTaskInfo')
            res1 = getTaskInfo.json()
            res2 = getPrize.json()
            if(res1['data']['taskInfo']['status'] == '1'):
                logging.info('【1G流量日包】: ' + res2['data']['statusDesc'])
            else:
                logging.info('【1G流量日包】: ' + res1['data']['taskInfo']['btn'])
            time.sleep(1)
        except Exception as e:
            print(traceback.format_exc())
            logging.error('【1G流量日包】: 错误，原因为: ' + str(e))