from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler
from proxy.get_ip import get_requests_ip
from random import choice
import requests

url = 'http://httpbin.org/get'

headers = {
    'User-Agent':UserAgent().random
}


request = Request(url, headers=headers)
handler = ProxyHandler({"http":'115.221.247.70:9999'})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())

# proxy = get_requests_ip()
# response = requests.get(url, headers=headers, proxies=choice(proxy))
# print(response.text)





