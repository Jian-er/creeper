import requests
from fake_useragent import UserAgent
from time import sleep
from urllib.parse import urlencode

url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'

name = input("请输入贴吧名称：")

proxy = {
    'http':'110.243.25.159:9999'
}

for i in range(0,100):
    response = requests.get(url.format(name, i*50), headers={"User-Agent":UserAgent().random}, proxies=proxy)
    with open('百度贴吧数据/{}贴吧数据第{}页.html'.format(name, i+1), 'w', encoding='utf-8') as f:
        f.write(response.text)

    print('百度贴吧数据/{}贴吧数据第{}页完成'.format(name, i+1))
    sleep(3)