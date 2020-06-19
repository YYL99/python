import requests
from lxml import etree

url = 'https://www.qiushibaike.com/'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0\
		.2743.116 Safari/537.36',
	'Accept-Language': 'zh-CN,zh;q=0.8'
}
res = requests.get(url, headers=headers).text
html = etree.HTML(res)
result = html.xpath('//div//a[@class="recmd-content"]/@href')
print(result)
# https://www.qiushibaike.com/article/123125805

# for site in result:
# 	xurl = "https://www.qiushibaike.com" + site
# 	resp = requests.get(xurl, headers=headers).text
# 	html2 = etree.HTML(resp)
# 	result2 = html2.xpath("//div[@class='content']")
# 	print(result2[0].text)