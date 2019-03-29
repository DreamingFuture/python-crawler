# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 15:02
# 文件     ：12-Cookie的使用3.py
# IDE      ：PyCharm
from urllib.parse import urlencode
from urllib.request import Request, HTTPCookieProcessor, build_opener
from http.cookiejar import MozillaCookieJar
from fake_useragent import UserAgent
# 登陆
# 保存cookie
def get_cookie():
    login_url = 'http://www.sxt.cn/index/login/login.html'
    headers = {
        'User-Agent': UserAgent().chrome,
    }
    form_data = {
        'user': '15333515094',
        'password': 'qwe123'
    }
    f_data = urlencode(form_data).encode()
    request = Request(login_url, headers=headers, data=f_data)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save("cookie.txt", ignore_expires=True, ignore_discard=True)

# 获取cookie
# 访问页面
def use_cookie():
    info_url = 'http://www.sxt.cn/index/user.html'
    headers = {
        'User-Agent': UserAgent().chrome,
    }
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load('cookie.txt', ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    print(response.read().decode())


if __name__ == '__main__':
    # get_cookie()
    use_cookie()
