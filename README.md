# Stock Tracker

A command-line tool that fetches live stock prices from Yahoo Finance and logs them to a local SQLite database, so you can track price history over time for a watchlist of tickers.

## Features

- Fetches real-time stock prices using the [yfinance](https://pypi.org/project/yfinance/) library (no API key required)
- Maintains a watchlist of tickers in a local SQLite database
- Logs every price fetch with a timestamp, building up price history
- Handles invalid tickers and network errors gracefully
- Fully unit tested, including mocked API tests (no network calls needed to run the test suite)

## Project Structure
stock-tracker/
├── project.py           # Main entry point — tracks the watchlist and shows history
├── stock_api.py          # Fetches live prices from Yahoo Finance
├── database.py            # All SQLite operations (watchlist + price log)
├── db_setup.py             # One-time script to create the database and tables
├── test_stock_api.py        # Unit tests for stock_api.py (uses mocking)
├── test_database.py          # Unit tests for database.py
├── requirements.txt
└── README.md
## Setup

1. Clone the repository:
```bash
   git clone https://github.com/YOUR-USERNAME/stock-tracker.git
   cd stock-tracker
```

2. Create and activate a virtual environment:
```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Create the database:
```bash
   python3 db_setup.py
```

## Usage

Run the main script to fetch and log prices for the watchlist:

```bash
python3 project.py
```

This fetches a live price for each ticker on the watchlist, logs it, prints the result, and shows AAPL's price history as an example.

### Changing the watchlist

The starter watchlist is defined in `project.py`:

```python
for ticker in ["AAPL", "MSFT", "GOOGL"]:
    add_to_watchlist(ticker)
```

Add or remove tickers here, or call `add_to_watchlist("TICKER")` directly from a Python shell.

### Using the functions directly

These are available from `database.py` and `stock_api.py`:

```python
from stock_api import get_current_price
from database import get_watchlist, get_price_history

get_current_price("AAPL")        # live price for one ticker
get_watchlist()                  # all tracked tickers
get_price_history("AAPL")        # every logged price for a ticker, most recent first
```

## Running Tests

The project uses `pytest`, with the Yahoo Finance API call mocked so tests run instantly with no network dependency, and a separate throwaway database so tests never touch your real data.

```bash
python3 -m pytest -v
```

## What I Learned

This project was built to practice combining a live external API with local SQLite storage in Python, including:
- Structuring reusable functions for API calls and database operations
- Handling bad input and network failures with `try/except`
- Writing unit tests with `pytest`, including mocking external calls with `unittest.mock` and isolating test data with `monkeypatch`

## License

This project is open source and available under the MIT License.