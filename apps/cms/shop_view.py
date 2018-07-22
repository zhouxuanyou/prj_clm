from flask import request, render_template, redirect, url_for, abort, Response
from flask_login import current_user, login_required

from apps.cms import cms_bp
from apps.forms.shop_form import ShopBaseForm, ShopCateForm, FoodForm
from apps.models.shop_model import SellerShop, db, MenuCategory, MenuFood


############################################################
# 通用函数块
############################################################
# 检查shop_id合法性
@login_required
def check_shop_id(shop_id):
    shop = SellerShop.query.filter_by(id=shop_id, seller_id=current_user.id).first()
    if not shop:
        abort(redirect(url_for('cms.index')))
        # return redirect(url_for('cms.index'))
    return shop


#############################################################
# 资源的增加
#############################################################
@cms_bp.route('/add_shop/', endpoint='add_shop', methods=['GET', 'POST'])
@login_required
def add_shop():
    shop_form = ShopBaseForm(request.form)
    if request.method == 'POST' and shop_form.validate():
        shop = SellerShop()
        shop.set_attrs(shop_form.data)
        shop.seller = current_user
        # shop.seller_id = current_user.id
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for('cms.index'))
    return render_template('cms/add_shop.html', form=shop_form)


# 菜品分类添加
@cms_bp.route('/add_cate/<int:shop_id>/', endpoint='add_cate', methods=['GET', 'POST'])
@login_required
def add_cate(shop_id):
    # 先检查shop_id合法性
    shop = check_shop_id(shop_id)
    # 创建form类对象
    cate_form = ShopCateForm(request.form)
    if request.method == 'POST' and cate_form.validate():
        cate = MenuCategory()
        cate.set_attrs(cate_form.data)
        cate.shop = shop  # shop_id = shop.id
        db.session.add(cate)
        db.session.commit()
        return redirect(url_for('cms.index'))
    return render_template('cms/add_cate.html', form=cate_form, shop=shop)


# 菜品信息添加
@cms_bp.route('/cms/add_food/<int:shop_id>/', endpoint='add_food', methods=['GET', 'POST'])
@login_required
def add_food(shop_id):
    shop = check_shop_id(shop_id)
    food_form = FoodForm(shop, request.form)
    if request.method == 'POST' and food_form.validate():
        food = MenuFood()
        food.set_attrs(food_form.data)
        food.shop = shop  # shop_id = shop.id
        db.session.add(food)
        db.session.commit()
        return redirect(url_for('cms.index'))
    return render_template('cms/add_food.html', form=food_form, shop=shop)


#############################################################
# 资源的更新
#############################################################
# 店铺的信息更新
@cms_bp.route('/update_shop/<int:shop_id>/', endpoint='update_shop', methods=['GET', 'POST'])
@login_required
def update_shop(shop_id):
    shop = check_shop_id(shop_id)
    if request.method == 'GET':
        shop_form = ShopBaseForm(data=dict(shop))
    elif request.method == 'POST':
        shop_form = ShopBaseForm(request.form)
        if shop_form.validate():
            shop.set_attrs(shop_form.data)
            db.session.add(shop)
            db.session.commit()
            return redirect(url_for('cms.index'))
    return render_template('cms/update_shop.html', form=shop_form)


#############################################################
# 资源的查看
#############################################################
@cms_bp.route('/show_food/<int:shop_id>/', endpoint='show_food', methods=['GET'])
@login_required
def show_food(shop_id):
    shop = check_shop_id(shop_id)
    cates = shop.categories
    return render_template('cms/show_foods.html', cates=cates, shop=shop)


@cms_bp.route('/show_cate/<int:shop_id>/', endpoint='show_cate', methods=['GET'])
@login_required
def show_cate(shop_id):
    shop = check_shop_id(shop_id)
    cates = shop.categories
    result = [{'name': cate.name, 'total': len(cate.foods)}
              for cate in cates]
    return render_template('cms/show_cates.html', cates=result, shop=shop)
