from fake_useragent import UserAgent
from random import choice
from lxml import etree
import requests
from time import sleep

# 发送请求
class Downloader():
    def do_download(self, url):
        headers = {'User-Agent': UserAgent().random}
        proxy = [
            {"http":"183.166.71.170:9999"},
            {"http":"163.204.244.130:9999"},
            {"http":"58.253.159.17:9999"},
            {"http":"121.233.226.173:9999"},
        ]
        response = requests.get(url, headers=headers)
        sleep(2)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return False

# 数据解析
class Parser():
    def do_parser_urls(self, index_html):
        e = etree.HTML(index_html)
        urls = ['http://www.xbiquge.la{}'.format(url) for url in e.xpath("//dl/dd[position()>1 and position()<102]/a/@href")]
        return urls

    def do_parser_datas(self, detail_html):
        e = etree.HTML(detail_html)
        title = e.xpath("//div[@class='bookname']/h1/text()")
        content = [ div.xpath("string(.)").strip() for div in e.xpath("//div[@id='content']")]
        return {'title':title, "content":content}



# 数据保存
class DataOutPut():
    def do_save(self, datas):
        with open("{}.txt".format(datas.get("title")[0]), 'w', encoding='utf-8') as f:
            f.write(datas.get('content')[0])

# URL管理器
class URLManager():
    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    # 加入一个url
    def add_new_url(self, url):
        if url not in self.old_url and url is not None and url != '':
            self.new_url.add(url)

    # 加入多个url
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # 获取一个url
    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.add(url)
        return url

    # 获取还有多少个url要爬取
    def get_new_url_size(self):
        return len(self.new_url)

    # 获取是否还有url要爬取
    def is_have_new_url(self):
        return self.get_new_url_size() > 0

# 调度器
class Scheduler:
    def __init__(self):
        self.downloader = Downloader()
        self.parser = Parser()
        self.data_out_put = DataOutPut()
        self.url_manager = URLManager()

    def start(self, url):
        index_html = self.downloader.do_download(url)
        urls = self.parser.do_parser_urls(index_html)
        self.url_manager.add_new_urls(urls)
        try:
            while self.url_manager.is_have_new_url():
                url = self.url_manager.get_new_url()
                detail_html = self.downloader.do_download(url)
                datas = self.parser.do_parser_datas(detail_html)
                self.data_out_put.do_save(datas)
        except:
            print(url)
            print(detail_html)
            print(datas)


if __name__ == '__main__':
    scheduler = Scheduler()
    url = 'http://www.xbiquge.la/10/10489/'
    scheduler.start(url)