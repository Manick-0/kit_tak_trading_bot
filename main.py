import os
from flask import Flask, jsonify, request
from bot.trading_bot import TradingBot
from algorithms.mean_reversion import mean_reversion_strategy
from algorithms.momentum import momentum_strategy

app = Flask(__name__)

@app.route('/run_bot', methods=['POST'])
def run_bot():
    # Initialize the trading bot with a set capital
    bot = TradingBot(capital=10000)

    # Load stock price data (you need to provide the data path or adjust how data is loaded)
    data = bot.load_data('/tmp/stock_prices.csv')  # Ensure this path is correct for your environment

    # Execute Mean Reversion Strategy
    portfolio_mean_reversion = bot.execute_strategy(mean_reversion_strategy, data)

    # Execute Momentum Strategy
    portfolio_momentum = bot.execute_strategy(momentum_strategy, data)

    # Create the response body
    response_body = {
        'mean_reversion': portfolio_mean_reversion.tolist(),
        'momentum': portfolio_momentum.tolist()
    }

    # Return the response
    return jsonify(response_body)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
