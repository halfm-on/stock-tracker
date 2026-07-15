from unittest.mock import patch, MagicMock
import pandas as pd
from stock_api import get_current_price


def test_get_current_price_success():
    fake_history = pd.DataFrame({"Close": [100.0, 101.0, 102.5]})

    with patch("stock_api.yf.Ticker") as mock_ticker:
        mock_ticker.return_value.history.return_value = fake_history
        price = get_current_price("AAPL")

    assert price == 102.5


def test_get_current_price_empty_history():
    with patch("stock_api.yf.Ticker") as mock_ticker:
        mock_ticker.return_value.history.return_value = pd.DataFrame()
        price = get_current_price("FAKETICKER")

    assert price is None


def test_get_current_price_raises_exception():
    with patch("stock_api.yf.Ticker") as mock_ticker:
        mock_ticker.side_effect = Exception("network error")
        price = get_current_price("AAPL")

    assert price is None