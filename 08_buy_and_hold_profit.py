import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "AAPL" 
initial_capital = 1000

# Download historical data
data = yf.download(ticker, start="2020-01-01", end="2025-01-01")

# Extract the first and last closing prices
purchase_price = float(data['Close'][ticker].iloc[0])
selling_price = float(data['Close'][ticker].iloc[-1])

# Calculate shares, final capital, and profit
number_of_shares = initial_capital / purchase_price
final_capital = number_of_shares * selling_price

profit = final_capital - initial_capital

# Print the results
print(f"Purchase price is : {purchase_price:.2f} $")
print(f"Selling price is : {selling_price:.2f} $")
print(f"Number of shares purchased : {number_of_shares:.2f}")
print(f"Profit : {profit:.2f} $")

# Plot the price chart
plt.plot(data['Close'][ticker])
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"Prices {ticker}")
plt.grid(True)
plt.show()
