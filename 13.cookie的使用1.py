# from urllib.request import Request, build_opener, ProxyHandler
# from fake_useragent import UserAgent
#
# url = 'https://www.kxdao.net/forum.php?mod=forumdisplay&fid=55'
#
# headers = {
#     'User-Agent':UserAgent().random,
#     'Cookie':'G1NZ_2132_saltkey=k9V77i9E; G1NZ_2132_lastvisit=1594960092; Hm_lvt_2b441fdd1b590975e0e2d2a00d32226c=1594978892; G1NZ_2132_sid=z2QQNp; PHPSESSID=4jkc48pq0faulomiv2ivsb9a05; G1NZ_2132_atarget=1; G1NZ_2132_popadv=a%3A0%3A%7B%7D; G1NZ_2132_st_p=0%7C1594978912%7C6dee56507423f6b74fbec4b9906bc189; G1NZ_2132_con_request_uri=https%3A%2F%2Fwww.kxdao.net%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dforum.php%253Fmod%253Dforumdisplay%2526fid%253D46%2526page%253D1; G1NZ_2132_client_created=1594979291; G1NZ_2132_client_token=DB569F65958A1CFBCBDEFE8C5806373C; G1NZ_2132_ulastactivity=12ccQs2xgsHetd8iyzh3vPtj4hxGOYQUA%2F0K5iwYG7fZ7WMpXEfM; G1NZ_2132_auth=9ae4yhyzOF7Ua%2FLI59CXlkrWJWKKf6tCBw%2FKysoGsZ9PVELttpsJF3K1InoYR2U7uCRldyB49Tqghmvtq%2F4vR9EehA; G1NZ_2132_connect_login=1; G1NZ_2132_connect_is_bind=1; G1NZ_2132_connect_uin=DB569F65958A1CFBCBDEFE8C5806373C; G1NZ_2132_stats_qc_login=3; G1NZ_2132_myrepeat_rr=R0; G1NZ_2132_nofavfid=1; G1NZ_2132_dsu_amuppered=40001; G1NZ_2132_dsu_amupper=DQo8c3R5bGU%2BDQoucHBlcndibSB7cGFkZGluZzo2cHggMTJweDtib3JkZXI6MXB4IHNvbGlkICNDRENEQ0Q7YmFja2dyb3VuZDojRjJGMkYyO2xpbmUtaGVpZ2h0OjEuOGVtO2NvbG9yOiMwMDMzMDA7d2lkdGg6MjAwcHg7b3ZlcmZsb3c6aGlkZGVufQ0KLnBwZXJ3Ym0gLnRpbWVze2NvbG9yOiNmZjk5MDA7fQ0KLnBwZXJ3Ym0gIGF7ZmxvYXQ6cmlnaHQ7Y29sb3I6I2ZmMzMwMDt0ZXh0LWRlY29yYXRpb246bm9uZX0NCjwvc3R5bGU%2BDQoNCjxkaXYgY2xhc3M9InBwZXJ3Ym0iIGlkPSJwcGVyd2JfbWVudSIgc3R5bGU9ImRpc3BsYXk6IG5vbmUiID4NCjxBIEhSRUY9InBsdWdpbi5waHA%2FaWQ9ZHN1X2FtdXBwZXI6cHBlcmxpc3QiIHRhcmdldD0iX2JsYW5rIj7mn6XnnIvnrb7liLDmjpLooYw8L0E%2BDQo8c3Ryb25nPue0r%2BiuoeetvuWIsDxzcGFuIGNsYXNzPSJ0aW1lcyI%2BMzY0PC9zcGFuPuasoTwvc3Ryb25nPjxicj4NCg0KPHN0cm9uZz7ov57nu63nrb7liLA8c3BhbiBjbGFzcz0idGltZXMiPjA8L3NwYW4%2B5qyhPC9zdHJvbmc%2BPGJyPg0KDQo8c3Ryb25nPuS4iuasoeetvuWIsDogPHNwYW4gY2xhc3M9InRpbWVzIj4yMDIwLTA3LTE3IDE3OjQ4OjE5PC9zcGFuPjwvc3Ryb25nPg0KPC9kaXY%2BDQo%3D; G1NZ_2132_visitedfid=55D46D47; G1NZ_2132_smile=5D1; G1NZ_2132_st_t=40001%7C1594979858%7C9b1ab96fff424cdcc0d5e859cc070d72; G1NZ_2132_forum_lastvisit=D_47_1594978896D_46_1594978904D_55_1594979858; G1NZ_2132_lastact=1594979860%09home.php%09spacecp; G1NZ_2132_lastcheckfeed=40001%7C1594979860; Hm_lpvt_2b441fdd1b590975e0e2d2a00d32226c=1594979860'
# }
#
# request = Request(url, headers=headers)
# handler = ProxyHandler({'http':'113.194.29.233:9999'})
# opener = build_opener(handler)
# response = opener.open(request)
# print(response.read().decode())


