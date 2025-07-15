# 1. IMPORT LIBRARIES
# ------------------------------------------------------------
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm


# 2. DOWNLOAD REAL DATA
# ------------------------------------------------------------
ticker = "AAPL"
df = yf.download(ticker,
                 start="2024-01-01",
                 auto_adjust=True,   # avoid warnings + adjusted prices
                 progress=False)

close_series = df["Close"]          # single Series
s0 = float(close_series.iloc[-1])   # spot price
print(f"Current price of {ticker}: {s0:.2f} USD")

# Annualized historical volatility
log_ret = np.log(close_series).diff().dropna()
sigma = float(log_ret.std(ddof=0) * np.sqrt(252))   # force to float
print(f"Estimated historical volatility: {sigma:.2%}")

 
# 3. OPTION PARAMETERS
# ------------------------------------------------------------
T      = 0.5                     # 6 months
K      = round(s0 * 1.05, 2)     # strike 5% above spot
r      = 0.035                   # 3.5% annual continuous rate
otype  = "call"

print("\nOPTION PARAMETERS")
print(f"  Strike     = {K} USD")
print(f"  Maturity   = {T} years")
print(f"  Type       = {otype}")
print(f"  Risk-free  = {r:.2%}")


# 4. FUNCTIONS
# ------------------------------------------------------------
def _d1_d2(s0, k, t, r, sigma):
    d1 = (np.log(s0/k) + (r + 0.5*sigma**2)*t) / (sigma*np.sqrt(t))
    d2 = d1 - sigma*np.sqrt(t)
    return d1, d2

def bs_price(s0, k, t, r, sigma, option_type="call"):
    d1, d2 = _d1_d2(s0, k, t, r, sigma)
    if option_type == "call":
        return s0*norm.cdf(d1) - k*np.exp(-r*t)*norm.cdf(d2)
    elif option_type == "put":
        return k*np.exp(-r*t)*norm.cdf(-d2) - s0*norm.cdf(-d1)
    raise ValueError("option_type must be 'call' or 'put'")

def mc_european_option(s0, k, t, r, sigma,
                       n_paths=100_000, option_type="call", seed=42):
    rng   = np.random.default_rng(seed)
    z     = rng.standard_normal(n_paths)
    st    = s0 * np.exp((r-0.5*sigma**2)*t + sigma*np.sqrt(t)*z)
    payoff = np.maximum(st-k, 0) if option_type=="call" else np.maximum(k-st, 0)
    return np.exp(-r*t)*payoff.mean(), st

def greeks(s0, k, t, r, sigma, option_type="call"):
    d1, d2 = _d1_d2(s0, k, t, r, sigma)
    sign   = 1 if option_type=="call" else -1
    delta  = sign * norm.cdf(sign*d1)
    gamma  = norm.pdf(d1)/(s0*sigma*np.sqrt(t))
    vega   = s0*norm.pdf(d1)*np.sqrt(t)/100
    theta  = (-s0*norm.pdf(d1)*sigma/(2*np.sqrt(t))
             -sign*r*k*np.exp(-r*t)*norm.cdf(sign*d2))/365
    rho    = sign*k*t*np.exp(-r*t)*norm.cdf(sign*d2)/100
    return dict(delta=delta, gamma=gamma, vega=vega, theta=theta, rho=rho)


# 5. PRICES
# ------------------------------------------------------------
price_bs = bs_price(s0, K, T, r, sigma, otype)
price_mc, st_paths = mc_european_option(s0, K, T, r, sigma,
                                        n_paths=200_000, option_type=otype)

print("\nPRICES")
print(f"  Black‑Scholes : {price_bs:.4f} USD")
print(f"  Monte Carlo   : {price_mc:.4f} USD")

 
# 6. PLOT
# ------------------------------------------------------------
plt.figure(figsize=(8,4))
plt.hist(st_paths, bins=100, density=True, color="skyblue")
plt.axvline(K, color="red", linestyle="--", label=f"Strike = {K}")
plt.title(f"Simulated $S_T$ Distribution ({ticker}, T={T})")
plt.xlabel("Simulated price at maturity")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()


# 7. GREEKS
# ------------------------------------------------------------
print("\nGREEKS")
for name, val in greeks(s0, K, T, r, sigma, otype).items():
    print(f"  {name.capitalize():<6} = {val:>8.4f}")
