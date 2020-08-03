import requests
from fake_useragent import UserAgent
from urllib.parse import urlencode

url = 'https://www.xiami.com/'

headers = {
    'User-Agent':UserAgent().random,
    'cookie':'xmgid=b4f8925f-ec0d-44a4-be4c-996e150e563d; _uab_collina=159497886934909402411476; cna=mA2XF1liSUwCAXekfYyNl3Vq; xm_token=0611c3b2bb9d92030c01fe4ce9e74927r88k7d; uidXM=444211483; member_auth=hGuaGt4Z6GsPx9XxSOppLHUfiOemS2P4ufUh0tZ431tBLNRqH4T419WYS30qm3ya1AxAGYSY2T9MHu9ZI9qZESQAye5XsOr3j2fFN%2FZa; xm_sg_tk=d6ce6e1ed0b8234f4822c0d5d3bcaaf7_1595338665026; xm_sg_tk.sig=cPXATGK8Yb2IK1OdR4H13ojjoZchG-lEjcozVXAyPw0; '
}
data={
    'user_name': "15910534399",
    'user_pass': "yj814762757"
}
response = requests.get(url, headers=headers, data=urlencode(data).encode())
with open('虾米登录成功页面.html', 'w+', encoding='utf-8') as f:
    f.write(response.text)


