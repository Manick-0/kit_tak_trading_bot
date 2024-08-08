import requests
import pandas as pd
from algorithms.mean_reversion import mean_reversion_strategy
from algorithms.momentum import momentum_strategy

class TradingBot:
    def __init__(self, capital: float, api_key: str):
        self.capital = capital
        self.api_key = api_key

    def fetch_data(self, symbol: str) -> pd.DataFrame:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={self.api_key}&outputsize=compact'
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index', dtype=float)
        df = df.rename(columns={
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        })
        df.index = pd.to_datetime(df.index)
        return df

    def execute_strategy(self, strategy, data: pd.DataFrame):
        signal = strategy(data)
        portfolio = backtest(data, signal, self.capital)
        return portfolio

    def find_top_stocks(self, symbols: list) -> list:
        results = []
        for symbol in symbols:
            data = self.fetch_data(symbol)
            mean_reversion_score = self.execute_strategy(mean_reversion_strategy, data)['final_value']
            momentum_score = self.execute_strategy(momentum_strategy, data)['final_value']
            total_score = mean_reversion_score + momentum_score
            results.append((symbol, total_score))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:10]
