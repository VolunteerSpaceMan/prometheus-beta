def reverse_words(input_string: str) -> str:
    """
    Reverse the order of words in a given string.

    Args:
        input_string (str): The input string to reverse.

    Returns:
        str: A new string with words in reverse order, preserving original word spacing.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Python is awesome  ")
        'awesome is Python'
        >>> reverse_words("")
        ''
    """
    # Explicit type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty input
    if not input_string:
        return ""
    
    # Split the string into words, preserving multiple spaces
    words = input_string.split()
    
    # Reverse the words and join them back together
    return " ".join(words[::-1])