from flask import Flask, request, jsonify
from recommender import recommend
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def get_recommendations():
    data = request.get_json()
    title = data.get("title")
    if not title:
        return jsonify({"error": "No title provided"}), 400

    try:
        recs = recommend(title)
        return jsonify({"recommendations": recs})
    except:
        return jsonify({"error": "Movie not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
