# Portfolio-Optimization-Engine

# Quantitative Portfolio Construction and Monte Carlo Risk Simulation

## Overview

This project focuses on building a **systematic portfolio construction and forward risk simulation framework** using quantitative methods. It combines classical portfolio optimization techniques with stochastic modeling to analyze the behavior of portfolios under uncertainty.

The objective is to simulate realistic market dynamics and evaluate how different portfolio construction strategies perform in a forward-looking setting in a 1000 different ways.

---

## Features

### Portfolio Construction Strategies

The project implements multiple quantitative portfolio allocation methods:

* **Mean-Variance Optimization (MVO)**
  Maximizes the Sharpe ratio.

* **Risk Parity**
  Allocates weights such that risk contribution by each asset is equal.

* **Inverse Volatility Portfolio**
  Assigns weights inversely proportional to the asset's volatility.

---

### Correlated Asset Modeling

* Uses empirical covariance matrices derived from historical data (around 3-4 yrs in the past)
* Applies **Cholesky decomposition** to generate correlated random variables

---

### Monte Carlo Simulation

* Simulates 1000 different future portfolio paths using a **Geometric Brownian Motion (GBM)-consistent framework**
* Incorporates:
  * Drift and volatility estimates tsken from the historical data
  * Correlation structure between assets
* Generates multiple simulated paths to study distribution of outcomes

---

## Methodology

1. **Data Collection**
   Historical price data is fetched using financial APIs and converted into return series.

2. **Portfolio Optimization**
   Different allocation strategies (MVO, Risk Parity, Inverse Volatility) are backtested first.

3. **Statistical Modeling**

   * Mean returns and covariance matrix estimated
   * Correlated shocks generated via Cholesky decomposition

4. **Simulation Engine**

   * Future return paths generated using GBM-consistent dynamics
   * Portfolio value simulated over time

---

## Project Status 🚧

This project is **currently in progress**.

* Individual components such as:
  * Portfolio optimization
  * Correlated asset simulation
  * Monte Carlo engine
    are implemented and functional.

* The **final integration between optimal strategy selection and Monte Carlo simulation** is currently under development.

Future updates will include:
* Portfolio for multiple assets
* Regime-based strategy selection
* Integrated pipeline for end-to-end simulation
* Enhanced risk analysis metrics

Code : 
  backtest_code.py takes in functions defined in MPT,inverse_volatility,risk_parity and tests the effectiveness of each stratergy, while the widget.py has the code for the framework, cuurently runs the GBM.py file, will be updated to multiple assets like in the MC_simulation.py

---

## Tech Stack

* **Python**
* NumPy
* pandas
* SciPy
* Matplotlib
* yfinance
* PyQt6 (Qt Designer)

---

## Key Concepts Used

* Mean-Variance Optimization
* Risk Parity
* Volatility Scaling
* Monte Carlo Simulation
* Geometric Brownian Motion
* Cholesky Decomposition
* Multivariate Normal Sampling

---

## Motivation

This project is aimed at understanding how **different portfolio construction techniques behave under uncertainty**, and how stochastic modeling can be used to estimate the weights accordingly and give out the best possible forward-looking setting.


---

## Disclaimer

This project is for educational and research purposes only and does not constitute financial advice.

---
