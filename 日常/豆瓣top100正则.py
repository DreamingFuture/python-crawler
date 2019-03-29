# 作者     ：孔庆杨
# 创建时间 ：2019/1/23 20:06
# 文件     ：豆瓣图书top100.py
# IDE      ：PyCharm
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

from pymongo import MongoClient


def get_htmls():
    htmls = ''
    for num in range(4):
        last_url = {
            'start': num * 25
        }
        root_url = 'https://www.douban.com/doulist/45004834/?{}'
        headers = {
            'User-Agent': UserAgent().random
        }
        response = requests.get(root_url, headers=headers, params=last_url)
        htmls = htmls + response.text
    print(htmls)
    with open('豆瓣TOP100.html', 'w', encoding='utf-8') as f:
        f.write(htmls)


def read_htmls(htmls):
    soup = BeautifulSoup(htmls, 'lxml')
    book_name = soup.select('div[class="title"]')
    book_autor = re.findall('作者: ([\s\S]*?)<br />', htmls)
    book_publisher = re.findall('出版社: ([\s\S]*?)<br />', htmls)
    book_score = soup.find_all(class_='rating_nums')
    book_url = re.findall('<div class="title">\n.*?"([http:\s\S]*?)" target="_blank">', htmls)
    for index in range(len(book_publisher)):
        book_publisher[index] = book_publisher[index].replace('\n', '').replace(' ', '')
        if '中国基督教协会' == book_publisher[index]:
            book_autor.insert(index, '')
        book_name[index] = book_name[index].text.replace('\n', '').replace(' ', '')
        book_autor[index] = book_autor[index].replace('\n', '').replace(' ', '')
        book_score[index] = book_score[index].text.replace('\n', '').replace(' ', '')
    return book_name, book_autor, book_url, book_publisher, book_score


def read_eachbook(htmls_eachbook):
    pages = re.findall('页数:</span> (.*?)<', htmls_eachbook, re.S)
    price = re.findall('定价:</span> (.*?)<', htmls_eachbook, re.S)
    cover = re.findall('装帧:</span> (.*?)<', htmls_eachbook, re.S)
    return pages, price, cover


def write_mangodb(book_name, book_autor, book_price, book_url, book_pages,
                  book_publisher, book_cover, book_score):
    client = MongoClient()
    book = client['book']
    for index in range(len(book_name)):
        if '聖經' == book_name[index]:
            book_pages.insert(index, '')
            book_price.insert(index, '')
        if '明朝那些事儿' == book_name[index]:
            book_pages.insert(index, '')
    book.book_info.delete_many({})
    for index in range(len(book_name)):
        print('正在录入第{}条数据...'.format(index + 1))
        post = {
            'TOP': index + 1,
            '评分': book_score[index],
            '书名': '《' + book_name[index] + '》',
            '作者': book_autor[index],
            '定价': book_price[index],
            '页数': book_pages[index],
            '装帧': book_cover[index],
            '出版社': book_publisher[index],
            '豆瓣网址': book_url[index]
        }
        book.book_info.insert_one(post)
    print('录入完成')


if __name__ == '__main__':
    # get_htmls()
    with open(r'E:\A学习学习\py_work\爬虫\孔庆杨_task6\豆瓣TOP100.html', 'r', encoding='utf-8') as f:
        htmls = f.read()
    book = read_htmls(htmls)
    book_name = book[0]
    book_autor = book[1]
    book_url = book[2]
    book_publisher = book[3]
    book_score = book[4]
    # 应该有一个html获取，在孔庆杨_task6中已经做完了
    with open(r'E:\A学习学习\py_work\爬虫\孔庆杨_task6\豆瓣TOP100_各本书.html', 'r', encoding='utf-8') as f:
        htmls_eachbook = f.read()
    eachbook = read_eachbook(htmls_eachbook)
    book_pages = eachbook[0]
    book_price = eachbook[1]
    book_cover = eachbook[2]
    write_mangodb(book_name, book_autor, book_price, book_url, book_pages,
                  book_publisher, book_cover, book_score)
