from fake_useragent import UserAgent
import requests

url = 'http://127.0.0.1:8000/login/'

args = {
    'name':'admin',
    'password':'123456'
}

response = requests.post(url, headers={'User-Agent':UserAgent().random}, data=args)
print(response.text)