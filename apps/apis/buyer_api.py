import random

from flask import request, jsonify, current_app, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from apps.apis import api_bp
from apps.forms.buyer_form import BuyerRegisterForm, BuyerLoginForm, BuyerAddressForm

from apps.libs.codes import code_database
from apps.libs.token_tools import check_token
from apps.models.buyer_model import BuyerUserModel, db, BuyerAddressModel
from apps.models.shop_model import CartModel


@api_bp.route('/register/', methods=['POST'])
def register():
    reg_form = BuyerRegisterForm(request.form)
    if reg_form.validate():
        buyer = BuyerUserModel()
        buyer.set_attrs(reg_form.data)
        db.session.add(buyer)
        db.session.commit()
        return jsonify({'status': "true", "message": "注册成功"})
    else:
        return jsonify(
            {"status": "false", "message": '\r\n'.join(["{}:{}".format(k, v[0]) for k, v in reg_form.errors.items()])})


@api_bp.route('/sms/', methods=['GET'])
def send_sms():
    tel = request.args.get('tel')
    code = ''.join([str(random.choice(list(range(10)))) for i in range(4)])
    print("code: ", code)
    code_database[tel] = code
    return jsonify({"status": True, "message": "发送验证码成功"})


# 登陆
@api_bp.route('/login/', methods=['POST'])
def login():
    msg = "参数错误"
    login_form = BuyerLoginForm(request.form)
    if login_form.validate():
        # 验证密码
        user = BuyerUserModel.query.filter_by(username=login_form.name.data).first()
        if user:
            # 生成token
            s = Serializer(current_app.config['SECRET_KEY'], expires_in=current_app.config['EXPIRES_TIME'])
            token = s.dumps({'uid': user.id})
            # 颁发token
            resp = jsonify({"status": "true", "token": token.decode('utf-8'), "user_id": str(user.id), "username": user.username})
            resp.set_cookie("token", token.decode('utf-8'))
            return resp
        else:
            msg = "用户名或密码错误"
    return jsonify({"status": "false", "message": msg})


# 获取所有地址和单个地址
@api_bp.route('/address/', methods=['GET'])
@check_token
def get_address_list():
    user = g.current_user
    addr_id = request.args.get('id', 0)
    if addr_id:
        addr = user.addresses[int(addr_id) - 1]
        # addr = BuyerAddressModel.query.get(addr_id)
        return jsonify({**dict(addr), "id": addr_id})
    else:
        result = [{**dict(addr), "id": str(i+1)} for i, addr in enumerate(user.addresses)]
        return jsonify(result)


@api_bp.route('/address/', methods=['POST'])
@check_token
def add_address():
    user = g.current_user
    flags = request.form.get('id', 0)
    addr_form = BuyerAddressForm(request.form)
    if addr_form.validate():
        if not flags:
            # 新添加地址
            addr = BuyerAddressModel()
            addr.user_id = user.id
        else:
            addr = user.addresses[int(flags) - 1]
        addr.set_attrs(addr_form.data)
        db.session.add(addr)
        db.session.commit()
        return jsonify({"status": "true", "message": "添加成功"})
    return jsonify({"status": "false", "message": "添加失败"})


@api_bp.route('/cart/', methods=['POST'])
@check_token
def add_cart():
    user = g.current_user
    fid_list = request.form.getlist('goodsList[]')
    fnum_list = request.form.getlist('goodsCount[]')
    for x, y in zip(fid_list, fnum_list):
        cart = CartModel(user_id=user.id, foods_id=x, food_num=y)
        db.session.add(cart)
        db.session.commit()
    return jsonify({"status": "true"})
