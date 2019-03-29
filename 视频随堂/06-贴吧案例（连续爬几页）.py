# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 10:51
# 文件     ：06-贴吧案例（连续爬几页）.py
# IDE      ：PyCharm
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    reqeuest = Request(url, headers=headers)
    response = urlopen(reqeuest).read()
    return response


def save_html(filenaem, html_byts):
    with open(filenaem, 'wb') as f:
        f.write(html_byts)


def main():
    content = input('请输入要下载的内容：')
    num = input('请输入要下载多少页：')
    for pn in range(int(num)):
        args = {
            'pn': pn * 50,
            'kw': content
        }
        args = urlencode(args)
        html_byts = get_html('http://tieba.baidu.com/f?ie=utf-8&{}'.format(args))
        filename = '%s百度贴吧第%s页.html' % (content, pn + 1)
        print('正在下载' + filename)
        save_html(filename, html_byts)


if __name__ == "__main__":
    main()
