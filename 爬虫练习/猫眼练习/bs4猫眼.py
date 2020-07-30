import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from random import choice
from time import sleep

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
        response.encoding = 'uft-8'
        return response.text
    else:
        return False

def get_detail_url(html):
    soup = BeautifulSoup(html, 'lxml')
    detail_url_a = soup.select('.movie-item.film-channel > a')
    detail_url_list = ["https://maoyan.com{}".format(detail_url.get('href')) for detail_url in detail_url_a]
    return detail_url_list

def rinse_data(data_list):
    data_set = set()
    for data in data_list:
        data_set.add(data.text.strip())
    return data_set

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.find("h1", class_='name').text
    types_a = soup.find_all("a", class_='text-link')
    types = [type.text for type in types_a]
    actors_a = soup.select('li.celebrity.actor > div > a')
    actors = rinse_data(actors_a)
    return {"name":name, "types":types, 'actors':actors}

if __name__ == '__main__':
    url = 'https://maoyan.com/films?showType=3&offset=0'
    index_html = get_html(url)
    detail_url_list = get_detail_url(index_html)
    for detail_url in detail_url_list:
        detail_html = get_html(detail_url)
        print(get_data(detail_html))