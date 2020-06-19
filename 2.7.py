from urllib import request
import re

url = "http://www.baidu.com"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
req = request.Request(url, headers=header)

http_handler = request.HTTPHandler()

opener = request.build_opener(http_handler)

#reponse = opener.open(req).read().decode()
request.install_opener(opener)
reponse = request.urlopen(req).read().decode()

t = "<title>(.*?)</title>"
data = re.findall(t,reponse)
print(data)