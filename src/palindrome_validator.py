def is_palindrome(input_string: str) -> bool:
    """
    Check if the given string is a palindrome, ignoring spaces, punctuation, and case.

    Args:
        input_string (str): The string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]