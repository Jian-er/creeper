import requests
from fake_useragent import UserAgent
from time import sleep

url = 'http://www.zongheng.com/rank/details.html?rt=1&d=1&p={}'

for i in range(1,4):
    response = requests.get(url.format(i), headers={'User-Agent':UserAgent().random})
    info = response.text
    with open('纵横小说前三页数据/第{}页数据.html'.format(i), 'w', encoding='utf-8') as f:
        f.write(info)

    print('第{}页完成！'.format(i))
    sleep(2)
