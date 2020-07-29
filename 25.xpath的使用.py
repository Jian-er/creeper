from fake_useragent import UserAgent
import requests
from lxml import etree

url = 'https://www.qidian.com/rank/yuepiao?style=1'

headers = {'User-Agent':UserAgent().random}

response = requests.get(url, headers=headers)

e = etree.HTML(response.text)
names = e.xpath('//h4/a/text()')
authors = e.xpath("//p[@class='author']/a[@class='name']/text()")

for name, author in zip(names, authors):
    print(name, ':', author)