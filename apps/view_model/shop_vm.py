import random


def shop_view_model(shop):
    distance = random.randint(200, 650)
    e_time = distance // 60
    data = {
        "id": shop.id,
        "shop_name": shop.shop_name,
        "shop_img": shop.shop_logo or '/c/static/images/shop-logo.png',
        "shop_rating": shop.shop_rating,
        "brand": shop.is_brand,
        "on_time": shop.is_ontime,
        "fengniao": shop.is_bird,
        "bao": shop.is_bao,
        "piao": shop.is_fp,
        "zhun": shop.is_zun,
        "start_send": shop.start_cost,
        "send_cost": shop.send_cost,
        "distance": distance,
        "estimate_time": e_time,
        "notice": shop.notice,
        "discount": shop.discount,
    }
    return data


# 菜品描述视图模型
def food_detail_view_model(cate):
    food_list = [
        {"goods_id": food.id,
         "goods_name": food.food_name,
         "rating": food.rating,
         "goods_price": float(food.food_price),
         "description": food.description,
         "month_sales": food.month_sales,
         "rating_count": food.rating_count,
         "tips": food.tips,
         "satisfy_count": 0,
         "satisfy_rate": 0,
         "goods_img": food.food_img}
        for food in cate.foods]

    return food_list
