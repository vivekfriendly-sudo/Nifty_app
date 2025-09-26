# streamlit_app.py

import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Nifty_Stocks.csv")
df.Date = pd.to_datetime(df.Date)

# Page title
st.title("📈 Nifty Stocks Explorer")

# Sidebar for category selection
categories = df['Category'].unique()
selected_category = st.sidebar.selectbox("Select Category", sorted(categories))

# Filter based on selected category
filtered_by_category = df[df['Category'] == selected_category]

# Sidebar for symbol selection
symbols = filtered_by_category['Symbol'].unique()
selected_symbol = st.sidebar.selectbox("Select Symbol", sorted(symbols))

# Filter based on selected symbol
final_data = filtered_by_category[filtered_by_category['Symbol'] == selected_symbol]

# Plotting
st.subheader(f"Closing Price of {selected_symbol} Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=final_data, x='Date', y='Close', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
