from urllib import request
import urllib
import time

'''https://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
https://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150'''


def loadPage(url, filename):
	print("正在下载" + filename)
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 SE 2.X MetaSr 1.0"}
	req = request.Request(url, headers=headers)
	return request.urlopen(req).read()

def writePage(html, filename):
	print("正在保存" + filename)
	with open(filename, "wb") as f:
		f.write(html)
	print("--------------------------------")

def tiebaSpider(url, beginPage, endPage):
	for page in range(beginPage, endPage + 1):
		pn = (page - 1) * 50
		filename = "e:/第" + str(page) + "页.html"
		fullurl = url + "&pn=" +str(pn)
		html = loadPage(fullurl, filename)
		writePage(html, filename)
		print("谢谢使用")

if __name__ == "__main__":
	kw = input("请输入需要爬取的贴吧名：")
	beginPage = int(input("请输入起始页："))
	endPage = int(input("请输入结束页："))

	url = "http://tieba.baidu.com/f?"
	key = urllib.parse.urlencode({"kw": kw})
	fullurl = url + key
	tiebaSpider(fullurl, beginPage, endPage)

time.sleep(6)
