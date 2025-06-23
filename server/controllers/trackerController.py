from flask import request, jsonify
from utils.scraper import get_info
from models.tracker import save_or_update_product


def track_product():
    data = request.get_json()
    url = data.get("url")
    target_price = int(data.get("target_price"))
    email = data.get("email")
    
    
    product = get_info(url)
    price = int(product["price"].replace("₹", "").replace(",", ""))
    
    send_mail = price <= target_price
    
    
    save_or_update_product({
            "url": url,
            "title": product["title"],
            "price": price,
            "target_price": target_price,
            "email": email,
            "image": product["image"],
            "notified": send_mail
        })
    
    if send_mail:
        pass