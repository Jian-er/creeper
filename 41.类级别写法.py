from fake_useragent import UserAgent
import requests

# 发送请求
class Downloader():
    def do_download(self, url):
        headers = {"User-Agent":UserAgent().random}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text

# 数据解析
class Parser():
    def do_parse(self, html):
        pass

# 数据保存
class DataOutPut():
    def do_save(self, data):
        pass

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
        self.url_manger = URLManager()

    def start(self, url):
        self.url_manger.add_new_url(url)
        url = self.url_manger.get_new_url()
        html = self.downloader.do_download(url)
        datas, urls = self.parser.do_parse(html)
        self.data_out_put.do_save(datas)
        self.url_manger.add_new_urls(urls)


if __name__ == '__main__':
    scheduler = Scheduler()
    url = ''
    scheduler.start(url)