from urllib.request import Request, build_opener, ProxyHandler
from fake_useragent import UserAgent

url = 'https://www.kxdao.net/forum.php?mod=forumdisplay&fid=119'

headers = {
    'User-Agent':UserAgent().random,
    'Cookie':'G1NZ_2132_saltkey=k9V77i9E; G1NZ_2132_lastvisit=1594960092; G1NZ_2132_atarget=1; G1NZ_2132_client_created=1594979291; G1NZ_2132_client_token=DB569F65958A1CFBCBDEFE8C5806373C; G1NZ_2132_auth=9ae4yhyzOF7Ua%2FLI59CXlkrWJWKKf6tCBw%2FKysoGsZ9PVELttpsJF3K1InoYR2U7uCRldyB49Tqghmvtq%2F4vR9EehA; G1NZ_2132_connect_login=1; G1NZ_2132_connect_is_bind=1; G1NZ_2132_connect_uin=DB569F65958A1CFBCBDEFE8C5806373C; G1NZ_2132_stats_qc_login=3; G1NZ_2132_myrepeat_rr=R0; G1NZ_2132_nofavfid=1; G1NZ_2132_smile=5D1; G1NZ_2132_sid=yYYJly; G1NZ_2132_lip=119.164.125.140%2C1594979291; G1NZ_2132_popadv=a%3A0%3A%7B%7D; G1NZ_2132_ulastactivity=8814vrAwXblPQ9dasW80eqeAzs6SXQZ4Hw5cA76%2BAt7ikmOwsuC6; G1NZ_2132_sendmail=1; PHPSESSID=cl127sn0td4smbb13t6hcrne74; Hm_lvt_2b441fdd1b590975e0e2d2a00d32226c=1594978892,1595057053; G1NZ_2132_dsu_amuppered=40001; G1NZ_2132_dsu_amupper=DQo8c3R5bGU%2BDQoucHBlcndibSB7cGFkZGluZzo2cHggMTJweDtib3JkZXI6MXB4IHNvbGlkICNDRENEQ0Q7YmFja2dyb3VuZDojRjJGMkYyO2xpbmUtaGVpZ2h0OjEuOGVtO2NvbG9yOiMwMDMzMDA7d2lkdGg6MjAwcHg7b3ZlcmZsb3c6aGlkZGVufQ0KLnBwZXJ3Ym0gLnRpbWVze2NvbG9yOiNmZjk5MDA7fQ0KLnBwZXJ3Ym0gIGF7ZmxvYXQ6cmlnaHQ7Y29sb3I6I2ZmMzMwMDt0ZXh0LWRlY29yYXRpb246bm9uZX0NCjwvc3R5bGU%2BDQoNCjxkaXYgY2xhc3M9InBwZXJ3Ym0iIGlkPSJwcGVyd2JfbWVudSIgc3R5bGU9ImRpc3BsYXk6IG5vbmUiID4NCjxBIEhSRUY9InBsdWdpbi5waHA%2FaWQ9ZHN1X2FtdXBwZXI6cHBlcmxpc3QiIHRhcmdldD0iX2JsYW5rIj7mn6XnnIvnrb7liLDmjpLooYw8L0E%2BDQo8c3Ryb25nPue0r%2BiuoeetvuWIsDxzcGFuIGNsYXNzPSJ0aW1lcyI%2BMzY1PC9zcGFuPuasoTwvc3Ryb25nPjxicj4NCg0KPHN0cm9uZz7ov57nu63nrb7liLA8c3BhbiBjbGFzcz0idGltZXMiPjE8L3NwYW4%2B5qyhPC9zdHJvbmc%2BPGJyPg0KDQo8c3Ryb25nPuS4iuasoeetvuWIsDogPHNwYW4gY2xhc3M9InRpbWVzIj4yMDIwLTA3LTE4IDE1OjI0OjEzPC9zcGFuPjwvc3Ryb25nPg0KPC9kaXY%2BDQo%3D; G1NZ_2132_visitedfid=119D55D46D47; G1NZ_2132_st_t=40001%7C1595057262%7C3a9b077c73260e86bb48dfad3a200b35; G1NZ_2132_forum_lastvisit=D_47_1594978896D_46_1594978904D_55_1594980257D_119_1595057262; Hm_lpvt_2b441fdd1b590975e0e2d2a00d32226c=1595057264; G1NZ_2132_lastact=1595057263%09home.php%09spacecp; G1NZ_2132_checkpm=1; G1NZ_2132_lastcheckfeed=40001%7C1595057263; G1NZ_2132_checkfollow=1'
}

request = Request(url, headers=headers)
handler = ProxyHandler({'http':'120.198.76.45:41443'})
opener = build_opener(handler)
response = opener.open(request)

print(response.read().decode())























