# -*- coding: utf-8 -*-
import requests
import logging
import traceback
import time

#领取 4G 流量包任务，看视频、下载软件每日可获得 240M 流量
#位置: 我的 --> 我的金币 --> 4G流量包
def collectFlow_task(client):
    data1 = {
        'stepflag': '22'
    }
    
    data2 = {
        'stepflag': '23'
    }
    try:
        for i in range(3):
            #看视频
            watchVideo = client.post('https://act.10010.com/SigninApp/mySignin/addFlow',data1)
            watchVideo.encoding='utf-8'
            res1 = watchVideo.json()
            if res1['reason'] == '00':
                logging.info('【4G流量包-看视频】: 获得' + res1['addNum'] + 'M流量 x' + str(i+1))
            elif res1['reason'] == '01':
                logging.info('【4G流量包-看视频】: 已完成' + ' x' + str(i+1))
            #等待1秒钟
            time.sleep(1)
            #下软件
            downloadProg = client.post('https://act.10010.com/SigninApp/mySignin/addFlow',data2)
            downloadProg.encoding='utf-8'
            res2 = downloadProg.json()
            if res2['reason'] == '00':
                logging.info('【4G流量包-下软件】: 获得' + res2['addNum'] + 'M流量 x' + str(i+1))
            elif res2['reason'] == '01':
                logging.info('【4G流量包-下软件】: 已完成' + ' x' + str(i+1))
            #等待1秒钟
            time.sleep(1)
    except Exception as e:
        print(traceback.format_exc())
        logging.error('【4G流量包】: 错误，原因为: ' + str(e))