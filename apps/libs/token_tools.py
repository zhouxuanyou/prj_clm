from flask import request, jsonify, current_app, g
from functools import wraps
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from apps.models.buyer_model import BuyerUserModel


def check_token(fn):
    @wraps(fn)
    def decroated(*args, **kwargs):
        # 获取token
        token = request.cookies.get('token')
        if not token:
            return jsonify({"status": "false", "message": "没有token"})
        # 解析token
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return jsonify({"status": "false", "message": "非法token"})
        uid = data.get('uid', 0)
        user = BuyerUserModel.query.get(uid)
        if not user:
            return jsonify({"status": "false", "message": "没有该用户"})
        g.current_user = user
        return fn(*args, **kwargs)
    return decroated
