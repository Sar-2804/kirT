import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("YouTube Subscriber Growth Prediction")

# Sidebar inputs
st.sidebar.header("Model Parameters")

K = st.sidebar.number_input("Maximum Audience (K)", value=1000000)
S0 = st.sidebar.number_input("Initial Subscribers (S0)", value=1000)
r = st.sidebar.slider("Growth Rate (r)", 0.01, 1.0, 0.3)

months = st.sidebar.slider("Time (Months)", 1, 60, 24)

# Time array
t = np.linspace(0, months, 100)

# Logistic Growth Formula
A = (K - S0) / S0
S = K / (1 + A * np.exp(-r * t))

# Plot
fig, ax = plt.subplots()
ax.plot(t, S)
ax.set_xlabel("Time (Months)")
ax.set_ylabel("Number of Subscribers")
ax.set_title("YouTube Subscriber Growth Prediction")

# Display plot
st.pyplot(fig)

# Show final value
st.subheader("Final Predicted Subscribers")
st.write(int(S[-1]))
