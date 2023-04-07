import re,requests

# URL = "https://silkroad.csdn.net/api/v2/assemble/list/channel/search_hot_word"
#
# params = {
#     "new_hot_flag": 1,
#     "channel_name": "pc_hot_word",
#     "size": 20,
#     "user_name": "weixin_52946862",
#     "platform": "pc",
#     "imei": "10_4679031120-1653288684630-414707"
# }
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
# }
#
# resp = requests.get(url=URL,params=params,headers=headers)
# print(resp.json())
# resp.close()

text = """
            {"name": "xixicai", "type": "3", "url": "https://laisoyiba.com/mov/s/?sv=3&url="},
            {"name": "天翼", "type": "1,3", "url": "https://jsap.attakids.com/?url="},
            {"name": "综合/B站", "type": "1,3", "url": "https://jx.bozrc.com:4433/player/?url="},
            {"name": "m1907", "type": "1,2", "url": "https://z1.m1907.cn/?jx="},
            {"name": "Player-JY", "type": "1,3", "url": "https://jx.playerjy.com/?url="},
            {"name": "虾米", "type": "1,3", "url": "https://jx.xmflv.com/?url="},
            {"name": "OK解析", "type": "1,3", "url": "https://okjx.cc/?url="},
            {"name": "乐多", "type": "1,3", "url": "https://api.leduotv.com/wp-api/ifr.php?isDp=1&vid="},
            {"name": "yparse", "type": "1,2", "url": "https://jx.yparse.com/index.php?url="},
            {"name": "MAO", "type": "1,3", "url": "https://www.mtosz.com/m3u8.php?url="},
            {"name": "诺讯", "type": "1,3", "url": "https://www.nxflv.com/?url="},
            {"name": "M3U8TV", "type": "1,3", "url": "https://jx.m3u8.tv/jiexi/?url="},
            {"name": "爱豆", "type": "1,3", "url": "https://jx.aidouer.net/?url="},
            {"name": "夜幕", "type": "1,3", "url": "https://www.yemu.xyz/?url="},
            {"name": "BL", "type": "1,3", "url": "https://svip.bljiex.cc/?v="},
            {"name": "七彩", "type": "1,3", "url": "https://www.xymav.com/?url="},
            {"name": "人人迷", "type": "1,3", "url": "https://jx.blbo.cc:4433/?url="},
            {"name": "七哥", "type": "1,3", "url": "https://jx.mmkv.cn/tv.php?url="},
            {"name": "铭人云", "type": "1,3", "url": "https://parse.123mingren.com/?url="},
            {"name": "江湖云", "type": "1,3", "url": "https://api.jhdyw.vip/?url="},
            {"name": "4kdv", "type": "1,3", "url": "https://jx.4kdv.com/?url="},
            {"name": "1717", "type": "1,3", "url": "https://ckmov.ccyjjd.com/ckmov/?url="},
            {"name": "8090", "type": "1,3", "url": "https://www.8090g.cn/?url="},
            {"name": "qianqi", "type": "1,3", "url": "https://api.qianqi.net/vip/?url="},
            {"name": "laobandq", "type": "1,3", "url": "https://vip.laobandq.com/jiexi.php?url="},
            {"name": "playm3u8", "type": "1,3", "url": "https://www.playm3u8.cn/jiexi.php?url="},
            {"name": "无名小站", "type": "1,3", "url": "https://www.administratorw.com/video.php?url="},
            {"name": "CK", "type": "1,3", "url": "https://www.ckplayer.vip/jiexi/?url="},
            {"name": "盖世", "type": "1,3", "url": "https://www.gai4.com/?url="},
            {"name": "盘古", "type": "1,3", "url": "https://go.yh0523.cn/y.cy?url="},
            {"name": "Blbo", "type": "1,3", "url": "https://jx.blbo.cc:4433/?url="}
"""

resp = re.compile(r'{"name": "(?P<ID>.*?)", "type": "(?P<type>.*?)", "url": "(?P<URL>.*?)="},', re.S)  # re.S 匹配换行符
for i in resp.finditer(text):
    print(i.group("ID"))
    print(i.group("type"))
    print(i.group("URL"))
