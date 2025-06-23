from flask import request, jsonify
from utils.scraper import get_info
from utils.mailer import send_email

def track_product():
    try:
        data = request.get_json()
        print("Received Data:", data)

        url = data.get("url")
        target_price = data.get("target_price")
        email = data.get("email")

        if not url or not target_price or not email:
            return jsonify({ "error": "Missing URL, target price or email" }), 400

        product = get_info(url)
        current_price = int(product["price"].replace("₹", "").replace(",", ""))

        notified = current_price <= int(target_price)

        
        if notified:
            try:
                send_email(email, product["title"], current_price, url)
            except Exception as e:
                print("Error sending email:", e)
                return jsonify({ "error": "Failed to send notification email" }), 500
        return jsonify({
            "title": product["title"],
            "price": current_price,
            "image": product["image"],
            "notified": notified
        }), 200

    except Exception as e:
        print("Error in track_product:", e)
        return jsonify({ "error": "Something went wrong on server" }), 500
    