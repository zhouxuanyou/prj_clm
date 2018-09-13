from werkzeug.security import generate_password_hash, check_password_hash
from apps.models.base import BaseModel, db


class BuyerUserModel(BaseModel):
    # 买家用户名
    username = db.Column(db.String(32), unique=True)
    # 买家密码
    _password = db.Column("password", db.String(128))
    # 买家电话号码
    tel = db.Column(db.String(16), unique=True)
    # token
    token = db.Column(db.String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_pwd(self, raw_pwd):
        return check_password_hash(self._password, raw_pwd)


# 买家地址表
class BuyerAddressModel(BaseModel):
    user_id = db.Column(db.Integer, db.ForeignKey('buyer_user_model.id'))
    user = db.relationship("BuyerUserModel", backref="addresses")
    # 省
    provence = db.Column(db.String(8))
    # 市
    city = db.Column(db.String(16))
    # 县
    area = db.Column(db.String(16))
    # 详细地址
    detail_address = db.Column(db.String(64))
    # 收货人姓名
    name = db.Column(db.String(32))
    # 收货人电话
    tel = db.Column(db.String(16))

    def keys(self):
        return "provence", "city", "area", "detail_address", "name", "tel"
