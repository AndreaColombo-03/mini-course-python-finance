"""
Exercise 5.1 – Price Chart with Matplotlib

Objective:
Plot a simple time series of prices using a line chart.
"""

import matplotlib.pyplot as plt

# Sample price data
prices = [100, 102, 101, 105, 110]
days = list(range(len(prices)))

# Create the plot
plt.plot(days, prices, marker='o', linestyle='-')
plt.title("Price Series Over Time")
plt.xlabel("Day")
plt.ylabel("Price")
plt.grid(True)
plt.tight_layout()
plt.show()
