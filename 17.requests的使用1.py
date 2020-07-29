import requests
from fake_useragent import UserAgent

url = 'http://www.baidu.com/s?'
params = {
    'wd':'快代理'
}
response = requests.get(url, params=params, headers={'User-Agent':UserAgent().random})
response.encoding = 'utf-8'
print(response.text)