import re

'''
a = "湖南湖北广东广西"
pat = "湖北"
result = re.search(pat, a)
print(result)


b = "13678927639"
pat2 = r"\d\d\d\d\d\d\d\d\d\d\d"

print(re.search(pat2, b))
'''

#匹配中文[\u4e00-\u9fa5]
#数字[0-9]
#英文[a-z][A-Z]
#原子表[]定义一组平等的原子

#元字符  . ^ $ * ? +
#匹配固定次数{n,m}
#多个表达式 |
#分组 ()  .group()
#贪婪模式 非贪婪模式?
#compile 模式修正符:(忽略大小写) re.I
#math 从开头开始匹配 search 任意位置 两者都匹配一次

#split() 按照能够匹配的字符串分割后返回列表
#sub() 用于替换



