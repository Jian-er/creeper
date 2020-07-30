import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from queue import Queue
from random import choice

def get_html(url):
    headers = {"User-Agent": UserAgent().random}
    proxy = [
        {"http":"115.221.244.4:9999"},
        {"http":"60.205.132.71:80"},
        {"http":"125.108.104.46:9000"},
    ]
    response = requests.get(url, headers=headers, proxies=choice(proxy))
    if response.status_code == 200:
        response.encoding = 'urf-8'
        return response.text
    else:
        return False

def get_detail_url(html, detail_url_q):
    soup = BeautifulSoup(html)
    name = soup.find("a", class_='')


def get_data():
    pass

if __name__ == '__main__':
    detail_url_q = Queue()
    index_url = 'https://maoyan.com/films?showType=3&offset=0'
    index_html = get_html(index_url)
    get_detail_url(index_html, detail_url_q)