import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from MPT_using_scipy import MVO,sharpe_ratio
from risk_parity import to_minimise,risk_parity_func,portfolio_var_RC

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "JPM", "V", "SPY"]
data = yf.download(tickers,'2020-01-01','2022-01-01')

close = data['Close']
returns = close.pct_change()
returns = returns.dropna()

N= len(tickers)

def inv_volatility(returns):
    vol = returns.std().values
    inv_vol = 1/vol
    weights = (inv_vol)/inv_vol.sum()
    return weights

def MVO_helper(train_data):
    rf=0.02
    return MVO(train_data.mean(),train_data.cov(),rf)

def risk_par_helper(train_data):
    cov_mat = train_data.cov()
    final_weights = risk_parity_func(cov_mat)
    return final_weights

def backtest(returns, time_window, weights_func):
    port_ret = []
    
    for t in range(time_window,len(returns)):
        train_data = returns.iloc[t-time_window:t]
        weights = weights_func(train_data) 
        today_ret = returns.iloc[t]
        port_ret.append(np.dot(weights,today_ret))
    
    return pd.Series(port_ret,index= returns.index[time_window:])

rf= 0.02
port_returns_invport = backtest(returns,60,inv_volatility)
port_returns_mvo = backtest(returns,60,MVO_helper)
port_returns_riskparity = backtest(returns,60,risk_par_helper)


net_pro_invport = (port_returns_invport+1).cumprod()
net_pro_mvo = (port_returns_mvo+1).cumprod()
net_pro_risk_par = (port_returns_riskparity+1).cumprod()


plt.plot(net_pro_invport,label = 'inv_port')
plt.plot(net_pro_mvo,label='mvo')
plt.plot(net_pro_risk_par,label='risk_parity')
plt.legend()
plt.show()
