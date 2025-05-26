from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ MarketBidder API is live!"

@app.route('/api/rfqs')
def get_rfqs():
    return jsonify([])
