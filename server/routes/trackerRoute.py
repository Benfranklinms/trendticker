from flask import Blueprint
from controllers.trackerController import track_product
from controllers.previewController import preview_product

tracker_bp = Blueprint("tracker", __name__)
tracker_bp.route("/", methods=["POST"])(track_product)
tracker_bp.route("/preview", methods=["GET"])(preview_product)  
