import os
from flask import Flask, jsonify, request, send_from_directory
from bot.trading_bot import TradingBot

app = Flask(__name__, static_url_path='')

API_KEY = '5JL6Q7PPEP5CGW77'  # Replace with your actual API key
SYMBOLS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA', 'V', 'JPM']  # List of symbols to analyze

@app.route('/')
def serve_frontend():
    return send_from_directory('', 'index.html')

@app.route('/run_bot', methods=['POST'])
def run_bot():
    try:
        # Initialize the trading bot with a set capital and API key
        bot = TradingBot(capital=10000, api_key=API_KEY)

        # Find top stocks
        top_stocks = bot.find_top_stocks(SYMBOLS)

        # Create the response body
        response_body = {'top_stocks': top_stocks}

        # Return the response
        return jsonify(response_body)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
