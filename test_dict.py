"""
字典和对象,不是一个内容
字典是可以序列化成字符串,转换为json格式, 实现form的实例化
普通类实例化的对象,默认不能序列化为json

dict(对象)时:
    {"key1": value1}
怎么保证对象的众多属性中,需要把哪些属性加入到字典的key中
    在类中只要定义了def keys(self): 函数, 他返回的结果进行遍历
Value:
    通过调用类的__getitem__魔术方法
"""
from flask import Flask, jsonify

app = Flask(__name__)

a = {'name': 'zzz'}


class Person:
    bbb = 200

    def __init__(self, name):
        self.name = name
        self.age = 10

    def keys(self):
        return "name", "age", "bbb"

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)


p = Person("bbb")

print(a['name'])
# print(jsonify(a))
print(dict(p))

@app.route('/',)
def index():
    data = {
        'name': p.name
    }
    return jsonify(data)


# if __name__ == '__main__':
#     app.run()
# print(p['name'])

