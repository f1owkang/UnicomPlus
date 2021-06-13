# -*- coding: utf-8 -*-
# @Time    : 2021/3/15
# @Author  : lxdebug,hyzaw
# @Email   : lxdebug@foxmail.com

import requests
import platform
import json
import subprocess


def getnetinfo(): 
    try:
        header = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1","Appect":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
        netinfo = requests.get('https://myip.ipip.net/json',headers=header).json()
        resdata = netinfo['data']
        ip = resdata['ip']
        country = resdata['location'][0]
        return ip,country
                
    except:
        netinfo = requests.get('http://ip-api.com/json/?lang=zh-CN').text
        ip = json.loads(netinfo).get('query')
        country = json.loads(netinfo).get('country')
        return ip,country

def ippass():
    ip,country = getnetinfo()
    if country == '中国':
        return True
    elif country == '台湾':
        return True
    elif country == '香港':
        return True
    else :
        return False

def system():
    if(platform.system()=='Windows'):
        return 'Windows'
    elif(platform.system()=='Linux'):
        return 'Linux'
    elif (platform.system() == 'Darwin'):
        return  'Darwin'
    else:
        return 'Other'

def cpu():
    return platform.machine()
    
def virtual():
    virtual_mode = str(subprocess.getoutput('systemd-detect-virt'))
    if virtual_mode == 'vmware':
        return True
    elif virtual_mode == 'microsoft':
        return True
    else:
        return False


   