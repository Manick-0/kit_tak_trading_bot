import pandas as pd

def momentum_strategy(prices: pd.DataFrame, window: int = 20):
    momentum = prices['Close'] - prices['Close'].shift(window)
    signal = (momentum > 0).astype(int)
    return signal
