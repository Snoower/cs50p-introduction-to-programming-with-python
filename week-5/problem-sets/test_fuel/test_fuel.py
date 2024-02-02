from fuel import convert, gauge
import pytest

def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_percentage():
    assert gauge(65) == "65%"
    assert gauge(45) == "45%"

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert ("0/0")

def test_value_error():
    with pytest.raises(ValueError):
        assert convert("4/3")
