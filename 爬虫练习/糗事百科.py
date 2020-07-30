from urllib.request import Request, urlopen
from fake_useragent import UserAgent
import ssl
from time import sleep

url = 'https://www.qiushibaike.com/8hr/page/{}/'
for i in range(1,100):
    headers = {'User-Agent':UserAgent().random}
    request = Request(url.format(i), headers=headers)\

    # context = ssl.create_default_context()
    response = urlopen(request)
    info = response.read().decode()

    with open('糗事百科数据/第{}页.html'.format(i), 'w', encoding='utf-8') as f:
        f.write(info)

    print('第{}页完成'.format(i))

    sleep(1)
