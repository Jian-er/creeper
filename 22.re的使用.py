import re

str = "I study python3.7 every_day"
print('-------------match()------------')  # 从头开始匹配
m1 = re.match(r'I', str)
m2 = re.match(r'\w', str)
m3 = re.match(r'.', str)
m4 = re.match(r'\S', str)
# m5 = re.match(r'study', str)
print(m4.group())
print('-------------search()------------') # 从任意位置开始匹配，匹配第一个
s1 = re.search(r'study', str)
s2 = re.search(r's\w+', str)
s3 = re.search(r'I (\w+)', str)
s4 = re.search(r'y', str)
print(s4.group())
print('-------------findall()------------')
f1 = re.findall(r'y', str)
f2 = re.findall(r'python3.7', str)
f3 = re.findall(r'p.+\d', str)
print(f3)
print('-------------sub()------------')
su1 = re.sub(r'every day', r'EveryDay', str)
su2 = re.sub(r'e\w+', r'EveryDay', str)
print(su2)
print('-------------text()------------')
str1 = '<div><a class="title" herf="http://www.bjsxt.com">尚学堂bjsxt</a></div>'
t1 = re.findall(r'尚学堂', str1)
t2 = re.findall(r'[\u4e00-\u9fa5]+', str1)
t3 = re.findall(r'[\u4e00-\u9fa5]+\w+', str1)
t4 = re.findall(r'<a class="title" herf="http://www.bjsxt.com">(.+)</a>', str1)
print(t4)