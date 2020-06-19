from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">张三</a></li>
         <li class="item-1"><a href="link2.html">李四</a></li>
         <li class="item-inactive"><a href="link3.html">王五</a></li>
         <li class="item-1"><a href="link4.html">赵六</a></li>
         <li class="item-0"><a href="link5.html">老七</a> 
     </ul>
 </div>
'''

html = etree.HTML(text)
result = etree.tostring(html, encoding="utf-8").decode()

print(result)