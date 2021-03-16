# -*- coding: utf-8 -*-
import requests
import traceback
import logging
import time

#经多次测试，都可加倍成功了
#每日签到，1积分 +4 积分(翻倍)，第七天得到 1G 日包
#位置: 我的 --> 我的金币
def main(*i):
    client = i[0]
    username= i[1]
    try:
        #参考同类项目 HiCnUnicom 待明日验证是否能加倍成功
        client.headers.update({'referer': 'https://img.client.10010.com/activitys/member/index.html'})
        param = 'yw_code=&desmobile=' + username + '&version=android@$8.0100'
        client.get('https://act.10010.com/SigninApp/signin/querySigninActivity.htm?' + param)
        client.headers.update({'referer': 'https://act.10010.com/SigninApp/signin/querySigninActivity.htm?' + param})
        daySign = client.post('https://act.10010.com/SigninApp/signin/daySign')
        daySign.encoding='utf-8'
        #本来是不想加这个的，但是会出现加倍失败的状况，暂时加上也是有可能出问题
        client.post('https://act.10010.com/SigninApp/signin/todaySign')
        client.post('https://act.10010.com/SigninApp/signin/addIntegralDA')
        client.post('https://act.10010.com/SigninApp/signin/getContinuous')
        client.post('https://act.10010.com/SigninApp/signin/getIntegral')
        client.post('https://act.10010.com/SigninApp/signin/getGoldTotal')
        doubleAd = client.post('https://act.10010.com/SigninApp/signin/bannerAdPlayingLogo')
        client.headers.pop('referer')
        doubleAd.encoding='utf-8'
        res1 = daySign.json()
        res2 = doubleAd.json()
        if res1['status'] == '0000':
            logging.info('【每日签到】: ' + '打卡成功,' + res2['data']['statusDesc'])
        elif res1['status'] == '0002':
            logging.info('【每日签到】: ' + res1['msg'])
        time.sleep(1)
    except Exception as e:
        print(traceback.format_exc())
        logging.error('【每日签到】: 错误，原因为: ' + str(e))