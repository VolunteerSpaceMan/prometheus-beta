import pytest
from src.word_reverser import reverse_words

def test_basic_word_reversal():
    """Test basic word reversal functionality."""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_words():
    """Test reversal of strings with multiple words."""
    assert reverse_words("Python is an amazing language") == "language amazing an is Python"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words("") == ""

def test_single_word():
    """Test handling of a single word."""
    assert reverse_words("Hello") == "Hello"

def test_string_with_extra_spaces():
    """Test handling of strings with extra spaces."""
    assert reverse_words("  Python   is  awesome  ") == "awesome is Python"

def test_input_types():
    """Test that the function handles different input types gracefully."""
    with pytest.raises(AttributeError):
        reverse_words(None)
    with pytest.raises(AttributeError):
        reverse_words(123)