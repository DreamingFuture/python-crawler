# 作者     ：孔庆杨
# 创建时间 ：2019/1/25 17:29
# 文件     ：python连接mongodb.py
# IDE      ：PyCharm
import random
from random import choice

from bson import ObjectId
from pymongo import MongoClient


class textmongo():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['students']

    def add_one(self):
        '''新增数据'''
        post = {
            'name': choice('赵，钱，孙，李，周，吴，郑，王'.split('，')) +
                    choice('''佳妮、康尼、昱薪、沐熙、嘉宥、嘉颀、瑞敏、天琪
                    、迪娜、柯楠、羽婷、秋羽、书成、煜晗、思琪、亚娜、妮可、莎娜
                    、长云、新宇、柯楠、嘉宥、宇健、天庆、怀晨、嘉诚、璟赫、泓运
                    、瑜玧、峥嵘、嘉佑、邵麒、成程、均恺、凯威、铭伟、旭成、少安
                    、建军、卫东、柯霖、志铭、康森'''.split('、')),
            'age': random.randint(10, 40),
            'sex': choice(['男', '女'])
        }
        return self.db.students.insert_one(post)

    def get_one(self):
        '''查询一条数据'''
        return self.db.students.find_one()

    def get_more(self):
        '''查询多条数据'''
        '''{'_id': 0}取消输出id'''
        '''projection=['name']输出id和name'''
        return self.db.students.find({'age': {'$gte': 18}})

    def get_ont_from_oid(self, oid):
        '''查询指定id的数据'''
        obj = ObjectId(oid)
        return self.db.students.find_one({'_id': obj})

    def update(self):
        '''修改数据'''
        # 修改一条数据
        rest = self.db.students.update_one({'age': 25}, {'$inc': {'age': 2}})
        return rest
        # 修改多条数据
        # return self.db.students.update_many({}, {'$inc': {'age': 10}})

    def delete(self):
        '''删除数据'''
        # 删除一条数据（默认删除第一条）
        # return self.db.students.delete_one({'age': 27})
        # 删除多条数据
        # return self.db.students.delete_many({'age': 38})
        # 删除全部数据
        return self.db.students.delete_many({})


def main():
    obj = textmongo()
    n = 0
    while n < 100:
        rest = obj.add_one()
        n = n+1
        print(rest.inserted_id)
    # rest = obj.get_one()
    # print(rest['_id'])
    # rest = obj.get_more()
    # for age in rest:
    #     print(age)
    # rest = obj.get_ont_from_oid("5c4ac490ff16433a5a919645")
    # print(rest)
    # rest = obj.update()
    # print(rest.matched_count)  # 修改前匹配到几个
    # print(rest.modified_count)  # 修改了几个
    # rest = obj.delete()
    # print(rest.deleted_count)


if __name__ == '__main__':
    main()
