import requests
from fake_useragent import UserAgent
from random import choice
from bs4 import BeautifulSoup


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
    soup = BeautifulSoup(html, 'lxml')
    a_list = soup.select(".movie-item.film-channel > a")
    href_list = []
    for a in a_list:
        href_list.append("https://maoyan.com{}".format(a.get('href')))
    if href_list != "[]":
        return href_list
    else:
        return False

def rinse_data(data_list):
    data_set = set()
    for data in data_list:
        data_set.add(data.text.strip())
    return data_set

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.find('h1', class_='name').text
    type_a_list = soup.select("li.ellipsis > a")
    types = rinse_data(type_a_list)
    actor_a_list = soup.select('li.celebrity.actor > div > a')
    actors = rinse_data(actor_a_list)
    return {'name':name, "type":types, "actors":actors}

if __name__ == '__main__':
    pages = int(input("请输入要获取多少页："))
    for page in range(pages):
        url = 'https://maoyan.com/films?showType=3&offset={}'.format(page*30)
        html = get_html(url)
        href_list = get_detail_url(html)
        for href in href_list:
            detail_html = get_html(href)
            print(get_data(detail_html))