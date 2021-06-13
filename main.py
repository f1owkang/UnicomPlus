# -*- coding: utf-8 -*-
import notify
import login
import requests
import json
import logging
import traceback
import check
import sys
import os

#引入任务模块
import scheduler

#用户登录全局变量
client = None
banlist = [18386000638]

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
        logging.error('1.请检查填写是否正确。')
        logging.error('2.填写之前，是否在网站验证过Json格式的正确性。')


#创建文件config.json
#file_path：文件路径
def newconfig(file_path):
    f=open(file_path,"a")
    f.write('''
    
    [
        {
            "username": "手机号（必填）",
            "password": "服务密码（必填）",
            "appId": "appId（必填）",
            "email": "邮箱（选填，不填请删除此行）",
            "lotteryNum": "抽奖次数（选填，不填请删除此行）注意 下方taskNum请勿删除！",
            "taskNum":"0",
            "dingtalkWebhook": "钉钉通知 https://oapi.dingtalk.com/robot/send?access_token=xxxx（选填，不填请删除此行）",
            "Bark": {
                "Barkkey": "（选填，不填请删除 Bark 对象）",
                "Barksave": "//是否需要保存推送信息到历史记录，1 为保存，其他值为不保存。（选填，不填请删除 Bark 对象）"
            },
            "telegramBot": {
                "tgToken": "Tg通知 token（选填，不填请删除 telegramBot 对象）",
                "tgUserId": "Tg通知 群组Id（选填，不填请删除 telegramBot 对象）"
            },
            "pushplusToken": "push+ token（选填，不填请删除此行）",
            "enterpriseWechat": {
                "id": "企业ID（选填，不填请删除 enterpriseWechat 对象）",
                "agentld": "企业微信自建应用AgentId（选填，不填请删除 enterpriseWechat 对象）",
                "secret": "企业微信自建应用Secrets（选填不填请删除 enterpriseWechat 对象）"
            },
            "IFTTT": {
                "apiKey": "IFTTT Webhook key",
                "eventName": "unicom_task",
                "subjectKey": "比如value1",
                "contentKey": "比如value2"
            }
        }
    ]
    
    ''')
    f.close


def main(event, context):
    ip,country=check.getnetinfo()
    logging.info('【地址自检】: ' + ip +'（'+ country+'）')
    logging.info('【环境自检】: ' + check.system()+'('+check.cpu()+')')
    if not check.ippass():
        logging.error('【地址异常】:您的地址异常，退出')
        sys.exit()
    if check.system() == 'Linux':
        if check.virtual():
            logging.error('【环境异常】:环境异常，退出')
            sys.exit()
        
    #配置检测生成
    if not os.path.isfile('config.json'):
        newconfig('./config.json')
        logging.error('【配置异常】:配置不存在已自动生成，请修改后使用')
        sys.exit()
    users = readJson()
    #黑名单处理逻辑
    for user in users:
        for banuser in banlist:
            if banuser == user['username']:
                logging.error('登陆失败，请提issue反馈')
                sys.exit()
        #清空上一个用户的日志记录
        open('./log.txt',mode='w',encoding='utf-8')
        global client
        client = login.login(user['username'],user['password'],user['appId'])
        username = user['username']
        if ('lotteryNum' in user):
            lotteryNum = user['lotteryNum']
        else:
            lotteryNum = 0
        #任务调度代码
        if client != False:
            scheduler.runscheduler(client,username,lotteryNum)
        else:
            logging.error('发生登陆错误，退出')
            sys.exit()
        scheduler.resetJson('./','./',0)
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
        if('Bark' in user):
            notify.sendBark(user['Bark'])
            
#主函数入口
if __name__ == '__main__':
    main("","")
