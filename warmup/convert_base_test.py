from warmup import convert_base
import pytest

@pytest.mark.parametrize("input,expected", [
    ("0", "0"),
    ("1", "1"),
    ("10", "2"),
    ("11", "3"),
    ("100", "4"),
    ("101", "5"),
    ("1001101", "77"),
    ("1011001", "89")
])
def test_binary_to_decimal(input, expected):
    assert convert_base.binary_to_decimal(input) == expected

@pytest.mark.parametrize("input,expected", [
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("9", "9"),
    ("A", "10"),
    ("B", "11"),
    ("F", "15"),
    ("4D72B", "317227"),
    ("C519F3", "12917235")
])
def test_hexadecimal_to_decimal(input, expected):
    assert convert_base.hexadecimal_to_decimal(input) == expected

@pytest.mark.parametrize("input,expected", [
    ("0", "0"),
    ("1", "1"),
    ("2", "10"),
    ("3", "11"),
    ("4", "100"),
    ("5", "101"),
    ("77", "1001101"),
    ("89", "1011001"),
    ("11639", "10110101110111")
])
def test_decimal_to_binary(input, expected):
    assert convert_base.decimal_to_binary(input) == expected

@pytest.mark.parametrize("input,expected", [
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("10", "A"),
    ("11", "B"),
    ("15", "F"),
    ("317227", "4D72B"),
    ("12917235", "C519F3")
])
def test_decimal_to_hexadecimal(input, expected):
    assert convert_base.decimal_to_hexadecimal(input) == expected

@pytest.mark.parametrize("input,expected", [
    ("0", "0"),
    ("1", "1"),
    ("10", "2"),
    ("101", "5"),
    ("101011", "2B"),
    ("11100", "1C"),
    ("10101110", "AE"),
    ("11110101110111", "3D77")
])
def test_binary_to_hexadecimal(input, expected):
    assert convert_base.binary_to_hexadecimal(input) == expected

@pytest.mark.parametrize("input,expected", [
    ("0", "0"),
    ("1", "1"),
    ("2", "10"),
    ("5", "101"),
    ("2B", "101011"),
    ("1C", "11100"),
    ("AE", "10101110"),
    ("3D77", "11110101110111")
])
def test_hexadecimal_to_binary(input, expected):
    assert convert_base.hexadecimal_to_binary(input) == expected