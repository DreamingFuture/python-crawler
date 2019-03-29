# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 14:14
# 文件     ：12-cookie的使用2.py
# IDE      ：PyCharm
from urllib.parse import urlencode
from urllib.request import Request, HTTPCookieProcessor, build_opener
from fake_useragent import UserAgent

# 登录
url ='http://www.sxt.cn/index/login/login.html'
headers = {
        'User-Agent': UserAgent().chrome,
    }
form_data = {
    'user': '15333515094',
    'password': 'qwe123'
}
f_data = urlencode(form_data).encode()
request = Request(url, headers=headers, data=f_data)
# response = urlopen(reqeuest).read() 错误的
# 下面几行是重点
handler = HTTPCookieProcessor()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())

# 访问界面
info_url = 'http://www.sxt.cn/index/user.html'
request = Request(info_url, headers=headers)
response = opener.open(request)
print(response.read().decode())
