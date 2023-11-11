# Import functions to be tested
from project import get_rate, convert


# Functions that test them
# FUN1:
def test_get_rate():
    assert get_rate("USD", "CAD") == 1.36715
    assert get_rate("NAD", "QAR") == 0.196518
    assert get_rate("MUR", "MXN") == 0.396463


# FUN2:
def test_convert():
    assert convert("USD", "CAD", 100) == 136.585
    assert convert("NAD", "QAR", 250) == 49.1295
    assert convert("MUR", "MXN", 500) == 198.2315
