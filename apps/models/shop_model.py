from apps.models.base import BaseModel, db


# 商家店铺信息表
class SellerShop(BaseModel):
    # 店铺名称
    shop_name = db.Column(db.String(32), nullable=False)
    # 和商家的关联关系
    seller_id = db.Column(db.Integer, db.ForeignKey('seller_user.id'))
    # 建立一个反向关系
    seller = db.relationship("SellerUser", backref="shop")
    # 店铺logo
    shop_logo = db.Column(db.String(128), default='')
    # 店铺评分
    shop_rating = db.Column(db.Float, default=5.0)
    # 是否是品牌
    is_brand = db.Column(db.Boolean, default=False)
    # 是否准时送达
    is_ontime = db.Column(db.Boolean, default=True)
    # 是否蜂鸟配送
    is_bird = db.Column(db.Boolean, default=True)
    # 是否保险
    is_bao = db.Column(db.Boolean, default=False)
    # 是否有发票
    is_fp = db.Column(db.Boolean, default=True)
    # 是否准标识
    is_zun = db.Column(db.Boolean, default=False)
    # 起送价格
    start_cost = db.Column(db.Float, default=0.0)
    # 配送费
    send_cost = db.Column(db.Float, default=0.0)
    # 店铺公告
    notice = db.Column(db.String(210), default='')
    # 优惠信息
    discount = db.Column(db.String(210), default='')

    def __repr__(self):
        return '<Shop {} --- {}>'.format(self.shop_name, self.seller)
