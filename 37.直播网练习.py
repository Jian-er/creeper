from selenium import webdriver
from time import sleep

chrom = webdriver.Chrome()

chrom.get('https://www.huya.com/g/lol')

while True:
    titles = chrom.find_elements_by_class_name('title')
    names = chrom.find_elements_by_class_name('nick')
    counts = chrom.find_elements_by_class_name('js-num')

    for title, name, count in zip(titles, names, counts):
        print(title.text, ":", name.text, ":", count.text)


    if chrom.page_source.find('laypage_next') != -1:
        chrom.find_element_by_class_name('laypage_next').click()
        sleep(3)
    else:
        break

chrom.close()