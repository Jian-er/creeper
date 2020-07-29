import requests
from fake_useragent import UserAgent
from random import choice
from re import findall

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
    detail_a_list = findall(r'<div.+class="movie-item film-channel">\s+<a href="(/films/\d+)"', html)
    detail_url_list = ["https://maoyan.com{}".format(url) for url in detail_a_list]
    return detail_url_list


def rinse_data(data_list):
    data_set = set()
    for data in data_list:
        data_set.add(data.strip())
    return data_set

def get_data(html):
    name = findall(r'<h1 class="name">(.+)</h1>', html)
    types = findall(r'<a class="text-link".+>(.+)</a>', html)
    actor_a_list = findall(r'<a.+class="name">\s+(.+)\s+</a>', html)
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