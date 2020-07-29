# from urllib.request import urlopen
# from urllib.request import Request
# from random import choice
#
# url = 'https://www.baidu.com/'
# 定义User_Agent变量
# User-Agent 列表
# user_agetns = [
#     'ua1',
#     'ua2',
#     'ua3'
# ]
#
# headers = {
#     'User-Agent': choice(user_agetns)
# }
# 封装request对象
# req = Request(url, headers=headers)
# print(req.get_header('User-agent'))
# 发送请求
# resp = urlopen(req)
#
# print(resp.read().decode())


# from urllib.request import urlopen, Request
# from random import choice
#
# url = 'https://www.kxdao.net/'
#
# # 定义user-agent
#
# user_agents = [
#     'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
# ]
#
# headers = {
#     'User-Agent':choice(user_agents)
# }
#
#
# req = Request(url, headers=headers)
# print(req.get_header('User-agent'))
# response = urlopen(req)
# # print(response.read().decode())


# from urllib.request import urlopen, Request
# from random import choice
#
# url = 'https://www.jianshu.com/p/da6a44d0791e'
#
# user_agents = [
#     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
# ]
#
# headers = {
#     'User-Agent':choice(user_agents)
# }
#
# req = Request(url, headers=headers)
#
# response = urlopen(req)
#
# print(response.read().decode())




























# from urllib.request import Request, urlopen
# from random import choice
#
# url = 'https://www.cnblogs.com/kevingrace/p/10482469.html'
#
# user_agents = [
#     'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
# ]
#
# headers = {
#     'User-Agent':choice(user_agents)
# }
#
# req = Request(url, headers=headers)
# print(req.get_header('User-agent'))
# response = urlopen(req)
# print(response.read().decode())
























from urllib.request import Request, urlopen
from random import choice

url = 'https://www.cnblogs.com/roooookie/p/8473640.html'

user_agents = [
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
]

headers = {
    'User-Agent':choice(user_agents)
}

req = Request(url, headers=headers)
print(req.get_header('User-agent'))
response = urlopen(req)
print(response.read().decode())


