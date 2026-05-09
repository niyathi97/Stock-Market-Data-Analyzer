import matplotlib.pyplot as plt


def create_charts(df, ticker):

    # Closing Price Chart
    plt.figure(figsize=(12, 6))

    plt.plot(df["Close"], label="Closing Price")

    plt.plot(df["MA20"], label="MA20")

    plt.plot(df["MA50"], label="MA50")

    plt.title(f"{ticker} Stock Price Analysis")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    plt.savefig("outputs/stock_chart.png")

    plt.close()


def create_return_chart(df):

    plt.figure(figsize=(12, 6))

    plt.plot(df["Daily Return"])

    plt.title("Daily Returns")

    plt.xlabel("Date")

    plt.ylabel("Return")

    plt.savefig("outputs/daily_returns.png")

    plt.close()