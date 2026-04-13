# each RC shoudl be equal, and hence equal to (sigmap**2)/N
# minimise the func (RC - (sigmap**2)/N)**2, like in the case of least sqaure fit

import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize

def portfolio_var_RC(weights,cov_mat):
        sigma_p = np.matmul(weights.T,np.matmul(cov_mat, weights))
        RC = weights*(np.matmul(cov_mat,weights))
        return sigma_p,RC

def to_minimise(weights,cov_mat):
    N = len(cov_mat)
    sigma_p,RC = portfolio_var_RC(weights,cov_mat)
    target = sigma_p/N
    return ((RC/target - 1)**2).sum()

def risk_parity_func(cov_mat):
    N = len(cov_mat)
    constraints = {'type':'eq','fun':lambda w :sum(w)-1}
    bounds = [(0,1) for i in range(N)]
    initial_guess = np.ones(N)/N

    final_weights = minimize(to_minimise,initial_guess,args=(cov_mat.values),method='SLSQP',bounds=bounds,constraints=constraints)
    return final_weights.x

if __name__ == '__main__':

    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "JPM", "V", "SPY"]
    data = yf.download(tickers,'2021-01-01','2026-01-01')

    close = data['Close']
    returns = close.pct_change()
    returns = returns.dropna()
    cov_mat= returns.cov()

    N= len(tickers)

    final_weights = risk_parity_func(cov_mat)
    # print(final_weights.success)
    # print(final_weights.message)
    print(final_weights)
