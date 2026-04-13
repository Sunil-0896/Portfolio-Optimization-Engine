# z is distributed along the standard normal, mu is mean, sigma is std

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''z = np.random.normal(size=(n))
# portfolio_ret = np.full(shape=(n,),fill_value=0.0)
portfolio_ret = mean_ret + std_ret*z
# print(portfolio_ret)
initial = 1000
price_day = np.cumprod(portfolio_ret+1)*initial

plt.plot(price_day)
plt.show()'''
# this is for 100 days , single scenerio, for multiple scenerio, use the same code mutiple times


def GBM_(close,initial,no_of_sims,no_of_days):
    # data = pd.read_csv(r'C:\Users\sunil\Desktop\Quant\projects\AAPL_data.csv')
    # data = yf.download(str(stock_name),'2023-01-01','2026-03-01')
    # close = data['Close']
    # close = pd.to_numeric(close,errors='coerce')
    close = close.dropna()
    returns = close.pct_change()
    mean_ret = returns.mean().item()
    std_ret = returns.std().item()

    price_final = np.full(shape=(no_of_days,no_of_sims),fill_value=0.0)
    portfolio_ret = np.full(shape=(no_of_days,no_of_sims),fill_value=0.0)
    z = np.random.normal(size=(no_of_days,no_of_sims))
    dt = 1 #day

    for i in range(no_of_sims):
        portfolio_ret[:,i] = mean_ret*dt + std_ret*z[:,i]*np.sqrt(dt)
        # print(portfolio_ret)
        price_final[:,i] = np.cumprod(portfolio_ret[:,i]+1)*initial
    
    return price_final

if __name__=='__main__':
    # data = yf.download('AAPL','2023-01-01','2026-03-01')
    # data.to_csv('AAPL_data.csv')
    
    # print(std_ret)
    no_of_days = 100 #days
    initial = 1000
    no_of_sims = 100
    price_final = GBM_(initial,no_of_days,no_of_sims)
    plt.plot(price_final)
    plt.show()
