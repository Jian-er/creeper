from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "http://httpbin.org/get"

ua = UserAgent()

headers ={
    'User-Agent':ua.random 
}

request = Request(url, headers=headers)
response = urlopen(request)

print(response.read().decode())