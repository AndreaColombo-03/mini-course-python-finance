"""
Exercise 3.1 – CAPM Regression

Objective:
Estimate beta, alpha, and R² between an asset and the market using linear regression.
"""

from scipy.stats import linregress

# Example asset and market returns
r_asset = [0.01, 0.02, 0.015, 0.017, 0.016]
r_market = [0.012, 0.021, 0.011, 0.018, 0.019]

# Perform linear regression
result = linregress(r_market, r_asset)

# Output
print(f"Beta (slope): {result.slope:.4f}")
print(f"Alpha (intercept): {result.intercept:.4f}")
print(f"R-squared: {result.rvalue**2:.4f}")
