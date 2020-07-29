# from urllib.request import Request,urlopen
# from urllib.parse import urlencode
#
# arg = {
#     'wd':'python爬虫',
#     's':'123456'
# }
#
# url = 'https://www.baidu.com/s?wd={}'.format(urlencode(arg))
#
# headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# req = Request(url, headers=headers)
# response = urlopen(req)
#
# print(response.read().decode())



# from urllib.request import Request, urlopen
# from urllib.parse import urlencode
#
# arg = {
#     'wd':'王者荣耀',
#     'ie':'utf-8'
# }
#
# url = 'https://www.baidu.com/s?{}'.format(urlencode(arg))
#
# headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# request = Request(url, headers=headers)
# response = urlopen(request)
# print(response.read().decode())







































# from urllib.request import Request, urlopen
# from urllib.parse import urlencode
#
# arg = {
#     'wd':'python数据清洗',
#     'ie':'utf-8'
# }
#
# url = 'https://www.baidu.com/s?{}'.format(urlencode(arg))
#
# headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# request = Request(url, headers=headers)
# response = urlopen(request)
# print(response.read().decode())



























from urllib.request import Request, urlopen
from urllib.parse import urlencode

arg = {
    'wd':'爬虫反爬机制',
    'ie':'utf-8'
}


url = 'https://www.baidu.com/s?{}'.format(urlencode(arg))

headers = {
    'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())