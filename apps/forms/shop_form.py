from wtforms import Form
from wtforms import StringField, BooleanField, DecimalField
from wtforms import validators


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
