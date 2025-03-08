import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    """Test basic functionality of unique character extraction"""
    assert extract_unique_chars("111223") == "123"
    assert extract_unique_chars("123456") == "123456"
    assert extract_unique_chars("654321") == "654321"

def test_extract_unique_chars_preserve_order():
    """Ensure unique characters are extracted in order of first appearance"""
    assert extract_unique_chars("213121") == "213"

def test_extract_unique_chars_empty_string():
    """Handle empty string input"""
    assert extract_unique_chars("") == ""

def test_extract_unique_chars_all_same_digits():
    """Handle input with all same digits"""
    assert extract_unique_chars("1111") == "1"
    assert extract_unique_chars("0000") == "0"

def test_extract_unique_chars_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        extract_unique_chars(123)
    
    with pytest.raises(TypeError):
        extract_unique_chars(None)
    
    with pytest.raises(TypeError):
        extract_unique_chars(["1", "2", "3"])

def test_extract_unique_chars_non_numeric_input():
    """Test error handling for non-numeric characters"""
    with pytest.raises(ValueError):
        extract_unique_chars("12a34")
    
    with pytest.raises(ValueError):
        extract_unique_chars("123 456")
    
    with pytest.raises(ValueError):
        extract_unique_chars("12.34")