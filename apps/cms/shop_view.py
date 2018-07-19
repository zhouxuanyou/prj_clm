from flask import request, render_template, redirect, url_for
from flask_login import current_user, login_required

from apps.cms import cms_bp
from apps.forms.shop_form import ShopBaseForm
from apps.models.shop_model import SellerShop, db


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
