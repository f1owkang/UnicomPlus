# -*- coding: utf-8 -*-
# @Time    : 2021/3/15
# @Author  : lxdebug
# @Email   : lxdebug@foxmail.com

import requests
import platform
import re

#正则表达式

def getip(): 
    html_text = requests.get("https://myip.ipip.net").text
# （1）正则匹配方式 ip
    ip_text = re.search(u"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)", html_text) 
    return ip_text.group(1)
    
def getcountry():
    html_text = requests.get("https://myip.ipip.net").text
# （2）正则匹配方式 汉字
    country_text = re.search(u"[\u4e00-\u9fa5]", html_text) 
    country = country_text.group(6)+country_text.group(7)
    return country
    
def system():
    if(platform.system()=='Windows'):
        return 'windows'
    elif(platform.system()=='Linux'):
        return 'linux'
    else:
        return 'other'

   