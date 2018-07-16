from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 设计所有数据库表的通用结构，每个结构都要设置ID和状态字段
class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, default=1)

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)

from . import seller_model
