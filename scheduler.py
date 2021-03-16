# -*- coding: utf-8 -*-
import os
import sys
import logging
import importlib
import random
import time
import main
import json


#获取任务列表
def listdir(path, list_name): 
  for file in os.listdir(path): 
    if os.path.isdir(file): 
      listdir(file, list_name) 
    elif os.path.splitext(file)[1]=='.py': 
      list_name.append(os.path.splitext(file)[0])
      #list_name.append(file_path) 

def runscheduler(client,username,num):
    # 检索任务数量
    tasklist=[]   
    listdir('./TaskList',tasklist)
    logging.info('【任务调度】: 当前任务数量' + str(len(tasklist)))
    forNum = 0
    for task in tasklist:
      user = main.readJson()
      if ('taskNum' in user[0]):
            taskNum = user[0]['taskNum']
      else:
            logging.error('Json未配置taskNum，停止运行')
            sys.exit()
      logging.info('【任务统计】: 已进行' + taskNum +'个任务')
      if forNum >= int(taskNum):
            logging.info('【任务分配】: ' + task)
            i = importlib.import_module('TaskList.'+task)
            i.main(client,username,num)
            resetJson('./','./',int(taskNum) + 1)
            forNum = forNum + 1
            dtime =random.randint(3,30)
            logging.info('【任务调度】: 延时进行' + str(dtime)+'秒')
            time.sleep(dtime)
      else:
            logging.info('【任务跳过】: ' + task)
            forNum = forNum + 1
      
      
#修改json函数
def resetJson(file_old,file_new,num):
    filename_rest = os.listdir(file_old)  # 获取需要读取的文件的名字
    L = []
    for rest in filename_rest:
        if os.path.splitext(rest)[1]=='.json':
            L.append(os.path.join(file_old,rest)) #创建文件路径
    for f11 in L:
        with open(f11,'r') as f:
            data = json.load(f)
            data[0]['taskNum'] = str(num)
            newpath = os.path.join(file_new,os.path.split(f11)[1])
            with open(newpath,'w') as f2:
                json.dump(data,f2)       # 写入f2文件到本地
