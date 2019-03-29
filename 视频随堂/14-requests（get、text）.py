# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 19:47
# 文件     ：14-requests（get、text）.py
# IDE      ：PyCharm
import requests
from fake_useragent import UserAgent
headers = {
    'User-Agent': UserAgent().chrome
}
url = 'https://www.baidu.com/s'
params = {
    'wd': '尚学堂'
}
response = requests.get(url, headers=headers, params=params)
print(response.text)
