from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url = 'http://httpbin.org/get'

headers = {
    'User-Agent':UserAgent().random
}


request = Request(url, headers=headers)
handler = ProxyHandler({"http":'124.200.36.118:40188'})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
