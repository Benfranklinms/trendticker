from flask import Flask, jsonify
from flask_cors import CORS
from routes.trackerRoute import tracker_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(tracker_bp, url_prefix="/api/track");


@app.route("/")
def Home():
    return jsonify({"message": "Server running"});


if(__name__ == "__main__"):
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)