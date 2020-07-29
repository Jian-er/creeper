# from urllib.request import Request, urlopen
# from  urllib.parse import quote
#
# def get_html(url):
#     headers = {
#         'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
#     }
#     request = Request(url, headers=headers)
#     response = urlopen(request)
#     return response.read().decode()
#
# def save_html(html, filename):
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(html)
#
# def main():
#     content = input('请输入要获取哪个贴吧：')
#     num = int(input("请输入要获取多少页："))
#     for i in range(num):
#         url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(quote(content), i*50)
#         # print(url)
#         html = get_html(url)
#         filename = content+'贴吧第'+str(i+1)+'页.html'
#         save_html(html, filename)
#
#
# if __name__ == '__main__':
#     main()

from urllib.request import Request, urlopen
from urllib.parse import urlencode

def get_html(url):
    headers = {
        'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read().decode()


def save_html(html, filename):
    with open("06.贴吧案例下载文件/"+filename, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    name = input("请输入要爬取的贴吧名称：")
    num = int(input("请输入要爬取多少页："))
    for i in range(num):
        args = {
            'kw':name,
            'ie':'utf-8',
            'pn':i*50
        }
        url = "https://tieba.baidu.com/f?{}".format(urlencode(args))
        html = get_html(url)
        filename = name+'贴吧第'+str(i+1)+'页.html'
        save_html(html, filename)

if __name__ == '__main__':
    main()



































