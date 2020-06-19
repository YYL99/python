from urllib import request
import urllib

q = {"q": "你好"}
header = {"User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
url = "https://www.so.com/s?"
qq = urllib.parse.urlencode(q)
url = url + qq
req = request.Request(url, headers=header)
reponse=request.urlopen(req).read().decode()
print(reponse)
