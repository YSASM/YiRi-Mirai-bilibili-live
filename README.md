# YiRi-Mirai-bilibili-live
## 1.安装YiriMiral

pip install yiri-mirai

详细参考https://yiri-mirai.wybxc.cc/docs/intro

## 2.将bot.py放入mcl同级目录下（为了方便寻找插件路径）

## 3.在plugins目录下建立一个pyPlugins文件夹，将jytime.py放进去

## 4.bot.py配置：

```  
from mirai import Mirai, WebSocketAdapter,GroupMessage

from plugins.pyPlugins import jytime,bilibililive#这样的方式引用插件

if __name__ == '__main__':

    bot = Mirai(
    
        qq=123456,#你机器人的qq 
        
        adapter=WebSocketAdapter(
        
            verify_key='12345678', host='localhost', port=8008#这里设置可以看官方文档或者往下看介绍
            
        )
        
    )
    
    jytime.main(bot)#这玩意要写在bot.run()前面
    
    '''
    
    多个插件就
    
    jytime.main(bot)
    
    bilibililive.main(bot)
    
    bilibililive.main(bot)...
    
    这样一个个列出来就行
    
    '''
    
    bot.run()
```  
    
## 5.setting.yum

mirai-api-http的配置文件，在config\net.mamoe.mirai-api-http里

配置如下：

```  
adapters:

  - ws
  
debug: false

enableVerify: true

verifyKey: 12345678

singleMode: false

cacheSize: 4096

adapterSettings:

  ws:
  
    host: localhost
    
    port: 8008
    
    reservedSyncId: -1
```  
    
## 最后是如何使用
按照注释更改bilibililive.py中以下几个参数即可
'''
sleepTime = 30 #检测频率/秒
groupINFO = [[[0000],[0000,'',"0","0",""]],#[[[群号，群号,......],[b站号,'',"0","0",""]],[[群号，群号,......],[b站号,'',"0","0",""]],......]
            [[0000],[0000,'',"0","0",""]]]
'''

