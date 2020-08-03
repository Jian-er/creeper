import requests
from fake_useragent import UserAgent
from chaojiying_Python.chaojiying import get_code

login_url = 'http://www.chaojiying.com/user/login/'

img_url = 'http://www.chaojiying.com/include/code/code.php?u=1'


headers = {'User-Agent':UserAgent().random}

# 创建session对象
session = requests.session()

# 第一次获取登录页面
session.get(login_url, headers=headers)
# 获取验证码
img_response = session.get(img_url, headers=headers)
with open('code.png', 'wb') as f:
    f.write(img_response.content)

# 获取验证码
code = get_code('code.png')

# 拼接完整表单
data = {
    'user': 'Akihi6',
    'pass': 'yj814762757',
    'imgtxt': code,
    'act': '1'
}

login_response = session.post(login_url, data=data, headers=headers)

print(login_response.text)