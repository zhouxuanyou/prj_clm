from apps.models.base import BaseModel, db


# 商家的用户信息表
class SellerUser(BaseModel):
    username = db.Column(db.String(32), unique=True, nullable=False)
    _password = db.Column("password", db.String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, arg):
        self._password = arg

    def __repr__(self):
        return "<User {}>".format(self.username)
