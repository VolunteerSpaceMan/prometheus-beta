def count_occurrences(arr, element):
    """
    Count the number of times a specific element appears in an array.

    Args:
        arr (list): The input array to search through.
        element: The element to count occurrences of.

    Returns:
        int: The number of times the element appears in the array.

    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use list comprehension to count occurrences
    return sum(1 for item in arr if item == element)