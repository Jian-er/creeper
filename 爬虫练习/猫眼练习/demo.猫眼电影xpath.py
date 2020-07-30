import requests
from fake_useragent import UserAgent
from lxml import etree
from random import choice
from time import sleep


def get_html(url):
    headers = {'User-Agent':UserAgent().random}
    proxy = [
        {'http':'123.169.96.4:9999'},
        {'http':'183.166.111.237:9999'},
        {'http':'163.204.245.20:9999'},
        {'http':'110.243.24.175:9999'},
    ]
    response = requests.get(url, headers=headers, proxies=choice(proxy))
    sleep(3)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return False

def get_detail_url(html):
    e = etree.HTML(html)
    detail_url_list = ['https://maoyan.com{}'.format(href) for href in e.xpath('//div[@class="movie-item film-channel"]/a/@href')]
    return detail_url_list

def rinse_data(data_list):
    data_set = set()
    for data in data_list:
        data_set.add(data.strip())
    return data_set

def get_data(html):
    e = etree.HTML(html)
    name = e.xpath('//h1/text()')
    types = e.xpath("//li[@class='ellipsis']/a/text()")
    types = rinse_data(types)
    actors = e.xpath("//li[@class='celebrity actor']/div/a/text()")
    actors = rinse_data(actors)
    return {'name':name, "types":types, "actors":actors}

if __name__ == '__main__':
    url = 'https://maoyan.com/films?showType=3&offset=0'
    index_html = get_html(url)
    detail_url_list = get_detail_url(index_html)
    for detail_url in detail_url_list:
        print(detail_url)
        detail_html = get_html(detail_url)
        print(get_data(detail_html))
