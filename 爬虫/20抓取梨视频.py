import requests

# 防盗链处理

# 1.拿到 contId
url = 'https://www.pearvideo.com/video_1031767'
contId = url.split('_')[1]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    # 防盗链 溯源 溯源本次请求的上一级
    'Referer': 'https://www.pearvideo.com/video_1031767'
}

videoStatusURL = 'https://www.pearvideo.com/videoStatus.jsp?contId=1031767&mrd=0.5434291548899366'

resp = requests.get(videoStatusURL,headers = headers)

data_dict = resp.json()

data_systemTime = data_dict['systemTime']

srcUrl_lict = data_dict['videoInfo']['videos']['srcUrl'].split(data_systemTime)

print(srcUrl_lict)

download_url = srcUrl_lict[0] + 'cont-' +contId + srcUrl_lict[1]

print(download_url)

with open('鸭梨视频.mp4',mode='wb') as w:
    w.write(requests.get(download_url).content)
