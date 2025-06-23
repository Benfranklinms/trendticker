from flask import Flask, jsonify
from utils.Scraper import get_info


app = Flask(__name__)

@app.route("/")
def Home():
    return jsonify(get_info());


if(__name__ == "__main__"):
    app.run(debug=True)