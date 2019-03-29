# 作者     ：孔庆杨
# 创建时间 ：2019/1/27 11:42
# 文件     ：虎扑NBA球员排名.py
# IDE      ：PyCharm
import requests
from pymongo import MongoClient

url_root = 'https://m.hupu.com/nba/stats/players/pergame-pts?api=1&page={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 '
                  'Mobile Safari/537.36 kanqiu/7.3.2.17891/7306 isp/-1 network/-1'

}


def write_mongodb(information):
    client = MongoClient().NBA
    client.team_member_list.insert_one(information)


def main():
    i = 1
    for n in range(1, 15):
        url = url_root.format(n)
        response = requests.get(url, headers=headers).json()['ranks']
        for index in range(len(response)):
            information = {
                '排名': response[index]['rank'],
                '姓名': response[index]['player_name'],
                '编号': response[index]['player_id'],
                '得分': response[index]['rank_value'],
                '篮板': response[index]['reb'],
                '助攻': response[index]['asts'],
                '效力球队': response[index]['team_name']
            }
            print('正在写入第{}名球员的数据'.format(i))
            write_mongodb(information)
            i = i + 1


if __name__ == '__main__':
    main()
