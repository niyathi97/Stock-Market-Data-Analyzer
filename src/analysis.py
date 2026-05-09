import pandas as pd


def analyze_data(df):

    # Daily Returns
    df["Daily Return"] = df["Close"].pct_change()

    # Moving Averages
    df["MA20"] = df["Close"].rolling(window=20).mean()

    df["MA50"] = df["Close"].rolling(window=50).mean()

    # Volatility
    volatility = df["Daily Return"].std()

    # Highest and Lowest Price
    highest_price = df["High"].max()

    lowest_price = df["Low"].min()

    return df, volatility, highest_price, lowest_price