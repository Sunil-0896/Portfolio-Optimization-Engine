import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "JPM", "V", "SPY"]
data = yf.download(tickers,'2021-01-01','2026-01-01')

close = data['Close']
# close = close.dropna()
returns = close.pct_change()

returns = returns.dropna()
# mean ret is calcuolated

mean = returns.mean()
# print(expected_ret.shape)

volatility= returns.std().values
# print(volatility)

inv_volatility = 1/volatility
weights = (inv_volatility)/np.sum(inv_volatility)

print(weights)
