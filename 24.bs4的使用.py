from bs4 import BeautifulSoup

html = """
<div class="content" name='aaa'>
<span>

<a href='www.baidu.com'>baidu</a>
我在汤臣一品担任销售经理一职，每天早上我都会给手下200多人开早会。<br><br>在汤臣一品售楼处下班后买了一包荷花烟，在公园的长椅上抽了起来。<br><br>旁边坐着一个大爷，我和他聊了一会儿天，然后给他发了根烟。<br><br>他一抽：“虽然是名贵的荷花，但是比我的烟还是差远了。”<br><br>只见他拿出一袋烟丝，烟纸，让我自己卷一根。<br><br>我卷了一根，抽了一下味道更浓郁，集成了各大名烟的优点。<br><br>我：“大爷，这烟能卖我一点吗？”<br><br>他：小伙子，咱俩有缘分，送你了，我大不了多捡半天烟头重新卷就行了。”

</span>

</div>
"""
# 创建一个bs4的对象
soup = BeautifulSoup(html, 'lxml')

print("--------------获取标签-----------------")
print(soup.span)
print(soup.div)

print("--------------获取属性-----------------")
print(soup.div.attrs)

print("--------------获取单个属性-----------------")
print(soup.div.get("name"))
print(soup.div["name"])
print(soup.a['href'])

print("--------------获取内容-----------------")
print(soup.a.string)
print(soup.a.text)