from fake_useragent import UserAgent
import requests

url = 'http://127.0.0.1:8000/login/'

args = {
    'name':'admin',
    'password':'123456'
}
headers = {
    'User-Agent':UserAgent().random
}

session = requests.Session()
response = session.post(url, headers=headers, data=args)
# print(response.text)


info_url = 'http://127.0.0.1:8000/userinfo/'
response2 = session.get(info_url, headers=headers)
print(response2.text)