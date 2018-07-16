"""
app的创建，这个文件叫做工厂模式
建议以函数进行封装
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    return app
