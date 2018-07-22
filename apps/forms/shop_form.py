from wtforms import Form
from wtforms import StringField, BooleanField, DecimalField, SelectField
from wtforms import validators
from flask_login import current_user


class ShopBaseForm(Form):
    shop_name = StringField(label="店铺名称",
                            validators=[validators.InputRequired(message="请输入店铺名称"),
                                        validators.Length(max=32, message="店铺名称不能超过32个字符"),
                                        ],
                            )
    is_ontime = BooleanField(label="准时送达", default=False)
    is_bird = BooleanField(label="蜂鸟快递", default=False)
    is_bao = BooleanField(label="提供保险", default=False)
    is_fp = BooleanField(label="提供发票", default=False)
    is_zun = BooleanField(label="准标识", default=False)

    start_cost = DecimalField(label="起送价格",
                              validators=[validators.InputRequired(message="填写起送价格")],
                              )
    send_cost = DecimalField(label="配送费用",
                             validators=[validators.InputRequired(message="填写配送费用")],
                             )

    notice = StringField(label="店铺公告",
                         validators=[validators.Length(max=210, message="不能超过128个字符")],
                         )
    discount = StringField(label="优惠信息", validators=[validators.Length(max=210, message="不能超过128个字符")],
                           )


class MySelectField(SelectField):
    def pre_validate(self, form):
        for v, _ in self.choices:
            if self.data == v:
                break
        else:
            raise ValueError(self.gettext('请选择正确分类'))


class ShopCateForm(Form):
    name = StringField(label="分类名称",
                       validators=[validators.InputRequired(message="请输入分类名称"),
                                   validators.Length(max=32, message="分类名称不能超过32个字符"),
                                   ],
                       )
    # 分类描述
    description = StringField(label="分类描述",
                              validators=[validators.Length(max=128, message="分类描述不能超过128个字符")],
                              default='',
                              )
    # 是否默认
    is_default = BooleanField(label="默认展示", default=False)


# 菜品信息的form验证类
class FoodForm(Form):
    food_name = StringField(label="菜品名称",
                            validators=[validators.InputRequired(message="请输入菜品名称"),
                                        validators.Length(max=64, message="菜品名称不能超过64个字符"),
                                        ],
                            )
    # 归属分类
    category_id = SelectField(label="所属分类", coerce=int)

    # 菜品价格
    food_price = DecimalField(label="菜品价钱", places=2,
                              validators=[validators.NumberRange(min=0, max=9999, message="价钱超出范围"),
                                          validators.InputRequired(message="请输入菜品价格"),
                                          ]
                              )
    # 菜品描述
    description = StringField(label="菜品描述",
                              validators=[
                                  validators.Length(max=128, message="不能超过128字符"),
                              ])
    # 提示信息
    tips = StringField(label="菜品提示信息",
                       validators=[
                           validators.Length(max=128, message="不能超过128字符"),
                       ])

    def __init__(self, shop, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(cate.id, cate.name) for cate in shop.categories]
