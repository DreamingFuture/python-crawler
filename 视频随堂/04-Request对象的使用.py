# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 9:29
# 文件     ：04-Request对象的使用.py
# IDE      ：PyCharm
from urllib.request import Request
from urllib.request import urlopen

from fake_useragent import UserAgent # 随机headers

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
request = Request(url, headers=headers)
print(request.get_header('User-agent'))
response = urlopen(request).read().decode()

print(response)


