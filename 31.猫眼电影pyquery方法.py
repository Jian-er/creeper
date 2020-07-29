import requests
from fake_useragent import UserAgent
from random import choice
from pyquery import PyQuery as pq

def get_html(url):
    headers = {'User-Agent':UserAgent().random}
    proxy = [
        {'http':'183.166.102.23:9999'},
        {'http':'112.111.217.26:9999'},
        {'http':'175.44.108.220:9999'},
        {'http':'114.230.105.156:9999'},
        {'http':'110.243.14.20:9999'},
        {'http':'171.11.29.153:9999'},
        {'http':'106.42.217.123:9999'},
        {'http':'223.242.225.161:9999'},
        {'http':'182.32.250.228:9999'},
             ]
    response = requests.get(url, headers=headers, proxies=choice(proxy))
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return False

def get_detail_url(html):
    doc = pq(html)
    detail_a_list = doc('.movie-item.film-channel > a')
    detail_url_list = []
    for a in detail_a_list:
        detail_url_list.append('https://maoyan.com{}'.format(a.get('href')))
    return detail_url_list


def rinse_data(data_list):
    data_set = set()
    for data in data_list:
        data_set.add(data.text.strip())
    return data_set

def get_data(html):
    doc = pq(html)
    name = doc('h1.name').text()
    type_a_list = doc('li.ellipsis > a')
    types = rinse_data(type_a_list)
    actor_a_list = doc('li.celebrity.actor > div > a')
    actors = rinse_data(actor_a_list)
    return {"name": name, "types": types, "actors": actors}



if __name__ == '__main__':
    pages = int(input("获取页数："))
    for page in range(pages):
        index_url = 'https://maoyan.com/films?showType=3&offset={}'.format(page*30)
        index_html = get_html(index_url)
        detail_url_lsit = get_detail_url(index_html)
        for detail_url in detail_url_lsit:
            detail_html = get_html(detail_url)
            print(get_data(detail_html))