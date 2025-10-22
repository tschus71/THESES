import numpy as np
import matplotlib.pyplot as plt

# Defining parameters
S0 = 100        # initial stock value
mu = 0.2        # drift 
sigma = 0.4     # volatility
T = 3.0         # time to maturity
N = 252         
dt = T / N      # time increment 

# random values for GBM
np.random.seed(42)  
Z = np.random.standard_normal(N)
W = np.cumsum(Z) * np.sqrt(dt)

# GBM formula
t = np.linspace(0, T, N)
S = S0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)

strike_prices = [70, 115, 125]

# Initiate plot
plt.figure(figsize=(12, 6))
plt.plot(t, S, label='GBM Path', color='blue')

# Plot different strike prices as horizontal lines in the graph
for strike in strike_prices:
    plt.axhline(y=strike, color='red', linestyle='--', linewidth=1)
    plt.text(0, strike + 1, f'Strike: {strike}', color='red', fontsize=9)

# Plotting
plt.title('Geometric Brownian Motion with Strike Prices')
plt.xlabel('Time (Years)')
plt.ylabel('Stock Price')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
