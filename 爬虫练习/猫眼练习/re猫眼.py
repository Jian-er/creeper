import requests
from fake_useragent import UserAgent
from random import choice
from re import findall

def get_html(url):
    headers = {'User-Agent': UserAgent().random}
    proxy = [
        {'http': "163.204.245.204:9999"},
        {'http': "110.243.26.245:9999"},
        {'http': "123.169.125.114:9999"},
        {'http': "171.13.137.32:9999"},
    ]
    response = requests.get(url, headers=headers, proxies=choice(proxy))
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    return False

def get_detail_url(html):
    detail_url_a = findall(r'<div.+class="movie-item film-channel">\s+<a href="(/films/\d+)"', html)
    detail_url_list = ['https://maoyan.com{}'.format(detail_url) for detail_url in detail_url_a]
    return detail_url_list

def rinse_data(data_list):
    pass

def get_data(html):
    name = findall(r'<h1 class="name">(.+)</h1>', html)
    types = findall(r'<a class="text-link".+> (.+) </a>', html)
    actors = findall(r'<li class="celebrity actor".+>\s+<a.+>\s+<img.+>\s+</a>\s+<div class="info">\s+<a.+class="name">\s+(.+)\s+</a>', html)
    return {'name':name, 'types':types, 'actors':actors}

if __name__ == '__main__':
    url = 'https://maoyan.com/films?showType=3&offset=0'
    index_html = get_html(url)
    detail_url_list = get_detail_url(index_html)
    for detail_url in detail_url_list:
        detail_html = get_html(detail_url)
        print(get_data(detail_html))