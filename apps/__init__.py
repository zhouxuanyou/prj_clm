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


# 登陆插件的注册
def register_lm(app):
    from apps.forms.login_man import login_manager
    login_manager.init_app(app)

    login_manager.login_view = 'cms.login'


# 产生后台服务的app
def create_app():
    app = Flask(__name__)
    # 配置app的一些跟数据库相关的配置项
    app.config.from_object('apps.private_conf')

    # 数据库对象的app绑定
    register_db(app)

    # 注册bs
    register_bs(app)

    # 注册login manager插件
    register_lm(app)

    # 把蓝图对象跟app进行绑定
    register_bp(app)

    return app


# 注册API蓝图
def register_api_bp(app):
    from apps.apis import api_bp
    app.register_blueprint(api_bp)


# 产生一个client的app
def create_api_app():
    app = Flask(__name__, static_url_path='/c', static_folder='./client_web')

    # 数据库配置
    app.config.from_object('apps.private_conf')

    # 注册数据库
    register_db(app)

    register_api_bp(app)

    return app
