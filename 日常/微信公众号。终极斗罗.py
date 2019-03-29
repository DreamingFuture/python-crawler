# 作者     ：孔庆杨
# 创建时间 ：2019/1/27 15:37
# 文件     ：微信公众号。终极斗罗.py
# IDE      ：PyCharm
import requests
from bs4 import BeautifulSoup

url = 'https://mp.weixin.qq.com/s?__biz=MzAwMDk0Nzc1Nw==&mid=2247492118&idx=6&sn=43355dd78c165e8e7edc749f7782cad5&chksm=9ae38154ad94084266429203f400ebeabcf55bea75efb8a6706d7243c623077901ce50531625&xtrack=1&scene=0&subscene=91&sessionid=1548574423&clicktime=1548574469&ascene=7&devicetype=android-28&version=2700003c&nettype=WIFI&abtest_cookie=BQABAAoACwASABMAFAAGACOXHgBXmR4Am5keAJ2ZHgC0mR4A1JkeAAAA&lang=zh_CN&pass_ticket=xM%2BIEPSMSDSSxlJ%2BpwdRMVzxi8vlLCb07WLcghDFvD%2B2Q9TUarxrc4Le6%2F2qH2n0&wx_header=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 9; zh-cn; MI 8 Build/PKQ1.180729.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.4.5'
}
htmls = requests.get(url, headers=headers)

soup = BeautifulSoup(htmls.text, 'lxml')
content = soup.select('p')
for index in range(len(content)):
    content[index] = content[index].text
    print(content[index])
