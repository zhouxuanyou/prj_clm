from flask import jsonify, request

from apps.apis import api_bp
from apps.models.shop_model import SellerShop, db, CartModel
from apps.view_model.shop_vm import shop_view_model, food_detail_view_model


@api_bp.route('/shop_list/', methods=['GET'])
def get_shop_list():
    # 根据用户请求获取数据
    # 校验数据合法性
    # 查询数据库,得到数据
    shop = SellerShop.query.all()
    # 使用一个视图模型层,将数据库的数据转换为api接口给出的数据
    result = [shop_view_model(s) for s in shop]
    return jsonify(result)


# 获取指定店铺的详细信息(分类,菜品)
# 通过id=来标记店铺ID号
@api_bp.route('/shop/', methods=['GET'])
def shop_detail():
    # 根据用户请求获取数据
    shop_id = request.args.get("id", 0)
    shop = SellerShop.query.get(shop_id)
    if not shop:
        return jsonify({"status": "false", "message": "没有这个店铺"})
    tmp1 = [{**dict(cate),
             **{'type_accumulation': 'c%s' % (i+1)},
             **{'goods_list': food_detail_view_model(cate)}
             }
            for i, cate in enumerate(shop.categories)
            ]
    result = {**shop_view_model(shop), **{'commodity': tmp1}}

    return jsonify(result)

