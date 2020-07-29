# from urllib.request import Request, urlopen

# url = 'https://www.baidu.com/s?wd=python'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# request = Request(url, headers=headers)
#
# resp = urlopen(request)
#
# print(resp.read().decode())

# from urllib.request import Request,urlopen
#
# url = 'https://www.kxdao.net/'
#
# headers = {
#     'User-Agent':"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
# }
#
# request = Request(url, headers=headers)
#
# response = urlopen(request)
#
# print(response.read().decode())


# from urllib.request import Request,urlopen
# from urllib.parse import quote
#
# url = 'https://www.baidu.com/s?wd={}'.format(quote('python爬虫'))
#
# headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# req = Request(url, headers=headers)
# response = urlopen(req)
#
# print(response.read().decode())

#
# from urllib.request import Request,urlopen
# from urllib.parse import quote
#
# url = 'https://www.baidu.com/s?wd={}'.format(quote('python爬虫'))
#
# headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# request = Request(url, headers=headers)
# response = urlopen(request)
#
# print(response.read().decode())




































# from urllib.request import Request, urlopen
# from urllib.parse import quote
#
# url = 'https://www.baidu.com/s?wd={}'.format(quote('百战程序员'))
#
# headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# request = Request(url, headers=headers)
# response = urlopen(request)
# print(response.read().decode())


































from urllib.request import Request, urlopen
from urllib.parse import quote


url = 'https://www.baidu.com/s?wd={}'.format(quote('英雄联盟'))

headers = {
    'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())
