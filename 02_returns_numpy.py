"""
Exercise 2.1 – Simple and Logarithmic Returns

Objective:
Calculate simple returns and log returns from a given price series.
"""

import numpy as np

# Example price series
prices = np.array([100, 102, 101, 105, 110])

# Simple returns
simple_returns = prices[1:] / prices[:-1] - 1

# Log returns
log_returns = np.log(prices[1:] / prices[:-1])

# Output
print("Simple returns:", simple_returns)
print("Log returns:", log_returns)
