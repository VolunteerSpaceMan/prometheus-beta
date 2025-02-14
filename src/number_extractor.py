import re

def extract_numbers_from_string(input_string):
    """
    Extract all numbers from a given string.
    
    Args:
        input_string (str): The string to extract numbers from.
    
    Returns:
        list: A list of numbers (as strings or integers) found in the input string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use regex to find all numbers (including decimals)
    numbers = re.findall(r'-?\d+(?:\.\d+)?', input_string)
    
    # Convert to integers or floats where possible
    converted_numbers = []
    for num in numbers:
        try:
            # Try to convert to int first
            converted_num = int(num)
        except ValueError:
            try:
                # If not an int, try to convert to float
                converted_num = float(num)
            except ValueError:
                # If conversion fails, keep as string
                converted_num = num
        converted_numbers.append(converted_num)
    
    return converted_numbers