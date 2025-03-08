def generate_fibonacci_sequence(n, k):
    """
    Generate a Fibonacci-like sequence with specific constraints.

    Args:
        n (int): Maximum length of the sequence
        k (int): Minimum sum of consecutive numbers

    Returns:
        list: A list of numbers forming the constrained Fibonacci sequence

    Raises:
        ValueError: If n or k is not a positive integer
    """
    # Validate input parameters
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")

    # Initialize the sequence
    sequence = []

    # Handle edge cases for very small sequences
    if n == 1:
        return [k]  # Return minimal valid start
    if n == 2:
        return [1, k] if k > 1 else [1]

    # Start with smallest possible initial values
    a, b = 1, k
    sequence = [a, b]

    # Generate sequence while meeting constraints
    while len(sequence) < n:
        # Calculate next number
        next_num = a + b
        
        # Check if next number would satisfy constraints
        if len(sequence) + 1 > n:
            break

        # Add next number to sequence
        sequence.append(next_num)
        
        # Shift values for next iteration
        a, b = b, next_num

    return sequence