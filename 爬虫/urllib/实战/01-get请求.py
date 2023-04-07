from urllib import request


url = 'https://vd3.bdstatic.com/mda-nhkdc06bp7tebbc1/haokan_t/dash/1661153161784532848/mda-nhkdc06bp7tebbc1-1.mp4'

# with语句读写
# resp = request.urlopen(url)
#
# with open('01.mp4',mode='wb') as f:
#     f.write(resp.read())

request.urlretrieve(url,'02.mp4')


