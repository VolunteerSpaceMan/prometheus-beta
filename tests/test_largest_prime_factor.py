import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_prime_number():
    """Test that a prime number returns itself as the largest prime factor."""
    assert find_largest_prime_factor(17) == 17

def test_composite_number():
    """Test a composite number with multiple prime factors."""
    assert find_largest_prime_factor(84) == 7

def test_large_number():
    """Test a larger number with multiple prime factors."""
    assert find_largest_prime_factor(13195) == 29

def test_very_large_number():
    """Test a very large number to ensure efficiency."""
    assert find_largest_prime_factor(600851475143) == 6857

def test_smallest_valid_input():
    """Test the smallest valid input."""
    assert find_largest_prime_factor(2) == 2

def test_invalid_input_less_than_two():
    """Test that ValueError is raised for inputs less than 2."""
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(-5)

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor(None)