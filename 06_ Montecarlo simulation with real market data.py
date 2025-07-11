import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Scarica dati reali di ENI ultimi 6 mesi
eni = yf.download('ENI.MI', period='6mo')

# Prezzo attuale (ultimo prezzo di chiusura disponibile)
S0 = eni['Close'].iloc[-1].item()
print(f"Prezzo attuale ENI = {S0:.2f} €")

# Calcolo rendimenti logaritmici giornalieri
log_returns = np.log(eni['Close'] / eni['Close'].shift(1)).dropna()

# Calcolo volatilità annualizzata (sqrt(252) giorni di borsa)
sigma = float(log_returns.std() * np.sqrt(252))
print(f"Volatilità annuale stimata = {sigma:.2%}")

# Parametri opzione call europea
K = S0 * 1.05      # Strike a 5% sopra il prezzo attuale
T = 1              # 1 anno alla scadenza
r = 0.02           # Tasso risk-free annuo (2%)
n_sims = 100000    # Numero simulazioni Monte Carlo

# Simulazione Monte Carlo dei prezzi finali ST
Z = np.random.standard_normal(n_sims)  # Numeri casuali standard normali
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

# Calcolo payoff call europea max(ST - K, 0)
payoffs = np.maximum(ST - K, 0)

# Prezzo stimato della call come media scontata dei payoff
call_price = np.exp(-r * T) * np.mean(payoffs)
print(f"Prezzo stimato della call europea = {call_price:.2f} €")

# Visualizzazione distribuzione prezzi finali simulati
plt.hist(ST, bins=100, color='blue', alpha=0.7)
plt.axvline(K, linestyle='--', color='red', label='Strike (K)')
plt.title("Distribuzione Prezzi Finali ENI (Monte Carlo)")
plt.xlabel("Prezzo finale (€)")
plt.ylabel("Frequenza")
plt.legend()
plt.show()
