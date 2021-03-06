import os

DEBUG = True

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
db_name = os.path.join(base_dir, 'clm.db')

SQLALCHEMY_DATABASE_URI = r'sqlite:///{}'.format(db_name)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 如果使用session，就必须配置秘钥
SECRET_KEY = '$clm!'

EXPIRES_TIME = 7 * 24 * 3600
