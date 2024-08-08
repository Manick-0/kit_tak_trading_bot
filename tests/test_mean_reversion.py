import pandas as pd
from algorithms.mean_reversion import mean_reversion_strategy

def test_mean_reversion_strategy():
    data = pd.DataFrame({
        'Close': [10, 11, 12, 11, 10, 9, 8, 9, 10, 11, 12, 11, 10]
    })
    signal = mean_reversion_strategy(data, window=3)
    expected_signal = pd.Series([0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1], name='Close')  # Updated expected signal with name attribute
    pd.testing.assert_series_equal(signal, expected_signal)
