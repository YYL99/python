from urllib import request
import urllib
import re

def Translation(key):
	formdata = {
	"i": key,
	"from": "AUTO",
	"to": "AUTO",
	"smartresult": "dict",
	"client": "fanyideskweb",
	"salt": "15895274879365",
	"sign": "eb1b1d6372311bc203a1284b2ea798bf",
	"ts": "1589527487936",
	"bv": "cc652a2ad669c22da983a705e3bca726",
	"doctype": "json",
	"version": "2.1",
	"keyfrom": "fanyi.web",
	"action": "FY_BY_REALTlME",
	"typoResult":"false"
	}

	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	headers = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"}
	data = urllib.parse.urlencode(formdata).encode(encoding='utf-8')
	req = request.Request(url, data=data, headers=headers)
	reponse = request.urlopen(req).read().decode()
	t = r'tgt":"(.*?)"}]]'
	result = re.findall(t, reponse)
	print(result[0])

if __name__ == '__main__':
	while 1:
		key = input("请输入查询单词：")
		if key == "退出":
			break
		else:
			Translation(key)
