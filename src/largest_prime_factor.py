def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        int: The largest prime factor of the input number.

    Raises:
        ValueError: If the input is less than or equal to 1.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 1:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Initialize the largest prime factor
    largest_prime_factor = 1
    
    # First, handle even numbers
    while n % 2 == 0:
        largest_prime_factor = 2
        n = n // 2
    
    # Now check for odd factors
    factor = 3
    while factor * factor <= n:
        # If factor divides n, it's a prime factor
        while n % factor == 0:
            largest_prime_factor = factor
            n = n // factor
        
        # Move to next odd number
        factor += 2
    
    # If n is still greater than 2, it is the largest prime factor
    if n > 2:
        largest_prime_factor = n
    
    return largest_prime_factor