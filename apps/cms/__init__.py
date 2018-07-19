from flask import Blueprint

cms_bp = Blueprint('cms', __name__, url_prefix='/cms')

# 导入蓝图管理的URL
from . import auth_view
from . import shop_view

