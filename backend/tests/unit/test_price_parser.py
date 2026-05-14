import pytest
from app.core.price_parser import parse_price, extract_currency

def test_parse_price_usd():
    assert parse_price("$19.99") == 19.99
    assert parse_price("$1,299.99") == 1299.99

def test_parse_price_eur():
    assert parse_price("€49,99") == 49.99
    assert parse_price("€1.299,99") == 1299.99

def test_parse_price_inr():
    assert parse_price("₹1,999") == 1999.0

def test_parse_price_invalid():
    assert parse_price("") is None
    assert parse_price("N/A") is None

def test_extract_currency():
    assert extract_currency("$19.99") == "USD"
    assert extract_currency("€49.99") == "EUR"
    assert extract_currency("£29.99") == "GBP"
    assert extract_currency("₹1999") == "INR"
