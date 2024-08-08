import pandas as pd

def mean_reversion_strategy(prices: pd.DataFrame, window: int = 20):
    rolling_mean = prices['Close'].rolling(window=window).mean()
    signal = (prices['Close'] < rolling_mean).astype(int)
    return signal
