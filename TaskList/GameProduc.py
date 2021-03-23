# -*- coding: utf-8 -*-
import requests
import traceback
import logging
import time
import json
import hmac
import base64
import random
import datetime


#娱乐中心 玩游戏3GB
#测试时 服务器返回400 无法使用
#若能够解决 希望能提交pr谢谢
def main(*i):
    client = i[0]
    username = i[1]
    
    #获取jwt 用于验证
    cookiesdata = client.cookies.get_dict()
    jwt = cookiesdata['jwt']
    try:
        headers = {'Origin': 'https://img.client.10010.com','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148                       unicom{version:iphone_c@8.0200}{systemVersion:dis}{yw_code:}'}
        client.headers.update(headers)
        #请求热门游戏列表
        data = {'methodType':'popularGames','deviceType':'iOS','clientVersion':'8.0200'}
        index = client.post('https://m.client.10010.com/producGameApp',data=data)
        index.encoding = 'utf-8'
        gamelist = index.json()
        tasklist = []
        if gamelist['msg'] == '热门游戏请求成功':
            for gameinfo in gamelist['popularList']:
                if gameinfo['flow']=='100' and gameinfo['state']!='2':
                    tasklist.append(gameinfo['id'])
                    tasklist.append(gameinfo['name'])
                    tasklist.append(gameinfo['url'])
        
        time.sleep(1)
        #adnew请求
        nowtime=int(time.time())
        adnew = {'version':'iphone_c@8.0200','desmobile':username,'time':nowtime}
        client.post('https://img.client.10010.com/adnew/play_center/',data=adnew)
        client.post('https://m.client.10010.com/pre_finderInterface/gameApp',data={'methodType':'isUnicom'})
        n = 1
        forNum = 0
        #隔三个取一个id
        idlist = tasklist[::3]
        namelist = tasklist[1::3]
        urllist = tasklist[2::3]
        for click in idlist:
            
            #点击游戏
            clickdata ={'methodType':'record','gameId':click,'deviceTyp':'iOS'}
            clickinfo = client.post('https://m.client.10010.com/producGameApp',data=clickdata)
            clickinfo.encoding = 'utf-8'
            clickinfo = clickinfo.json()
            if clickinfo['msg'] == '游戏点击方法调用成功':
                logging.info('【玩游戏3G】:'+namelist[forNum]+' 点击成功')
            else:
                logging.info('【玩游戏3G】:'+namelist[forNum]+' 点击失败')
            
