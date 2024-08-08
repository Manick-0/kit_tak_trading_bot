import pandas as pd

def backtest(prices: pd.DataFrame, signal: pd.Series, initial_capital: float = 10000):
    positions = signal.diff().fillna(0)
    returns = prices['Close'].pct_change()
    portfolio = initial_capital * (1 + (returns * positions).cumsum())
    return portfolio
