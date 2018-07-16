from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms import validators


# 商家注册数据验证类
class SellerRegisterForm(Form):
    username = StringField(label="用户名",
                           validators=[validators.InputRequired(message="请填写用户名"),
                                       validators.Length(min=3, message="不少于3字符"),
                                       validators.Length(max=32, message='不能多于32字符'),
                                       ]
                           )
    password1 = PasswordField(label="输入密码",
                              validators=[validators.InputRequired(message="请填写密码"),
                                          validators.Length(min=3, message="不少于3字符"),
                                          validators.Length(max=32, message='不能多于32字符'),
                                          ]
                              )
    password2 = PasswordField(label="确认密码",
                              validators=[validators.InputRequired(message="请填写密码"),
                                          validators.EqualTo('password1', message='密码要保持一致'),
                                          ]
                              )
