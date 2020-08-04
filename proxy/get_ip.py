from fake_useragent import UserAgent
from lxml import etree
from random import choice
import requests

def get_ips():
    url = 'https://www.kuaidaili.com/free/'
    response = requests.get(url, headers={'User-Agent':UserAgent().random})
    e = etree.HTML(response.text)
    ips = e.xpath('//tbody/tr/td[1]/text()')
    ports = e.xpath("//tbody/tr/td[2]/text()")
    # ips = [ip.strip() for ip in e.xpath('//tbody/tr/td[1]/text()')]
    # ports = [ip.strip() for ip in e.xpath("//tbody/tr/td[2]/text()")]
    return ips, ports

def is_can(ip_port):
    try:
        requests.get('http://httpbin.org/get', headers={"User-Agent":UserAgent().random}, proxies={'http':ip_port}, timeout=1)
        return True
    except:
        return False



def get_requests_proxy():
    ips, ports = get_ips()
    for ip, port in zip(ips, ports):
        flog = is_can("{}:{}".format(ip, port))
        if flog:
            with open("requests_proxy.txt", 'w', encoding='utf-8') as f:
                f.write(("{" + ip + ":" + port + "},\n"))

def get_selenium_proxy():
    ips, ports = get_ips()
    for ip, port in zip(ips, ports):
        flog = is_can("{}:{}".format(ip, port))
        if flog:
            with open("requests_proxy.txt", 'w', encoding='utf-8') as f:
                f.write("{}:{},\n".format(ip, port))

if __name__ == '__main__':
    get_requests_proxy()
    get_selenium_proxy()






