from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

url = 'https://www.kxdao.net/forum-42-1asda.html'

headers = {'User-Agent': UserAgent().random}
request = Request(url, headers=headers)

try:
    response = urlopen(request)
except URLError as e:
    if e.args is ():
        print(e.code)
    else:
        print(e.args[0])
print("完成")