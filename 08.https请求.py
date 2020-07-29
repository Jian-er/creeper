# from urllib.request import Request, urlopen
# # import ssl
# #
# # url = 'https://www.12306.cn/index/'
# #
# # headers = {
# #     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# # }
# #
# # context = ssl._create_unverified_context()
# # request = Request(url, headers=headers)
# # response = urlopen(request, context=context)
# # print(response.read().decode())






from urllib.request import Request, urlopen
import ssl

url = 'https://www.12306.cn/index/'

request = Request(url)

context = ssl._create_unverified_context()
response = urlopen(request, context=context)

print(response.read().decode())

















