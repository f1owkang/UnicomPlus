from . import DailyWotree,DailySignin,DailyOneG,DailyLuck,DailyCollectflow,DailyGamecenter,DailyOpenbox,DailyPoints,DailyPointsluck,ShortOlympic,ToolSupport

def run(client,username,lotteryNum):
    #日常任务 沃之树
    DailyWotree.woTree_task(client)
    #日常任务 签到
    DailySignin.daySign_task(client,username)
    #日常任务 一天1g
    DailyOneG.dayOneG_Task(client)
    #日常任务 天天抽奖
    DailyLuck.luckDraw_task(client)
    #日常任务 240M流量
    DailyCollectflow.collectFlow_task(client)
    #日常任务 游戏中心打卡
    DailyGamecenter.gameCenterSign_Task(client,username)
    #日常任务 开宝箱每天100M
    DailyOpenbox.openBox_task(client)
    #日常任务 100定向积分
    DailyPoints.day100Integral_task(client)
    #日常任务 定向积分抽奖
    DailyPointsluck.pointsLottery_task(client,lotteryNum)
    #限时任务 冬奥定向积分
    ShortOlympic.dongaoPoints_task(client)
    #工具类
    ToolSupport.getIntegral(client)