import pytest
from src.prime_numbers import find_primes_to_hundred

def test_find_primes_to_hundred():
    """
    Test the find_primes_to_hundred function.
    
    Validates:
    - Correct number of primes
    - Correct prime numbers
    - First and last primes
    - Order of primes
    """
    # Expected list of primes from 1 to 100
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    
    # Get the primes
    result = find_primes_to_hundred()
    
    # Assertions
    assert len(result) == len(expected_primes), "Number of primes should match expected"
    assert result == expected_primes, "Returned primes should exactly match expected primes"
    
    # Additional checks
    assert result[0] == 2, "First prime should be 2"
    assert result[-1] == 97, "Last prime should be 97"
    
    # Verify all numbers are prime
    for prime in result:
        # A prime number should have exactly two factors
        factors = [i for i in range(1, prime + 1) if prime % i == 0]
        assert len(factors) == 2, f"{prime} should have exactly two factors"
        assert factors == [1, prime], f"{prime} should only be divisible by 1 and itself"

def test_no_negative_or_zero_primes():
    """
    Ensure no negative or zero primes are returned.
    """
    result = find_primes_to_hundred()
    assert all(prime > 1 for prime in result), "All primes should be greater than 1"

def test_result_type():
    """
    Verify the return type is a list.
    """
    result = find_primes_to_hundred()
    assert isinstance(result, list), "Function should return a list"
    assert all(isinstance(prime, int) for prime in result), "All elements should be integers"