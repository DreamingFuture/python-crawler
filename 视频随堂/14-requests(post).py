# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 19:54
# 文件     ：14-requests(post).py
# IDE      ：PyCharm
import requests
from fake_useragent import UserAgent
headers = {
    'User-Agent': UserAgent().chrome
}
url = 'https://www.sxt.cn/index/login/login'
params = {
    'user': '15333515094',
    'password': 'qwe123'
}
response = requests.post(url, headers=headers, data=params)
print(response.text)