from stock_api import get_current_price
from database import create_tables, add_to_watchlist, get_watchlist, log_price, get_price_history


def track_watchlist():
    """Fetch and log a current price for every ticker on the watchlist."""
    tickers = get_watchlist()

    if not tickers:
        print("Watchlist is empty. Add a ticker first.")
        return

    for ticker in tickers:
        price = get_current_price(ticker)

        if price is None:
            print(f"{ticker}: could not fetch price")
            continue

        log_price(ticker, price)
        print(f"{ticker}: {price}")


def show_history(ticker):
    """Print all logged prices for a given ticker."""
    history = get_price_history(ticker)

    if not history:
        print(f"No price history for {ticker}.")
        return

    print(f"Price history for {ticker.upper()}:")
    for price, timestamp in history:
        print(f"  {timestamp} — {price}")


if __name__ == "__main__":
    create_tables()

    # Starter watchlist — add more tickers here as you like
    for ticker in ["AAPL", "MSFT", "GOOGL"]:
        add_to_watchlist(ticker)

    print("Tracking watchlist...")
    track_watchlist()

    print()
    show_history("AAPL")