# 作者     ：孔庆杨
# 创建时间 ：2019/1/24 20:25
# 文件     ：糗事百科.py
# IDE      ：PyCharm
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url_root = 'https://www.qiushibaike.com/text/page/{}'
headers = {
    'User-Agent': UserAgent().random
}
content = []
html = ''
answer = []
n = 1
for num in range(int(input('请输入你想读取的页数:'))):
    url = url_root.format(int(num + 1))
    response = requests.get(url, headers=headers)
    html = html + response.text
    soup = BeautifulSoup(response.text, 'lxml')
    content.extend(soup.select('a[class="contentHerf"]'))
    for element in content:
        element = element.text
        element = re.sub('\n', '', element)
        answer = (str(n) + '--' + element + '\n')
        with open('糗事百科.doc', 'a', encoding='utf-8') as f:
            f.write(answer)
        n = n + 1
