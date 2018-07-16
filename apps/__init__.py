"""
app的创建，这个文件叫做工厂模式
建议以函数进行封装
"""
from flask import Flask


# 数据库绑定的注册函数
def register_db(app):
    from apps.models.base import db
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    # 配置app的一些跟数据库相关的配置项
    app.config.from_object('apps.private_conf')

    # 数据库对象的app绑定
    register_db(app)

    return app
