# 作者     ：孔庆杨
# 创建时间 ：2019/1/27 17:59
# 文件     ：斗鱼.py
# IDE      ：PyCharm
import requests
from pymongo import MongoClient
import datetime
import time

url_root = 'https://apiv2.douyucdn.cn/gv2api/rkc/roomlistV1/{}/{}/20/android?client_sys=android'

headers = {
    'User-Agent': 'User-Agent: android/5.4.0 (android 9; ; MI+8)',
    'Accept-Encoding': 'gzip'
}

'''获取更新时间'''
now_time = datetime.datetime.now()
time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def choose_url():
    '''输入你选择查询的游戏名称'''
    '''输入你选择查询的页数（每页20条主播数据）'''
    '''获取url'''
    print('可查询的斗鱼实时直播情况：LOL，王者荣耀(wang_zhe)，绝地求生(chi_ji)，dota2，DNF，炉石传说(lu_shi)，qq飞车(fei_che)，美食(mei_shi)')
    name = input('请输入(中文请输入括号中内容)你选择爬取的频道：')
    if name not in ['LOL', 'wang_zhe', 'chi_ji', 'dota2', 'DNF', 'lu_shi', 'fei_che', 'mei_shi']:
        return -1
    num = input('请输入你选择爬去的页数：')
    url_choice = {
        'LOL': '2_1',
        'wang_zhe': '2_181',
        'chi_ji': '2_270',
        'dota2': '2_3',
        'DNF': '2_40',
        'lu_shi': '2_2',
        'fei_che': '2_331',
        'mei_shi': '2_194'
    }
    url = []
    last_url = url_choice[name]
    for i in range(0, int(num)):
        element = url_root.format(last_url, i*20)
        url.append(element)
    return url, name


def use_url(url):
    '''通过url爬取数据，并存到数据库中'''
    '''删除原有数据，更新数据库'''
    info = []
    n = 1
    for url in url:
        response = requests.get(url, headers=headers).json()
        while 1:
            if response == {'error': 1001, 'data': []}:
                print('读取失败，再次尝试读取...')
                time.sleep(5)
                response = requests.get(url, headers=headers).json()
            else:
                break

        response = response['data']['list']  # 双重字典，列表中的第index项
        for index in range(len(response)):
            responses = response[index]
            print('正在查找第{}条数据...'.format(n))
            information = {
                '更新时间': time_now,
                '房号': responses['room_id'],
                '房名': responses['room_name'],
                '主播名': responses['nickname'],
                '直播类型': responses['cate2_name'],
                '标签': responses['od'],
                '在线观看人数': responses['online_num']
            }
            info.append(information)
            n = n+1
    return info


def write_mongodb(info, name):
    '''更新数据'''
    client = MongoClient().DouYu
    if name == 'LOL':
        connect = client.LOL
    elif name == 'wang_zhe':
        connect = client.wang_zhe
    elif name == 'chi_ji':
        connect = client.chi_ji
    elif name == 'dota2':
        connect = client.dota2
    elif name == 'DNF':
        connect = client.DNF
    elif name == 'lu_shi':
        connect = client.lu_shi
    elif name == 'fei_che':
        connect = client.fei_che
    else:
        connect = client.mei_shi
    connect.delete_many({})
    for index in range(len(info)):
        print('正在写入第{}条数据--'.format(index+1), info[index])
        connect.insert_one(info[index])


def main():
    choose = choose_url()
    if choose == -1:
        return -1
    print('请稍等...')
    url = choose[0]
    name = choose[1]
    info = use_url(url)
    if info == -1:
        return -1
    write_mongodb(info, name)


if __name__ == '__main__':
    if main() == -1:
        print('您所输入项，不存在！')
