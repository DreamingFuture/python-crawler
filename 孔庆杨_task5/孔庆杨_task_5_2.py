# 作者     ：孔庆杨
# 创建时间 ：2019/1/21,21:15
# 文件     ：task_5_2.py
# IDE      ：PyCharm
from urllib import request
import re
import os


class Picture(object):
    url = [
        'https://tieba.baidu.com/photo/g/bw/picture/list?kw=%E5%A4%A7%E6%B5%B7&alt=jview&rn=200&tid=2125145202&pn=1&ps=1&pe=40&info=1&_=1548060342941',
        'https://tieba.baidu.com/photo/g/bw/picture/list?kw=%E5%A4%A7%E6%B5%B7&alt=jview&rn=200&tid=2125145202&pn=1&ps=40&pe=79&wall_type=h&_=1548062781588']

    def go(self):
        htmls = self.__read()[0]
        judges = self.__read()[1]
        self.__write(htmls, judges)

    @staticmethod
    def __read():
        htmls = []
        judges = []
        for url in picture.url:
            r = request.urlopen(url).read().decode('gbk')  # 全部html
            r = re.findall(',"index":[\s\S]*?"pwrapper_height"', r)  # r是列表
            judge = re.findall('"descr":"([\w\W]*?)","', ''.join(r))  # 筛选判断文件格式的条件
            html = re.findall('murl":"([\s\S]*?)","', ''.join(r))  # 筛选图片
            htmls.extend(html)
            judges.extend(judge)
        return htmls, judges

    @staticmethod
    def __write(htmls, judges):

        if os.path.exists(r'E:\A学习学习\py_work\爬虫\孔庆杨_task5\图片'):
            print('目录存在，开始获取图片')
        else:
            print('目录不存在，正在创建目录')
            os.mkdir(r'E:\A学习学习\py_work\爬虫\孔庆杨_task5\图片')
            print('目录创建完成，开始获取图片')

        for index in range(len(htmls)):
            print('正在获取第%d张图片' % (index + 1))
            if judges[index] == '':
                request.urlretrieve(htmls[index], r'E:\A学习学习\py_work\爬虫\孔庆杨_task5\图片\ocean%d.gif' % (int(index + 1)))
            else:
                request.urlretrieve(htmls[index], r'E:\A学习学习\py_work\爬虫\孔庆杨_task5\图片\ocean%d.jpg' % (int(index + 1)))
        print("图片全部获取完成！(*^▽^*)")


picture = Picture()
picture.go()
