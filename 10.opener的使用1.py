from urllib.request import Request
from urllib.request import build_opener
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'

headers = {
    'User-Agent':UserAgent().random
}

request = Request(url, headers=headers)

opener = build_opener()
response = opener.open(request)
print(response.read().decode())