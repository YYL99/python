import requests
import re


#http://changyongdianhuahaoma.51240.com/

url = "http://changyongdianhuahaoma.51240.com/"
headers = {
	"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0"
}

res = requests.get(url, headers=headers).text
# print(res)
pat1 = r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2 = r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'
data1 = re.compile(pat1).findall(res)
data2 = re.compile(pat2).findall(res)
# print(data1, data2)

resultlist = []
for i in range(0,len(data1)):
	resultlist.append(data1[i] + ":" + data2[i])
print(resultlist)