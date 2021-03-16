# -*- coding: utf-8 -*-
import os
import logging
import importlib
import random
import time

def listdir(path, list_name): 
  for file in os.listdir(path): 
    file_path = os.path.join(path, file) 
    if os.path.isdir(file_path): 
      listdir(file_path, list_name) 
    elif os.path.splitext(file_path)[1]=='.py': 
      list_name.append(os.path.splitext(file_path)[0])
      #list_name.append(file_path) 

def runscheduler(client,username,num):
    # 检索任务数量
    tasklist=[]   
    listdir('./TaskList',tasklist)
    logging.info('【任务调度】: 当前任务数量' + str(len(tasklist)))
    for task in tasklist:
      logging.info('【测试】: ' + task)
      i = importlib.import_module('TaskList.'+task)
      i.main(client=client,username=username,n=num)
      dtime =random.randint(30,300)
      logging.info('【任务调度】: 延时进行' + str(dtime)+'秒')
      time.sleep(dtime)