from selenium import webdriver
from lxml import etree
from time import sleep

chrom = webdriver.Chrome()
chrom.get('https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&wq=bi&pvid=219187a2df094724aa9ebdeef830de9f')
js = 'document.documentElement.scrollTop=100000'
# js = 'window.scrollTo(0,10000)'
chrom.execute_script(js)
sleep(3)

html = chrom.page_source
e = etree.HTML(html)

titles = e.xpath("//div[@class='gl-i-wrap']/div[@class='p-name p-name-type-2']//em/text()[1]")
nums = e.xpath("//div[@class='gl-i-wrap']/div[@class='p-price']/strong/i/text()")

for title, num in zip(titles, nums):
    print(title, num)

print(len(nums))