from fake_useragent import UserAgent
import requests
from jsonpath import jsonpath

url = 'https://www.zhipin.com/wapi/zpCommon/data/city.json'

headers = {'User-Agent':UserAgent().random}

response = requests.get(url, headers=headers)



names = jsonpath(response.json(), '$..name')
codes = jsonpath(response.json(), '$..code')

for name, code in zip(names, codes):
    print(name, ":", code)