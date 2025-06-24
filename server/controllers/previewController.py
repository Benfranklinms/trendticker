from flask import request, jsonify
from utils.scraper import get_info

def preview_product():
    try:
        url = request.args.get("url").strip()

        if not url:
            return jsonify({ "error": "Missing URL" }), 400

        product = get_info(url)
        current_price = int(product["price"].replace("₹", "").replace(",", ""))

        return jsonify({
            "title": product["title"],
            "price": current_price,
            "image": product["image"]
        }), 200

    except Exception as e:
        print("Error in preview_product:", e)
        return jsonify({ "error": "Failed to preview product" }), 500