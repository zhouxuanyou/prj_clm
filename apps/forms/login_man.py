from flask_login import LoginManager

from apps.models.seller_model import SellerUser

login_manager = LoginManager()


@login_manager.user_loader
def load_user(userid):
    # User.get(userid)
    return SellerUser.query.get(int(userid))
