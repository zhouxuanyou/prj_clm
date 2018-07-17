from apps.models.base import BaseModel, db
from werkzeug.security import generate_password_hash


# 商家的用户信息表
class SellerUser(BaseModel):
    username = db.Column(db.String(32), unique=True, nullable=False)
    _password = db.Column("password", db.String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, arg):
        self._password = generate_password_hash(arg)

    def __repr__(self):
        return "<User {}>".format(self.username)
