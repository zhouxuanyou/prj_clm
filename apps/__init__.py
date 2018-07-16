"""
app的创建，这个文件叫做工厂模式
建议以函数进行封装
bootstrap插件跟其他插件没有任何冲突，可以最开始导入
"""
from flask import Flask


# 数据库绑定的注册函数
def register_db(app):
    from apps.models.base import db
    db.init_app(app)


# 蓝图注册函数
def register_bp(app):
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


# bootstrap的插件注册
def register_bs(app):
    from flask_bootstrap import Bootstrap
    Bootstrap(app)


def create_app():
    app = Flask(__name__)
    # 配置app的一些跟数据库相关的配置项
    app.config.from_object('apps.private_conf')

    # 数据库对象的app绑定
    register_db(app)

    # 注册bs
    register_bs(app)

    # 把蓝图对象跟app进行绑定
    register_bp(app)

    return app
