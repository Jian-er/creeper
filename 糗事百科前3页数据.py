from urllib.request import Request, urlopen
from time import sleep
import ssl
from fake_useragent import UserAgent

url = 'https://www.qiushibaike.com/8hr/page/{}/'

ua = UserAgent()

for i in range(1,4):
    headers = {
        'User-Agent':ua.random
    }
    request = Request(url.format(i), headers=headers)
    context = ssl._create_unverified_context()
    response = urlopen(request, context=context)
    info = response.read().decode()

    with open('糗事百科数据\糗事百科第{}页数据.html'.format(i), 'w', encoding='utf-8') as f:
        f.write(info)

    sleep(1)

    print('第{}页完成'.format(i))