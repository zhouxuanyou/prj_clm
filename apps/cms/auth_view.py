from flask import render_template, request, jsonify, session, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from apps.cms import cms_bp
from apps.forms.seller_form import SellerRegisterForm, SellerLoginForm
from apps.models.seller_model import SellerUser, db


# 创建首页
@cms_bp.route('/', endpoint='index')
def seller_index():
    shop = []
    if current_user.is_authenticated:
        shop = current_user.shop
        print(shop)
    return render_template('cms/index.html', shop=shop)


# 创建注册页面
@cms_bp.route('/register/', endpoint='register', methods=['GET', 'POST'])
def seller_register():
    if request.method == 'GET':
        reg = SellerRegisterForm(request.form)
        return render_template('cms/register.html', form=reg)
    elif request.method == 'POST':
        # 利用用户输入的数据，实例化表单验证器，使用用户的post提交的数据
        reg = SellerRegisterForm(request.form)
        # 利用验证器模块的校验方式，产生校验错误的数据
        if reg.validate():
            user = SellerUser()
            user.set_attrs(reg.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('cms.index'))
        # 一旦有错误，他自动在reg.errors里进行绑定
        return render_template('cms/register.html', form=reg)


# 实现用户登陆视图
@cms_bp.route('/login/', endpoint='login', methods=['GET', 'POST'])
def seller_login():
    login_form = SellerLoginForm(request.form)
    # 当请求为POST
    if request.method == 'POST' and login_form.validate():
        # 先把用户请求的数据，交给验证层进行验证
        # 一旦验证通过，再进行密码校验
        # 先通过用户名查找到用户的对象(记录)，在该记录下去访问password，和明文进行哈希的相等校验
        user = SellerUser.query.filter_by(username=login_form.username.data).first()
        if user and user.check_password(login_form.password.data):
            # 把当前请求对应的session空间，进行了赋值操作
            login_user(user)
            # 判断是否传递了next的参数
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('cms.index')
            return redirect(next_page)
        login_form.password.errors = ['用户名或密码错误']
    return render_template('cms/login.html', form=login_form)


@cms_bp.route('/logout/', endpoint='logout')
def seller_logout():
    logout_user()
    return redirect(url_for('cms.index'))


# 商家资料的视图函数
@cms_bp.route('/shop/', endpoint='shop')
@login_required                             # 必须放置在视图函数最近地方
def seller_shop():
    return "在商家的资料里..."
