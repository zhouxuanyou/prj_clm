from wtforms import Form, IntegerField
from wtforms import StringField
from wtforms import validators

from apps.libs.codes import code_database
from apps.models.buyer_model import BuyerUserModel


class BuyerRegisterForm(Form):
    TEL_REG = r'^((13[0-9])|(14[5,7])|(15[^4])|(17[0,3,5-8])|(18[0-9])|166|198|199)\d{8}$'
    username = StringField(validators=[validators.InputRequired(message="请输入用户名信息"),
                                       validators.Length(min=3, message="用户名不能少于3个字符"),
                                       validators.Length(max=32, message="用户名不能超过32个字符"),
                                       ],
                           )
    # 买家密码
    password = StringField(validators=[validators.InputRequired(message="请输入密码"),
                                       validators.Length(min=3, message="密码不能少于3个字符"),
                                       validators.Length(max=16, message="密码不能超过16个字符"),
                                       ],
                           )
    # 电话号码
    tel = StringField(validators=[validators.InputRequired(message="请输入电话号码"),
                                  validators.Regexp(TEL_REG, message='请输入正确的电话号码'),
                                  ],
                      )
    # 验证码
    sms = StringField(validators=[validators.InputRequired(message="请输入验证码")])

    def validate_sms(self, value):
        tel = self.tel.data
        if value.data != code_database.get(tel):
            raise validators.ValidationError("验证码无效")

    def validate_username(self, value):
        u1 = BuyerUserModel.query.filter_by(username=value.data).first()
        if u1:
            raise validators.ValidationError('该用户名已经被注册了')

    def validate_tel(self, value):
        u1 = BuyerUserModel.query.filter_by(tel=value.data).first()
        if u1:
            raise validators.ValidationError('该电话号码已经被注册了')


class BuyerLoginForm(Form):
    name = StringField(validators=[validators.InputRequired(message="请输入用户名信息"),
                                   validators.Length(min=3, message="用户名不能少于3个字符"),
                                   validators.Length(max=32, message="用户名不能超过32个字符"),
                                   ],
                       )

    password = StringField(validators=[validators.InputRequired(message="请输入密码"),
                                       validators.Length(min=3, message="密码不能少于3个字符"),
                                       validators.Length(max=16, message="密码不能超过16个字符"),
                                       ],
                           )


class BuyerAddressForm(Form):
    provence = StringField(validators=[validators.Length(max=16, message="不能超过8个字符")])
    # 市
    city = StringField(validators=[validators.Length(max=16, message="不能超过16个字符")])
    # 县
    area = StringField(validators=[validators.Length(max=16, message="不能超过16个字符")])
    # 详细地址
    detail_address = StringField(validators=[validators.InputRequired(message="请输入详细地址"),
                                             validators.Length(max=64, message="详细地址不能超过64个字符"),
                                             ],
                                 )
    # 收货人姓名
    name = StringField(validators=[validators.InputRequired(message="请输入收货人姓名"),
                                   validators.Length(max=32, message="收货人姓名不能超过32个字符"),
                                   ],
                       )
    # 收货人电话
    tel = StringField(validators=[validators.InputRequired(message="请输入电话号码"),
                                  validators.Regexp(r'^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18['
                                                    r'0-9])|166|198|199)\d{8}$', message="请输入正确的电话号码"),
                                  ],
                      )