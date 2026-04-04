import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 1000000        # Maximum audience (1 Million)
S0 = 1000          # Initial subscribers
r = 0.3            # Growth rate

# Time (in months)
t = np.linspace(0, 24, 100)

# Logistic Growth Formula
A = (K - S0) / S0
S = K / (1 + A * np.exp(-r * t))

# Plotting
plt.figure()
plt.plot(t, S)
plt.xlabel("Time (Months)")
plt.ylabel("Number of Subscribers")
plt.title("YouTube Subscriber Growth Prediction")
plt.show()
