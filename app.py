from flask import Flask, jsonify, request
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "text": "Stay hungry, stay foolish."},
    {"id": 2, "text": "Code is like humor. When you have to explain it, it’s bad."}
]

@app.route("/")
def home():
    return "Welcome to the Quote API!"

@app.route("/quotes", methods=["GET"])
def get_quotes():
    return jsonify(quotes)

@app.route("/quotes/random", methods=["GET"])
def random_quote():
    return jsonify(random.choice(quotes))

@app.route("/quotes", methods=["POST"])
def add_quote():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_quote = {
        "id": len(quotes) + 1,
        "text": data["text"]
    }

    quotes.append(new_quote)
    return jsonify(new_quote), 201

if __name__ == "__main__":
    app.run(debug=True)