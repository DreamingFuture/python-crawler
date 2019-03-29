# 作者     ：孔庆杨
# 创建时间 ：2019/1/2020:51
# 文件     ：爬虫初接触.py
# IDE      ：PyCharm
import re
from urllib import request


class Answer:
    url = 'https://tieba.baidu.com/p/4990813310'

    def __read(self, url):
        answer = request.urlopen(url)
        htmls = answer.read()
        htmls = htmls.decode('utf-8', 'ignore')
        htmls = re.findall('style="display:;"> ([\s\S]*?)</div>', htmls)
        return htmls

    def __handle(self, htmls):
        HTMLS = []
        for element in htmls:
            if '<br>' in element:
                HTMLS.append(element)

                for element_index in range(len(HTMLS)):
                    HTMLS[element_index] = HTMLS[element_index].strip()
                    HTMLS[element_index] = re.sub('(<br>){1,5}', '\n', HTMLS[element_index])
        return HTMLS

    def __print(self, htmls):
        print("\n".join(htmls))

    def go(self):
        htmls = self.__read(Answer.url)
        htmls = self.__handle(htmls)
        self.__print(htmls)


if __name__ == '__main__':
    answer = Answer()
    answer.go()
