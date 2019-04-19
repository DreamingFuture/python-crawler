# 作者     ：孔庆杨
# 创建时间 ：2019/1/21,17:40
# 文件     ：孔庆杨_task5.py
# IDE      ：PyCharm
from urllib import request
import re


class picture():
    def __read(self, each_url):
        r = request.urlopen(each_url).read()
        htmls = r.decode('utf-8', 'ignore')
        return htmls

    def __judge(self, htmls):
        judge = re.findall('"descr":"([\s\S]*?)","', htmls)
        print(judge)
        return judge

    def __refind(self,htmls):
        htmls = re.findall('http:[\s\S]*?.jpg', htmls)
        return htmls

    def __write(self, htmls, n, judge):
        answer = []

        for index in range(len(htmls)):
            if index % 2 == 0:
                answer.append(htmls[index])

        for index in range(len(answer)):
            n = n+1
            print('开始获取第%d张图片' % (n))
            if type(judge[index]) != 'int':
                request.urlretrieve(answer[index], 'E:\A学习学习\py_work\爬虫\孔庆杨_task5\图片\ocean%d.gif' % (n))
            else:
                request.urlretrieve(answer[index], 'E:\A学习学习\py_work\爬虫\孔庆杨_task5\图片\ocean%d.jpg' % (n))
        return n

    def go(self):
        url = ['https://tieba.baidu.com/photo/g/bw/picture/list?kw=%E5%A4%A7%E6%B5%B7&alt=jview&rn=200&tid=2125145202&pn=1&ps=1&pe=40&info=1&_=1548060342941',
               'https://tieba.baidu.com/photo/g/bw/picture/list?kw=%E5%A4%A7%E6%B5%B7&alt=jview&rn=200&tid=2125145202&pn=1&ps=40&pe=79&wall_type=h&_=1548062781588']
        n = 0
        for each_url in url:
            htmls = []
            htmls = self.__read(each_url)
            judge = self.__judge(htmls)
            htmls = self.__refind(htmls)
            n = self.__write(htmls, n, judge)
        if htmls !=[]:
            print("获取成功！(*^▽^*)")
        else:
            print('获取失败！(ー`´ー)')

picture = picture()
picture.go()
