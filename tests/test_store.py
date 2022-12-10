import pytest

from src.assignment_1_1 import *

def test_welcome(capsys):
    welcome()
    stdout, stderr = capsys.readouterr()
    assert stdout == "Hello, welcome to the Python store!\n"

def test_ask_product(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "orange")
    result = ask_product(1)
    assert result == "orange"

def test_ask_price(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.66)
    result = ask_price()
    assert result == 0.66

def test_ask_amount(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 10)
    result = ask_amount()
    assert result == 10

def test_count_total():
    price_1 = 0.66
    price_2 = 3.55
    amount_1 = 10
    amount_2 = 2
    result = count_total(amount_1, amount_2, price_1, price_2)
    assert result == 13.7

def test_goodbye(capsys):
    goodbye()
    stdout, stderr = capsys.readouterr()
    assert stdout == "Thank you! Goodbye! See you soon again!\n"