from threading import Thread
import requests
from lxml import etree
from fake_useragent import UserAgent
from queue import Queue

class Spider(Thread):
    def __init__(self, url_q):
        Thread.__init__(self)
        self.url_q = url_q

    def run(self):
        while not self.url_q.empty():
            url = self.url_q.get()
            headers = {'User-Agent':UserAgent().random}
            response = requests.get(url, headers=headers)
            e = etree.HTML(response.text)
            contents =[div.xpath("string(.)").strip() for div in e.xpath("//div[@class='content']")]
            with open('duanzi.txt', 'a', encoding='utf-8')as f:
                for content in contents:
                    f.write(content + "\n")

if __name__ == '__main__':
    base_url = 'https://www.qiushibaike.com/text/page/{}/'
    url_q = Queue()
    for i in range(1,5):
        url_q.put(base_url.format(i))

    for num in range(3):
        spider = Spider(url_q)
        spider.start()
