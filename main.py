import pandas as pd
import streamlit as st

from src.fetch_data import fetch_stock_data
from src.analysis import analyze_data
from src.visualization import create_charts
from src.visualization import create_return_chart


st.set_page_config(page_title="Stock Market Data Analyzer", layout="wide")

st.title("📈 Stock Market Data Analyzer")


# User Inputs
ticker = st.text_input("Enter Stock Ticker", "AAPL")

start_date = st.date_input("Start Date")

end_date = st.date_input("End Date")


# Analyze Button
if st.button("Analyze Stock"):

    # Fetch Data
    stock_data = fetch_stock_data(
        ticker,
        start_date,
        end_date
    )

    # Save Raw Data
    stock_data.to_csv("data/stock_data.csv")

    # Analysis
    analyzed_data, volatility, highest_price, lowest_price = analyze_data(stock_data)

    # Create Charts
    create_charts(analyzed_data, ticker)

    create_return_chart(analyzed_data)

    # Display Data
    st.subheader("📊 Stock Data")

    st.dataframe(analyzed_data.tail())

    # Display Metrics
    st.subheader("📌 Analysis Summary")

    st.write(f"Volatility: {volatility}")

    st.write(f"Highest Price: {highest_price}")

    st.write(f"Lowest Price: {lowest_price}")

    # Show Charts
    st.subheader("📉 Stock Price Chart")

    st.image("outputs/stock_chart.png")

    st.subheader("📉 Daily Returns Chart")

    st.image("outputs/daily_returns.png")

    # Save Report
    analyzed_data.to_csv("outputs/final_report.csv")

    st.success("Stock Analysis Completed!")

    st.success("Report Saved in outputs folder")