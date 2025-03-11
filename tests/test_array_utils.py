import pytest
from src.array_utils import count_occurrences

def test_count_occurrences_basic():
    """Test basic occurrence counting."""
    assert count_occurrences([1, 2, 3, 2, 2], 2) == 3

def test_count_occurrences_empty_list():
    """Test counting in an empty list."""
    assert count_occurrences([], 5) == 0

def test_count_occurrences_no_match():
    """Test when element is not in the list."""
    assert count_occurrences([1, 2, 3, 4], 5) == 0

def test_count_occurrences_different_types():
    """Test counting with different types of elements."""
    assert count_occurrences(['a', 'b', 'a', 'c'], 'a') == 2
    assert count_occurrences([1, '1', 1, '1'], 1) == 2

def test_count_occurrences_invalid_input():
    """Test error handling for invalid input."""
    with pytest.raises(TypeError):
        count_occurrences("not a list", 1)
    
    with pytest.raises(TypeError):
        count_occurrences(None, 1)
    
    with pytest.raises(TypeError):
        count_occurrences(123, 1)