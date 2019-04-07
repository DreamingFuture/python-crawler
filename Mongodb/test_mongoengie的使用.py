# 作者     ：孔庆杨
# 创建时间 ：2019/1/26 9:18
# 文件     ：test_mongoengie的使用.py
# IDE      ：PyCharm
from mongoengine import *

connect('students')

sex_choice = (
    '男', 'male',
    '女', 'female',
)
oid = '5c4b1278e739194538280bfb'
# 排序
meta = {
    'collection': 'students',
    'ordering': ['-age']
}


class grades(EmbeddedDocument):
    subject = StringField()
    score = FloatField()


class students(Document):
    '''学生信息'''
    name = StringField(required=True, max_length=10)
    age = IntField(required=True)
    sex = StringField(required=True, choices=sex_choice)
    grade = FloatField()
    grades = ListField(EmbeddedDocumentField(grades))


class test_mongoengine():
    def add_one(self):
        '''添加1条数据到数据库'''
        yuwen = grades(
            subject='语文',
            score=90
        )
        shuxue = grades(
            subject='数学',
            score=100)
        stu_obj = students(
            name='李四',
            age=17,
            sex='male',
            grades=[yuwen, shuxue]
        )
        stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        '''查询一条数据'''
        return students.objects.first()

    def get_more(self):
        '''查询多条数据'''
        return students.objects.all()

    def get_from_oid(self, oid):
        '''根据id来获取数据'''
        return students.objects.filter(id=oid).first()


def main():
    obj = test_mongoengine()
    # rest = obj.add_one()
    # print(rest)
    rest = obj.get_one()
    print(rest.name)
    # rest = obj.get_more()
    # print(rest.name)



    # rest = obj.get_from_oid(oid)
    # print(rest.name)


if __name__ == '__main__':
    main()


