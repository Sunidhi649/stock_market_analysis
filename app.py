import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Stock Market Analysis App")

ticker = st.text_input("Enter Stock Symbol (e.g. AAPL, MSFT):", "AAPL")
start = st.date_input("Start Date", pd.to_datetime("2022-01-01"))
end = st.date_input("End Date", pd.to_datetime("today"))

if st.button("Run Analysis"):
    df = yf.download(ticker, start=start, end=end)
    st.subheader("Closing Price")
    st.line_chart(df['Close'])
    st.subheader("Daily Returns")
    df['Daily Return'] = df['Close'].pct_change()
    st.line_chart(df['Daily Return'])
    st.write("Mean Daily Return:", df['Daily Return'].mean())
    st.write("Std Dev Daily Return:", df['Daily Return'].std())
