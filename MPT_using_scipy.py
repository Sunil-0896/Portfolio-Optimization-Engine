import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def sharpe_ratio(weights,mean,cov_mat,rf):
    expected_mean = np.matmul(weights.T,mean)
    expected_risk = np.sqrt(np.matmul(weights.T,np.matmul(cov_mat,weights)))

    return -(expected_mean - rf)/expected_risk

def MVO(mean,cov_mat,risk_free):
    bounds = tuple((0,1) for i in range(len(cov_mat)))
    constraints = ({'type':'eq','fun':lambda w: np.sum(w)-1})
    initial_guess = np.ones(len(cov_mat))/len(cov_mat)

    optimisation = minimize(sharpe_ratio,initial_guess,args=(mean,cov_mat,risk_free),bounds=bounds,constraints=constraints,method='SLSQP')

    return optimisation.x

if __name__ == '__main__':
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "JPM", "V", "SPY"]
    data = yf.download(tickers,'2021-01-01','2026-01-01')

    close = data['Close']
    # close = close.dropna()
    returns = close.pct_change()

    returns = returns.dropna()
    mean = returns.mean()*252
    # print(expected_ret.shape)

    cov_mat = returns.cov()*252
    # print(cov_mat)
    rf=0.02
    n = len(tickers)

    optimised_weights = MVO(mean,cov_mat,rf,n)


    


