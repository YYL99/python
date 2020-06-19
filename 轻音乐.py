import re
import requests
import time

#page = int(input("请输入要爬取的页数："))
#http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
#http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
#http://f2.htqyy.com/play7/1618/mp3/5 音乐
#http://f2.htqyy.com/play7/93/mp3/5
#http://www.htqyy.com/genre/musicList/1?pageIndex=1&pageSize=20&order=hot
#http://www.htqyy.com/genre/musicList/1?pageIndex=2&pageSize=20&order=hot

songID = []
songName = []

for i in range(0,2):
	url = "http://www.htqyy.com/genre/musicList/1?pageIndex="+str(i)+"&pageSize=20&order=hot"
	html = requests.get(url)
	strr=html.text
	pat1 = r'title="(.*?)" sid='
	pat2 = r'sid="(.*?)"'
	songid = re.findall(pat2, strr)
	songname = re.findall(pat1, strr)
	songID.extend(songid)
	songName.extend(songname)
#print(songID)
#print(songName)

for i in range(0,len(songID)):
	songurl = "http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/5"
	songname = songName[i]
	data = requests.get(songurl).content
	print("正在下载第",i+1,"首")
	with open("E:\\music\\{}.mp3".format(songname), "wb") as f:
		f.write(data)
	time.sleep(0.5)