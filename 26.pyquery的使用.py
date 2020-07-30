import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq

url = 'https://www.qidian.com/rank/yuepiao'

headers = {
    'User-Agent':UserAgent().random
}

response = requests.get(url, headers=headers)

doc = pq(response.text)
names = [a.text for a in doc('h4 a')]
authors_a = doc('.author a')
author_list = []
for num in range(len(authors_a)):
    if num%2 == 0:
        author_list.append(authors_a[num].text)

for name, author in zip(names, author_list):
    print(name, author)