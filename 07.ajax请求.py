# from urllib.request import Request, urlopen
#
# url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=60'
#
# headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# }
#
# request = Request(url, headers=headers)
# response = urlopen(request)
# info = response.read().decode()
# print(info)




# from urllib.request import Request, urlopen
# from time import sleep
#
#
# url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'
#
# headers = {
#     'User-Agent':"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
# }
#
#
# i = 0
# while True:
#     # request = Request(url, headers=headers)
#     request = Request(url.format(i*20), headers=headers)
#     response = urlopen(request)
#     info = response.read().decode()
#     if info == "[]":
#         break
#     else:
#         print(info)
#         i += 1
#     sleep(3)




from urllib.request import Request, urlopen
from time import sleep
from fake_useragent import UserAgent


url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=1'
ua = UserAgent()

i = 0
while True:
    headers = {
        "User-Agent":ua.random
    }
    request = Request(url.format(i), headers=headers)
    response = urlopen(request)
    info = response.read().decode()

    with open('豆瓣电影信息.txt', 'a', encoding='utf-8') as f:
        f.write(info+"\n")

    if info == '[]':
        break
    else:
        i += 1
        print(info)

    sleep(3)




























