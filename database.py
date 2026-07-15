import sqlite3


DB_NAME = "stock_tracker.db"


def create_tables():
    """Create the watchlist and price_log tables if they don't already exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS watchlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            price REAL NOT NULL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def add_to_watchlist(ticker):
    """Add a ticker to the watchlist. Does nothing if it's already there."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO watchlist (ticker) VALUES (?)", (ticker.upper(),))
        connection.commit()
    except sqlite3.IntegrityError:
        # Ticker already exists in the watchlist — that's fine, just skip it
        pass

    connection.close()


def get_watchlist():
    """Return a list of all tickers currently on the watchlist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT ticker FROM watchlist")
    rows = cursor.fetchall()

    connection.close()
    return [row[0] for row in rows]


def log_price(ticker, price):
    """Save a price reading for a ticker."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO price_log (ticker, price) VALUES (?, ?)",
        (ticker.upper(), price)
    )
    connection.commit()
    connection.close()


def get_price_history(ticker):
    """Return all logged prices for a given ticker, most recent first."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT price, timestamp FROM price_log WHERE ticker = ? ORDER BY timestamp DESC",
        (ticker.upper(),)
    )
    rows = cursor.fetchall()

    connection.close()
    return rows

if __name__ == "__main__":
    add_to_watchlist("AAPL")
    add_to_watchlist("MSFT")
    print("Watchlist:", get_watchlist())

    log_price("AAPL", 195.50)
    print("AAPL history:", get_price_history("AAPL"))