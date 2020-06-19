from lxml import etree

html = etree.parse(r'E:\桌面\python\hello.html')

# result = etree.tostring(html, encoding="utf-8").decode()
# print(result)

# result = html.xpath("//a")
# print(result[0].text)

# result = html.xpath("//li/a[@href='link2.html']")
# print(result[0].text)

# result=html.xpath("//li[@class='item-88']")
# print(result)

# result = html.xpath("//li/a/@href")
# for i in result:
# 	requests.get(i)

# result1 = html.xpath("//li/a")
# result2 = html.xpath("//li//span")
# result3 = html.xpath("//li/a//@class")
# print(result3)

# result1 = html.xpath("//li[last()-1]/a")
# print(result1[0].text)
# result2 = html.xpath("//li/a")
# print(result2[-2].text)
result3=html.xpath("//*[@class='bold']")
print(result3[0].tag)

