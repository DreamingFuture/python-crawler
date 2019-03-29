# 作者     ：孔庆杨
# 创建时间 ：2019/1/2215:08
# 文件     ：模拟浏览器尝试.py
# IDE      ：PyCharm
import re
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://tieba.baidu.com/p/2125145202#!/l/p1')
for i in range(0, 5):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
print(browser.page_source)  # browser.page_source是获取网页的全部html

#htmls = re.findall('http[\s\S].png', browser.page_source)
#print(htmls)
browser.close()
