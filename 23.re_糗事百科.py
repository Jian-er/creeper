import requests
from fake_useragent import UserAgent
import re

url = 'https://www.qiushibaike.com/text/'
headers = {'User-Agent':UserAgent().random}

response = requests.get(url, headers=headers)

contents = re.findall(r'<div class="content">\s*<span>\s*(.+)', response.text)


with open('段子.txt', 'a', encoding='utf-8') as f:
    for info in contents:
        new_info = re.sub('<br.*>', '', info)
        f.write(new_info+"\n\n")