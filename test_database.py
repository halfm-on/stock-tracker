import os
import pytest
import database


@pytest.fixture(autouse=True)
def use_test_db(monkeypatch):
    """Point database.py at a throwaway test database for every test in this file."""
    monkeypatch.setattr(database, "DB_NAME", "test_stock_tracker.db")
    database.create_tables()
    yield
    if os.path.exists("test_stock_tracker.db"):
        os.remove("test_stock_tracker.db")


def test_add_and_get_watchlist():
    database.add_to_watchlist("aapl")
    database.add_to_watchlist("msft")

    watchlist = database.get_watchlist()

    assert "AAPL" in watchlist
    assert "MSFT" in watchlist


def test_add_to_watchlist_no_duplicates():
    database.add_to_watchlist("AAPL")
    database.add_to_watchlist("AAPL")

    watchlist = database.get_watchlist()

    assert watchlist.count("AAPL") == 1


def test_log_price_and_get_history():
    database.log_price("AAPL", 150.25)
    database.log_price("AAPL", 151.00)

    history = database.get_price_history("AAPL")

    assert len(history) == 2
    prices = [price for price, timestamp in history]
    assert 150.25 in prices
    assert 151.00 in prices