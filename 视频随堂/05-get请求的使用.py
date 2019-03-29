# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 9:55
# 文件     ：05-get请求的使用.py
# IDE      ：PyCharm
# get请求主要做转码用。
print('''
第一种 quote（）
''')
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
url = 'http://www.baidu.com/s?wd=' + quote('尚学堂')
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())

print('''
第二种 urlencode()
''')
from urllib.request import Request, urlopen
import random
from fake_useragent import UserAgent
args = {
    'wd': '尚学堂',
    'ie': 'utf-8'
}
url = 'http://www.baidu.com/s?' + urlencode(args)
headers = {
    'User-Agents': UserAgent().random
}
request = Request(url, headers=headers)
response = urlopen(request).read().decode()
print(response)