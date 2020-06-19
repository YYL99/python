from urllib import request
import random

proxylist = [
	{"http": "61.178.149.237:59042"},
	{"http": "123.132.232.254:37638"},
	{"http": "218.93.119.165:9002"},
	{"http": "221.13.156.158:55443"}
]
proxy = random.choice(proxylist)

proxyHandler = request.ProxyHandler(proxy)

opener = request.build_opener(proxyHandler)
request.install_opener(opener)
req = request.Request("http://www.baidu.com")
reponse = opener.open(req).read()
print(reponse)