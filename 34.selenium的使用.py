from selenium import webdriver

# 构造浏览器
chrome = webdriver.Chrome()

# 发送请求，访问rul
url = 'https://www.baidu.com/'

chrome.get(url)

# 截图
chrome.save_screenshot("baidu.png")

# 获取源代码
html = chrome.page_source
print(html)

# chrome.close()
chrome.quit()