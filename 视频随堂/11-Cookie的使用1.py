# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 15:05
# 文件     ：11-Cookie的使用1.py
# IDE      ：PyCharm
from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = 'http://www.sxt.cn/index/user.html'
headers = {
    'User-Agernt': UserAgent().chrome,
    'Cookie': 'PHPSESSID=grami4c53o428cc4e99i81s6u3; UM_distinctid=168798177dd4a2-0e472b4fc93c52-b781636-144000-168798177de70d; CNZZDATA1261969808=509727308-1548225185-http%253A%252F%252Fwww.sxt.cn%252F%7C1548225185; 53gid2=11255033926012; visitor_type=new; 53gid0=11255033926012; 53gid1=11255033926012; 53revisit=1548226754893; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_keyword=http%3A%2F%2Fwww.sxt.cn%2Findex%2Flogin%2Flogin.html; 53kf_72085067_land_page=http%253A%252F%252Fwww.sxt.cn%252F; kf_72085067_land_page_ok=1'
}
request = Request(url, headers=headers)
response = urlopen(request).read().decode()
print(response)
