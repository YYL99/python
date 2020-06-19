from urllib import request
import re
import random

url = r"http://www.baidu.com/"

agent1 = "Mozilla/5.0 (Linux; Android 8.1.0;ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)"
agent2 = "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
agent3 = "Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gec ko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.3 6 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)"
agent4 = "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHT ML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrows er/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(D ingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel /227200 language/zh-CN"
agent5 = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"

list1 = [agent1,agent2,agent3,agent4,agent5]

agent = random.choice(list1)
print(agent)

#手机的User-Agent
header = {
	"User-Agent": agent
}

req = request.Request(url,headers=header)

reponse = request.urlopen(req).read().decode()

p = r"<title>(.*?)</title>"
data = re.findall(p,reponse)

print(data[0])
