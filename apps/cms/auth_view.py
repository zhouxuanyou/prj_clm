from flask import render_template, request, jsonify, session

from apps.cms import cms_bp
from apps.forms.seller_form import SellerRegisterForm, SellerLoginForm
from apps.models.seller_model import SellerUser, db


# 创建首页
@cms_bp.route('/', endpoint='index')
def seller_index():
    if session.get('is_login'):
        return "有用户登陆"
    else:
        return "未登陆状态"
    return render_template('cms/index.html')


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
            return "success"
        # 一旦有错误，他自动在reg.errors里进行绑定
        return render_template('cms/register.html', form=reg)


# 实现用户登陆视图
@cms_bp.route('/login/', endpoint='login', methods=['GET', 'POST'])
def seller_login():
    # 当请求为POST
    if request.method == 'POST':
        # 先把用户请求的数据，交给验证层进行验证
        login_form = SellerLoginForm(request.form)
        if login_form.validate():
            # 一旦验证通过，再进行密码校验
            # 先通过用户名查找到用户的对象(记录)，在该记录下去访问password，和明文进行哈希的相等校验
            user = SellerUser.query.filter_by(username=login_form.username.data).first()
            if user and user.check_password(login_form.password.data):
                # 把当前请求对应的session空间，进行了赋值操作
                session['is_login'] = True
                return "success"
            login_form.password.errors = ['用户名或密码错误']
        return jsonify(login_form.errors)
