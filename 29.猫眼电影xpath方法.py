from fake_useragent import UserAgent
import requests
from lxml import etree
from random import choice
from time import sleep

def get_html(url):
    """

    :param url: 要爬取的地址
    :return: 返回html
    """
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
    sleep(3)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return None

def parse_list(html):
    """

    :param html:传递进来一个有电影列表的html
    :return: 返回一个电影列表url
    """
    if html:
        e = etree.HTML(html)
        list_url = ["https://maoyan.com{}".format(url) for url in e.xpath('//div[@class="movie-item film-channel"]/a/@href')]
        return list_url

def parse_index(html):
    """

    :param html: 传递进来一个有电影列表的html
    :return: 已经提取好的电影信息
    """
    e = etree.HTML(html)
    name = e.xpath('//h1/text()')
    type = e.xpath('//li[@class="ellipsis"]/a/text()')
    actors = e.xpath('//div[@class="celebrity-group"][2]/ul[@class="celebrity-list clearfix"]/li/div/a/text()')
    actors = format_data(actors)
    return {'name':name, "type":type, "actors":actors}

def format_data(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())
    return actor_set

def main():
    num = int(input('请输入要获取多少页：'))
    for page in range(num):
        url = 'https://maoyan.com/films?showType=3&offset={}'.format(page*30)
        list_html = get_html(url)
        list_url = parse_list(list_html)
        for url in list_url:
            info_html = get_html(url)
            movie = parse_index(info_html)
            print(movie)

main()