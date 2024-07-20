import pytest
from fraction_module import convert, gauge

def test_convert_value_error():
    """
    Test that convert function raises a ValueError for invalid fractions.
    """
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("3/2")

def test_convert_zero_division_error():
    """
    Test that convert function raises a ZeroDivisionError for a denominator of zero.
    """
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_success():
    """
    Test that convert function returns the correct percentage for valid fractions.
    """
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100

def test_gauge():
    """
    Test that gauge function returns the correct gauge string for given percentages.
    """
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

