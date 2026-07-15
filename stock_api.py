import yfinance as yf


def get_current_price(ticker):
    """Return the latest closing price for a ticker, or None if it can't be found."""
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="1d")

        if history.empty:
            return None

        latest_close = history["Close"].iloc[-1]
        return round(float(latest_close), 2)

    except Exception:
        return None
    

if __name__ == "__main__":
    price = get_current_price("NOTAREALTICKER")
    print(f"NOTAREALTICKER price: {price}")