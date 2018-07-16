import os

DEBUG = True

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
db_name = os.path.join(base_dir, 'clm.db')

SQLALCHEMY_DATABASE_URI = r'sqlite:///{}'.format(db_name)
SQLALCHEMY_TRACK_MODIFICATIONS = True
