# -*- coding: utf-8 -*-
import os
import logging
import importlib
import random
import time

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
    for task in tasklist:
      logging.info('【任务分配】: ' + task)
      i = importlib.import_module('TaskList.'+task)
      i.main(client,username,num)
      dtime =random.randint(30,300)
      logging.info('【任务调度】: 延时进行' + str(dtime)+'秒')
      time.sleep(dtime)