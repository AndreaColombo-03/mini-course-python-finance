"""
Exercise 4.1 – Portfolio Variance

Objective:
Calculate the variance of a portfolio made up of two assets using:
Var_p = w.T * Cov * w
"""

import numpy as np

# Expected returns (not used here, but often part of the model)
mu = np.array([0.1, 0.12])

# Covariance matrix
cov_matrix = np.array([
    [0.005, 0.001],
    [0.001, 0.006]
])

# Asset weights in the portfolio
weights = np.array([0.4, 0.6])

# Portfolio variance calculation
portfolio_variance = weights.T @ cov_matrix @ weights

# Output
print(f"Portfolio variance: {portfolio_variance:.6f}")

