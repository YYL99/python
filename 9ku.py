import requests
import re
import time

#http://www.9ku.com/douyin/
#<a target="_1" href="/play/471298.htm" class="songName ">苏幕遮 </a>
#<a target="_1" href="/play/1002010.htm" class="songName ">世界这么大还是遇见你 </a>
#http://www.9ku.com/play/471298.htm
#http://mp32.9ku.com/upload/128/2012/09/06/471298.mp3
#http://www.9ku.com/play/1002010.htm
#http://mp32.9ku.com/upload/128/2020/02/13/1002010.mp3
#http://www.9ku.com/play/1001940.htm
#http://mp32.9ku.com/upload/128/2020/01/22/1001940.mp3
#"pubDate": "2012-09-06T15:06:50",
#"pubDate": "2020-02-13T00:00:00",
#http://mp32.9ku.com/upload/128/2020/02/13/1002002.mp3
#http://mp32.9ku.com/upload/128/2017/08/14/864839.mp3
#http://mp32.9ku.com/upload/128/2020/02/13/1002010.mp3
#http://mp32.9ku.com/upload/128/2020/02/13/1002002.mp3


url = "http://www.9ku.com/douyin/"
html = requests.get(url)
res = html.text
pat1 = r'class="songName ">(.*?) </a>'
pat2 = r'<a target="_1" href="/play/(.*?).htm'
songName = re.findall(pat1, res)
songID = re.findall(pat2, res)
#print(len(songID),len(songName))
#len(songID)-30

for i in range(0, 10):
	url = r"http://www.9ku.com/play/" + str(songID[i]) + ".htm"
	html = requests.get(url)
	res = html.text
	a = re.compile(r'"pubDate": "+\d+\-+\d+\-+\d+T')
	b = a.findall(res)
	t = re.findall(r'"pubDate": (.*?)T', b[0])
	#print(t)
	c = re.compile(r'\d\d').findall(t[0])
	#print(c)
	year = c[0]+c[1]
	month = c[-2]
	day = c[-1]
	#print(year1, month1, day1)

	f = re.compile(r'\d\d\d\d\d\d\d\d+/').findall(res)
	#print(f)
	if len(f) != 0:
		data = re.compile(r'\d\d\d\d\d\d\d\d').findall(f[0])
		#print(data)
		year = data[0][0:4]
		month = data[0][4:6]
		day = data[0][6:8]
		#print(year2, month2, day2)
	#else:
		#print(year1, month1, day1)

	Data = year +"/"+ month +"/"+ day +"/"
	songurl = "http://mp32.9ku.com/upload/128/" + Data + str(songID[i]) + ".mp3"
	Mp3 = requests.get(songurl).content
	#print(len(Mp3))
	if len(Mp3) < 1000:
		Data = year +"/"+ month +"-"+ day +"/"
		songurl = "http://mp3.9ku.com/hot/" + Data + str(songID[i]) + ".mp3"
		Mp3 = requests.get(songurl).content
	
	print("正在下载第",i+1,"首")
	with open("E:\\music\\1\\{}.mp3".format(songName[i]), "wb") as f:
		f.write(Mp3)
	time.sleep(0.5)




