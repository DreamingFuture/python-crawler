# 作者     ：孔庆杨
# 创建时间 ：2019/1/28 9:56
# 文件     ：孔庆杨_task7.py
# IDE      ：PyCharm
import requests
from pymongo import MongoClient
import datetime
import time

headers = {
    'User-Agent': 'User-Agent: android/5.4.0 (android 9; ; MI+8)',
    'Accept-Encoding': 'gzip',

}

url_root = 'https://apiv2.douyucdn.cn/gv2api/rkc/roomlistV1/{}/0/20/android?client_sys=android'
last_url = ['2_1', '2_181', '2_270', '2_174', '2_33', '2_124', '2_19', '2_350', '2_40', '2_3','2_201',
            '2_194', '2_2', '2_175', '2_434', '2_6', '2_347', '2_331', '2_136', '2_405']

'''获取更新时间'''
now_time = datetime.datetime.now()
time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def use_url():
    info = []

    '''处理所有的url信息'''
    for index in range(len(last_url)):

        print('正在读取第{}个网址数据'.format(index+1))

        url = last_url[index]
        url = url_root.format(last_url[index])
        response = requests.get(url, headers=headers).json()

        '''访问失败，进入死循环，重复访问'''
        while 1:
            if response == {'error': 1001, 'data': []}:
                print('读取失败，再次尝试读取...')
                time.sleep(5)
                response = requests.get(url, headers=headers).json()
            else:
                break

        n = 1
        response = response['data']['list']

        for num in range(0, 10):
            print('正在读取第{}个网址，第{}条信息'.format(index+1, n))
            information = {
                '更新时间': time_now,
                '直播类型': response[num]['cate2_name'],
                '房间名': response[num]['room_name'],
                '主播名': response[num]['nickname'],
                '在线观看人数': response[num]['online_num']
            }
            info.append(information)
            n = n+1
    return info


def write_mongodb(info):
    '''写入数据库'''
    client = MongoClient().DouYu
    n = 1
    client.kqy_task7.delete_many({})
    print('正在写入全部数据')
    client.kqy_task7.insert_many(info)
    print('数据已全部写入')


def main():
    info = use_url()
    write_mongodb(info)


if __name__ == '__main__':
    main()
