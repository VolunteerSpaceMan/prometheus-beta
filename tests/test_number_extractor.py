import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.number_extractor import extract_numbers_from_string

def test_extract_numbers_basic():
    assert extract_numbers_from_string("hello 123 world") == [123]
    assert extract_numbers_from_string("42 is the answer") == [42]

def test_extract_numbers_multiple():
    assert extract_numbers_from_string("I have 3 apples and 5 oranges") == [3, 5]

def test_extract_numbers_with_decimals():
    assert extract_numbers_from_string("Price: $10.99 and $5.50") == [10.99, 5.50]

def test_extract_numbers_with_negative():
    assert extract_numbers_from_string("Temperature: -5 and 20 degrees") == [-5, 20]

def test_extract_numbers_mixed_types():
    result = extract_numbers_from_string("Mixed: 42, 3.14, -7")
    assert result == [42, 3.14, -7]

def test_no_numbers():
    assert extract_numbers_from_string("No numbers here") == []

def test_invalid_input():
    with pytest.raises(TypeError):
        extract_numbers_from_string(123)
    with pytest.raises(TypeError):
        extract_numbers_from_string(None)