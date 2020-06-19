import requests
import re
import time

#
#http://mp32.9ku.com/upload/128/2020/01/22/1001940.mp3
#http://mp32.9ku.com/upload/128/2019/06/11/893217.mp3
#http://mp32.9ku.com/upload/128/2019/06/20/890625.mp3
#http://mp3.9ku.com/hot/2004/12-14/63537.mp3

url = "http://www.9ku.com/play/890625.htm"
res = requests.get(url).text
#print(res)



a = re.compile(r'"pubDate": "+\d+\-+\d+\-+\d+T')
b = a.findall(res)
t = re.findall(r'"pubDate": (.*?)T', b[0])
c = re.compile(r'\d\d').findall(t[0])
year = c[0]+c[1]
month = c[-2]
day = c[-1]
print(year, month, day)

f = re.compile(r'\d\d\d\d\d\d\d\d+/').findall(res)
data = re.compile(r'\d\d\d\d\d\d\d\d').findall(f[0])
year = data[0][0:4]
month = data[0][4:6]
day = data[0][6:8]
print(year, month, day)
'''
try:
	Data = year +"/"+ month +"/"+ day +"/"
	songurl = "http://mp32.9ku.com/upload/128/" + Data + str(songID[i]) + ".mp3"
	data = requests.get(songurl).content
except:
	Data = year +"/"+ month +"-"+ day +"/"
	songurl = "http://mp32.9ku.com/upload/128/" + Data + str(songID[i]) + ".mp3"
	data = requests.get(songurl).content


#songurl = "http://mp3.9ku.com/hot/" + year +"/"+ month +"-"+ '14' +"/" + "63537" + ".mp3"'''
'''songurl = "http://mp32.9ku.com/upload/128/2018/03/28/877422.mp3"
data = requests.get(songurl).content
with open("E:\\music\\1\\日常喜欢你.mp3", "wb") as f:
	f.write(data)'''