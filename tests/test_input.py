import pytest

from src.assignment_0_1 import congratulate

def test_congratulations(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Teija")
    result = congratulate()
    assert result == "Congratulations, Teija! You are the best!"
