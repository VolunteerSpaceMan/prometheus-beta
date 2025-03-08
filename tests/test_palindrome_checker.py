import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces, punctuation, and mixed case."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_edge_cases():
    """Test edge cases for palindrome checking."""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Only whitespace
    assert is_palindrome("!!") == True  # Only punctuation

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("OpenAI") == False

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_mixed_character_palindromes():
    """Test palindromes with mixed alphanumeric characters."""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c3b1a") == False