from selenium import webdriver

def headless():
    options = webdriver.ChromeOptions()
    # 开启无头浏览器模式
    options.add_argument('--headless')
    # 将参数设置到浏览器
    chrome = webdriver.Chrome(chrome_options=options)
    chrome.get('https://cn.bing.com/')
    print(chrome.page_source)
    chrome.close()

def proxy():
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=http://123.54.52.37:9999')
    chrom = webdriver.Chrome(chrome_options=options)
    chrom.get('http://httpbin.org/get')
    print(chrom.page_source)
    chrom.close()


if __name__ == '__main__':
    proxy()