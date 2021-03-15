import login
import requests
import logging
import traceback
import notify

import TaskList.DailyWotree as Dwotree
import TaskList.DailySignin as Dsignin
import TaskList.DailyOneg as Doneg

#用户登录全局变量
client = None


#读取用户配置信息
#错误原因有两种：格式错误、未读取到错误
def readJson():
    try:
        #用户配置信息
        with open('./config.json','r') as fp:
            users = json.load(fp)
            return users
    except Exception as e:
        print(traceback.format_exc())
        logging.error('账号信息获取失败错误，原因为: ' + str(e))
        logging.error('1.请检查是否在Secrets添加了账号信息，以及添加的位置是否正确。')
        logging.error('2.填写之前，是否在网站验证过Json格式的正确性。')


def main(event, context):
    users = readJson()
    for user in users:
        #清空上一个用户的日志记录
        open('./log.txt',mode='w',encoding='utf-8')
        global client
        client = login.login(user['username'],user['password'],user['appId'])
        if client != False:
        
            #日常任务 沃之树
            Dwotree.woTree_task()
            #日常任务 签到
            Dsignin.daySign_task(user['username'])
            #日常任务 一天1g
            Doneg.dayOneG_Task()
            
            
           
        if ('email' in user) :
            notify.sendEmail(user['email'])
        if ('dingtalkWebhook' in user) :
            notify.sendDing(user['dingtalkWebhook'])
        if ('telegramBot' in user) :
            notify.sendTg(user['telegramBot'])
        if ('pushplusToken' in user):
            notify.sendPushplus(user['pushplusToken'])
        if('enterpriseWechat' in user):
            notify.sendWechat(user['enterpriseWechat'])
        if('IFTTT' in user):
            notify.sendIFTTT(user['IFTTT'])
        if('Barkkey' in user):
            notify.sendBarkkey(user['Barkkey'])

#主函数入口
if __name__ == '__main__':
    main("","")
