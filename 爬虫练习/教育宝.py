import requests
from fake_useragent import UserAgent
from time import sleep

url = 'https://jn.jiaoyubao.cn/edu/jnynkhjy/'

headers = {
    'User-Agent':UserAgent().random
}
porxy = {
    'http':'113.194.136.219:9999'
}

i = 0
while True:
    i += 1
    response = requests.get(url, headers=headers, proxies=porxy)
    print("第{}次请求".format(i))
    sleep(3)