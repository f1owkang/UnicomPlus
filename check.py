# -*- coding: utf-8 -*-
# @Time    : 2021/3/15
# @Author  : lxdebug
# @Email   : lxdebug@foxmail.com

import socket

#UDP 协议来实现的，生成一个UDP包，把自己的 IP 放如到 UDP 协议头中，然后从UDP包中获取本机的IP，经常调用比较耗时！


def getip(): 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
    
    
def getcountry():
    url = 'http://ip-api.com/json/'   
    url = url + getip()
    response = requests.get(url)
    strpp={}                  #定义一个字典strpp   
    strpp=response.json()    #把英文网站json接口返回值传给字典strpp
    country = strpp.get('country'))
    return country
   