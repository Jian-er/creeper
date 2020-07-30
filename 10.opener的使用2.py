from urllib.request import Request, build_opener
from urllib.request import HTTPHandler
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'

headers = {
    'User-Agent':UserAgent().random
}

request = Request(url, headers=headers)
handler = HTTPHandler(debuglevel=1)
opener = build_opener(handler)
response = opener.open(request)
# print(response.read().decode())

