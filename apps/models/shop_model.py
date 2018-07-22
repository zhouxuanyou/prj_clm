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


# 店铺菜品分类
class MenuCategory(BaseModel):
    # 分类名称
    name = db.Column(db.String(32))
    # 分类描述
    description = db.Column(db.String(128), default='')
    # 是否默认
    is_default = db.Column(db.Boolean, default=False)
    # 归属店铺
    shop_id = db.Column(db.Integer, db.ForeignKey('seller_shop.id'))

    shop = db.relationship('SellerShop', backref='categories')

    def __repr__(self):
        return "<MenuCate {}>".format(self.name)


# 菜品数据模型
# 菜品信息
class MenuFood(BaseModel):
    # 菜品名称
    food_name = db.Column(db.String(64))
    # 菜品评分
    rating = db.Column(db.Float, default=5.0)
    # 归属店铺
    shop_id = db.Column(db.Integer, db.ForeignKey('seller_shop.id'))
    # 归属分类
    category_id = db.Column(db.Integer, db.ForeignKey('menu_category.id'))
    cates = db.relationship('MenuCategory', backref='foods')    # 添加一条关系
    # 菜品价格
    food_price = db.Column(db.DECIMAL(6, 2), default=0.0)
    # 菜品描述
    description = db.Column(db.String(128), default='')
    # 月销售额
    month_sales = db.Column(db.Integer, default=0)
    # 评分数量
    rating_count = db.Column(db.Integer, default=0)
    # 提示信息
    tips = db.Column(db.String(128), default='')
    # 菜品图片
    food_img = db.Column(db.String(128), default='')

    def __repr__(self):
        return "<Food: {}-{}>".format(self.food_name, self.food_price)
