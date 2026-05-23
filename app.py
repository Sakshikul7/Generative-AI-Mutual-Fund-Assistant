from flask import Flask, request, jsonify
from market_data import get_market_summary
from rag_engine import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return "Generative AI Mutual Fund Assistant Running Successfully!"

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("query")

    market_info = get_market_summary()

    final_response = generate_response(user_query, market_info)

    return jsonify({
        "query": user_query,
        "response": final_response
    })

if __name__ == "__main__":
    app.run(debug=True)
