import requests
from fake_useragent import UserAgent
from random import choice
from bs4 import BeautifulSoup
import lxml

url = 'https://www.qidian.com/rank/collect?page={}'

proxy_list = [
    {'http':'47.94.89.87:3128'},
    {'http':'119.108.188.81:9999'},
    {'http':'113.194.134.216:9999'},
    {'http':'113.194.134.111:9999'},
    {'http':'113.194.135.84:9999'},
    {'http':'60.168.207.21:1133'},
]

for i in range(1,21):
    response = requests.get(url.format(i), headers={'User-Agent':UserAgent().random}, proxies=choice(proxy_list))
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find_all('a')
    # author = soup;.
    # time = soup
    print(title)
