import pytest
from src.palindrome_validator import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_non_palindromes():
    """Test non-palindrome scenarios."""
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False

def test_edge_cases():
    """Test edge cases of palindrome validation."""
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome(" ") == True  # Space-only string is a palindrome
    assert is_palindrome("!@#$") == True  # Only punctuation is technically a palindrome

def test_case_sensitivity():
    """Test case-insensitive palindrome checking."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_mixed_characters():
    """Test palindromes with mixed alphanumeric and punctuation."""
    assert is_palindrome("Do geese see God?") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_unicode_characters():
    """Test palindrome with unicode and special characters."""
    assert is_palindrome("Madam, I'm Adam") == True

def test_different_types():
    """Ensure function handles different input types."""
    with pytest.raises(TypeError):
        is_palindrome(12321)  # Should raise TypeError for non-string input
    with pytest.raises(TypeError):
        is_palindrome(None)  # Should raise TypeError for None input