from flask import Blueprint


api_bp = Blueprint("api", __name__, url_prefix='/api/v1')

from . import shop_api
from . import buyer_api
