from fake_useragent import UserAgent
import requests

url = 'https://www.12306.cn/mormhweb/'
headers = {
    'User-Agent':UserAgent().random
}
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, verify=False)
response.encoding = 'utf-8'
print(response.text)