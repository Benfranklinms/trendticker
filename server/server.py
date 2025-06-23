from flask import Flask, jsonify
from flask_cors import CORS
from routes.trackerRoute import tracker_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(tracker_bp, url_prefix="/track")

@app.route("/")
def Home():
    return jsonify({"message": "Server running"});


if(__name__ == "__main__"):
    app.run(debug=True)