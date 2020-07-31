from selenium import webdriver
from time import sleep
# 构造浏览器

chrom = webdriver.Chrome()

url = 'https://cn.bing.com/'
chrom.get(url)

# 输入要搜索的内容
chrom.find_element_by_id('sb_form_q').send_keys('python')
# 点击搜索
chrom.find_element_by_id('sb_form_go').click()
sleep(3)
# 获取源代码
html = chrom.page_source
print(html)

chrom.close()