#print(idlist[forNum],namelist[forNum],urllist[forNum])
            #查询状态
            record = {'methodType':'iOSTaskRecord','gameId':click}
            client.post('https://m.client.10010.com/producGameApp',data=record)
            #进行验证
            authdata = {'uin':username,'sig':jwt}
            verify = {'extInfo':jwt,'auth':authdata}
            verifyinfo = client.post('https://m.client.10010.com/game/verify',json=verify)
            verifyinfo.encoding = 'utf-8'
            verifyinfo = verifyinfo.json()
            logging.info('【玩游戏3G】:验证状态'+str(verifyinfo['isLegal']))
            time.sleep(1)
            #完成6分钟游戏
            Seq = n * 3
            nonce = str((random.random() * 90000)+ 10000)
            dd = str(datetime.datetime.now().strftime('%m%d%H%M%S'))
            jtime = str(nowtime % 1000)
            s = int(random.random() * 90000 + 10000)
            traceid = username+'_'+dd+jtime+'_'+str(s)
            deviceInfos = [
  "m=VKY-AL00&o=9&a=28&p=1080*1920&f=HUAWEI&mm=5725&cf=1800&cc=8&qqversion=null",
  "m=SM-G977N&o=7&a=24&p=1080*1920&f=samsung&mm=5725&cf=1800&cc=8&qqversion=null",
  "m=Pixel&o=8&a=27&p=1080*1920&f=google&mm=5725&cf=1800&cc=8&qqversion=null",
]
                    
            launchId1 = str(nowtime)
            deviceInfo = deviceInfos[random.randint(0,2)]
            while(n<=6):
              
              if n == 6:
                  fact = 13
              else:
                  fact = 12
              a = {'0':username,'1':jwt,'2': '2001','3': 0,'4':'101794394'}
              busiBuff = {'0':'null','1':click,'2':fact,'3':'null','4': (nowtime / 1000) + n * 62,'5': 0,'6': 1,'7': 1001,'8': n * 62,'9': launchId1,'10':'','11': 0,'12':'null'}
              c = {'0': Seq,'1': 'V1_AND_MINISDK_1.5.3_0_RELEASE_B','2': deviceInfo,'3': busiBuff,'4': traceid,'5':'mini_app_growguard','6': 'JudgeTiming','7': a,'8':'null','9': 'null','10': 0}
              qurl = 'https://q.qq.com/mini/OpenChannel?Action=input&Nonce='+nonce+'&PlatformID=2001&SignatureMethod=HmacSHA256&Timestamp='+str(nowtime)
              Signature = get_sign(qurl, 'test')
              hashInBase64 = str(base64.b64encode(Signature.encode("utf-8")), encoding ="utf-8")
              headers = {
            'User-Agent': 'ChinaUnicom4.x/300.0 CFNetwork/1220.1 Darwin/20.3.0',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
              client.headers.update(headers)
              qurl = 'https://q.qq.com/mini/OpenChannel?Action=input&Nonce='+nonce+'&PlatformID=2001&SignatureMethod=HmacSHA256&Timestamp='+str(nowtime)+'&Signature='+hashInBase64
              infoEncodeMessage =json.dumps(c).encode().hex()
              playgame = requests.post(qurl,data=infoEncodeMessage)
              time.sleep(1)
              print(infoEncodeMessage)
              print(playgame.json())
              n = n + 1
            
            n = 1
            a = {'1':username,'2':jwt,'3':'2001','4': 0,'5':'101794394'}
            busiBuff = {'1':urllist[forNum],'2': 0}
            c = {'1':Seq,'2':'V1_AND_MINISDK_1.5.3_0_RELEASE_B','3':deviceInfo,'4':json.dumps(busiBuff),'5':traceid,'6':'mini_app_info','7':'GetAppInfoByLink','8':a,'9':'null','10': 'null','11': 1}
            
            qqurl = 'https://q.qq.com/mini/OpenChannel?Action=input&Nonce='+nonce+'&PlatformID=2001&SignatureMethod=HmacSHA256&Timestamp='+str(nowtime)
            Signature = get_sign(qqurl, "test")
            hashInBase64 = str(base64.b64encode(Signature.encode("utf-8")), encoding ="utf-8")
            qqurl = 'https://q.qq.com/mini/OpenChannel?Action=input&Nonce='+nonce+'&PlatformID=2001&SignatureMethod=HmacSHA256&Timestamp='+str(nowtime)+'&Signature='+hashInBase64
            headers = {
            'User-Agent': 'ChinaUnicom4.x/300.0 CFNetwork/1220.1 Darwin/20.3.0',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            client.headers.update(headers)
            qqurl = 'https://q.qq.com/mini/OpenChannel?Action=input&Nonce='+nonce+'&PlatformID=2001&SignatureMethod=HmacSHA256&Timestamp='+str(nowtime)+'&Signature='+hashInBase64
            infoEncodeMessage =   json.dumps(c).encode().hex()
            playgame = requests.post(qurl,data=infoEncodeMessage)
            print(playgame.json())
            time.sleep(1)
            
            #领取流量接口
            flowdata = {'methodType':'flowGet','deviceType':'iOS','clientVersion':'8.0200','gameId':idlist[forNum]}
            flowinfo = client.post('https://m.client.10010.com/producGameApp',data=flowdata)
            flowinfo.encoding = 'utf-8'
            flowinfo = flowinfo.json()
            if flowinfo['msg'] == '流量领取接口请求成功':
                logging.info('【玩游戏3G】:'+namelist[forNum]+' +100MB')
            else:
                logging.info('【玩游戏3G】:'+namelist[forNum]+' 领取失败')
            forNum = forNum + 1
        
    except Exception as e:
        print(traceback.format_exc())
        logging.error('【游戏3GB】: 错误，原因为: ' + str(e))
        
#python实现HmacSHA256加密算法
def get_sign(data, key):
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    sign = base64.b64encode(hmac.new(key, message, digestmod='sha256').digest())
    sign = str(sign, 'utf-8')
    print(sign)
    return sign
    