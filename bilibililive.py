import requests
import json
from  time import sleep
from mirai import Startup
from mirai.models import AtAll
from mirai.exceptions import ApiError

sleepTime = 30
groupINFO = [[[389391931],[69731917,'',"0","0",""]],#[[[群号，群号,......],[b站号,'',"0","0",""]],[[群号，群号,......],[b站号,'',"0","0",""]],......]
            [[517814646],[1553878284,'',"0","0",""]]]
def getLive(i):
    global groupINFO
    url = "https://api.bilibili.com/x/space/acc/info?mid="+str(groupINFO[i][1][0])
    pythondy = json.loads(requests.get(url).text)  # json对象转换为python字典
    groupINFO[i][1][1]=pythondy['data']['name']
    groupINFO[i][1][2] = str(pythondy['data']['live_room']['liveStatus'])
    groupINFO[i][1][4] = str(pythondy['data']['live_room']['url'])
async def Print(bot):
    global groupINFO
    for i in range(0,groupINFO.__len__()):
        if groupINFO[i][1][2] != groupINFO[i][1][3]:
            groupINFO[i][1][3] = groupINFO[i][1][2]
            for group in groupINFO[i][0]:
                try:
                    if groupINFO[i][1][2]=="1":
                        await bot.send_group_message(group, [groupINFO[i][1][1]+"开始直播了\n地址："+groupINFO[i][1][4],AtAll()])
                    elif groupINFO[i][1][2]=="0":
                        await bot.send_group_message(group, [groupINFO[i][1][1]+"直播结束了\n",AtAll()])
                except ApiError:
                    if groupINFO[i][1][2]=="1":
                        await bot.send_group_message(group, [groupINFO[i][1][1]+"开始直播了\n地址："+groupINFO[i][1][4]])
                    elif groupINFO[i][1][2]=="0":
                        await bot.send_group_message(group, [groupINFO[i][1][1]+"直播结束了\n"])
def main(bot):
    @bot.on(Startup)
    async def get_live(event:Startup):
        while True:
            for i in range(0,groupINFO.__len__()):
                getLive(i)
                await Print(bot)
            # print ("循环成功")
            sleep(sleepTime)
