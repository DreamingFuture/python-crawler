# 作者     ：孔庆杨
# 创建时间 ：2019/1/29 14:42
# 文件     ：18.xpath的使用.py
# IDE      ：PyCharm

'''教程网址： w3shcool'''
import requests
from lxml import etree
from fake_useragent import UserAgent
url = 'https://www.qidian.com/rank/yuepiao?chn=21'
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
names = e.xpath('//h4/a/text()')
author = e.xpath('//p/a[@class="name"]/text()')
grope = e.xpath('//p/a[@data-eid="qd_C42"]/text()')
done = e.xpath('//p[@class="author"]/span/text()')
for index in range(len(names)):
    print(names[index], author[index])
