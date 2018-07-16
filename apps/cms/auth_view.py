from flask import render_template, request

from apps.cms import cms_bp
from apps.forms.seller_form import SellerRegisterForm


# 创建首页
@cms_bp.route('/', endpoint='index')
def seller_index():
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
            return "success"
        # 一旦有错误，他自动在reg.errors里进行绑定
        return render_template('cms/register.html', form=reg)
