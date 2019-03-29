# 作者     ：孔庆杨
# 创建时间 ：2019/1/2111:26
# 文件     ：百度贴吧文字爬虫.py
# IDE      ：PyCharm
# 初次网站 ：'https://tieba.baidu.com/p/6009666124'
from urllib import request
import re


class baidu():
    url = 'https://tieba.baidu.com/p/5965430869'

    def __read(self):
        r = request.urlopen(baidu.url)
        htmls = r.read()
        htmls = htmls.decode('utf-8')
        htmls = re.findall('<cc>([\s\S]*?)</cc>', htmls)
        return htmls

    def __chose_content(self, htmls):
        answer =[]
        for index in range(len(htmls)):
            add = ''.join(re.findall('<div class="post_bubble_middle_inner">([\s\S]*?)</div></div>', htmls[index]))
            if add !='':
                answer.append(add)
            else:
                add = ''.join(re.findall('class="d_post_content j_d_post_content " style="display:;">([\s\S]*?)</div>', htmls[index]))

                answer.append(add)
            pop1 = re.findall('<img[\s\S]*?>', answer[index])
            if pop1 != []:
                pop1 = ''.join(pop1)
                answer[index] = re.sub(pop1, '[图片]', answer[index])
            answer[index] = re.sub('<br>', '\n\t', answer[index])
            answer[index] = answer[index].strip()
        return answer

    def __build_print(self, answer):
        for index in range(len(answer)):
            print(index+1, '楼:', answer[index])

    def go(self):
        htmls = self.__read()
        answer = self.__chose_content(htmls)
        self.__build_print(answer)


baidu = baidu()
baidu.go()