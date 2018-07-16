from apps.cms import cms_bp


# 创建首页
@cms_bp.route('/', endpoint='index')
def seller_index():
    return "success"


# 创建注册页面
@cms_bp.route('/register/', endpoint='register', methods=['GET', 'POST'])
def seller_register():
    return "1-success"
