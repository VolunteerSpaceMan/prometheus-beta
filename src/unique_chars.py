def extract_unique_chars(number_string: str) -> str:
    """
    Extract unique characters from a string of numbers using a custom approach.
    
    Args:
        number_string (str): Input string of numbers
    
    Returns:
        str: String containing only unique characters in the order of first appearance
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input contains non-numeric characters
    """
    # Input validation
    if not isinstance(number_string, str):
        raise TypeError("Input must be a string")
    
    # Validate that input contains only numeric characters
    if not all(char.isdigit() for char in number_string):
        raise ValueError("Input must contain only numeric characters")
    
    # Custom unique character extraction without using built-in methods or sets
    unique_chars = []
    for char in number_string:
        # Check if character is already in unique_chars
        is_unique = True
        for existing_char in unique_chars:
            if char == existing_char:
                is_unique = False
                break
        
        # Add to unique_chars if not already present
        if is_unique:
            unique_chars.append(char)
    
    # Convert unique characters back to string
    return ''.join(unique_chars)