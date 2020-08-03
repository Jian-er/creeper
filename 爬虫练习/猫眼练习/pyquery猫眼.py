import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq
from random import choice


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
        response.encoding = 'urf-8'
        return response.text
    else:
        return False

def get_detail_url(html):
    doc = pq(html)
    detail_url_a = doc('.movie-item.film-channel > a')
    detail_url_list = ["https://maoyan.com{}".format(detail_url.get("href")) for detail_url in detail_url_a]
    return detail_url_list

def rinse_data(data_list):
    data_set = set()
    for data in data_list:
        data_set.add(data.text.strip())
    return data_set

def get_data(html):
    doc = pq(html)
    name = doc('h1.name').text()
    types_a = doc('li.ellipsis > a')
    types = [type.text.strip() for type in types_a]
    actors_a = doc('li.celebrity.actor > div > a')
    actors = rinse_data(actors_a)
    return {'name':name, "types":types, 'actors':actors}

if __name__ == '__main__':
    url = 'https://maoyan.com/films?showType=3&offset=0'
    index_html = get_html(url)
    detail_url_list = get_detail_url(index_html)
    for detail_url in detail_url_list:
        detail_html = get_html(detail_url)
        print(get_data(detail_html))
