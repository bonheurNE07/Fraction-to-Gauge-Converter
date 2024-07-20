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

