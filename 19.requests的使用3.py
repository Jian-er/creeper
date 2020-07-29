from fake_useragent import UserAgent
import requests

url = 'http://httpbin.org/get'

proxy = {
    'http':'129.28.183.30:8118'
}

response = requests.get(url, headers={'User-Agent':UserAgent().random}, proxies=proxy)
print(response.text)