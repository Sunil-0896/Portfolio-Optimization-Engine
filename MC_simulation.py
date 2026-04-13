# We will be assuming daily returns are distributed by a Multivariate Normal Distribution
#     R_t ~ MVN(μ, Σ)
#
# Cholesky Decomposition is used to determine Lower Triangular Matrix
#     L ∈ LL' = Σ
#
#     R_t = μ + LZ_t
#     Z_t ~ N(0, I)
#
# Z_t are the samples from a normal distribution
# (I represents the Identity matrix)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf

def get_data(tickers,start,end):
    # data = pdr.get_data_yahoo(tickers,start,end)
    data = yf.download(tickers,start,end)
    close = data['Close']
    return close
    

def MC_simulate(close,initial,no_of_simulations,no_of_days):

    returns = close.pct_change().dropna()
    mean_ret = returns.mean()
    cov_mat = returns.cov()
    # return cov_ret,mean

    weights = np.random.random(len(mean_ret))
    weights = np.divide(weights,np.sum(weights)) # represents the weight of the company, that is how the initial is split and invested among the companies 

    #optimal weights obtained from MPT while trying with different random weights
    # weights = [0.00757418, 0.00049529 ,0.17527062, 0.0575211,  0.06035322, 0.04741318,
    #  0.41410364, 0.01445766, 0.12866263, 0.09414848]

    
    # weihgts obtained from scipy 
#     weights = [0.00000000e+00, 1.17786022e-16, 1.70869029e-01 ,4.61931865e-01,
#  0.00000000e+00, 0.00000000e+00, 3.67199106e-01, 0.00000000e+00,
#  0.00000000e+00, 1.72289533e-16]

    mean_mat = np.full(shape=(no_of_days,len(weights)),fill_value=mean_ret)
    # print(mean_mat)
    mean_mat = mean_mat.T

    portfolio_mat = np.full(shape=(no_of_days,no_of_simulations),fill_value=0.0)

    for i in range(no_of_simulations):
        z = np.random.normal(size=(no_of_days, len(weights))) # z is the random number choosen from a normal distribution,m representing the uncertainity 
        l = np.linalg.cholesky(cov_mat) # the lower trigular matrix, got using cholesky decmpositon

        daily_ret = mean_mat + np.inner(l, z) 
        portfolio_mat[:, i] = np.cumprod(np.inner(weights, daily_ret.T) + 1) * initial
    final_val = portfolio_mat[-1,:]


    plt.figure()
    plt.plot(portfolio_mat)

    plt.figure()
    plt.hist(final_val)
    plt.show()

if __name__ == '__main__':
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "JPM", "V", "SPY"]
    
    # end = dt.datetime.now()
    # start = end - dt.timedelta(days=500)
    start = '2022-01-01'
    end = '2026-01-01'

    close = get_data(tickers,start,end)
    MC_simulate(close,1000,100,100)
    
    