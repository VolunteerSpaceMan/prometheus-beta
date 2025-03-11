def find_primes_to_hundred():
    """
    Return a list of all prime numbers between 1 and 100 (inclusive).
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Returns:
        list: A sorted list of prime numbers from 1 to 100.
    """
    # Using the Sieve of Eratosthenes algorithm for efficient prime finding
    # Initialize the sieve
    sieve = [True] * 101
    sieve[0] = sieve[1] = False
    
    # Mark non-prime numbers
    for i in range(2, int(100**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, 101, i):
                sieve[j] = False
    
    # Collect prime numbers
    return [num for num in range(2, 101) if sieve[num]]