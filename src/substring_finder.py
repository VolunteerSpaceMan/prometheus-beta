def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two given strings.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        str: The longest common substring. If no common substring exists, 
             returns an empty string.

    Time Complexity: O(m*n), where m and n are lengths of str1 and str2
    Space Complexity: O(m*n)

    Examples:
        >>> longest_common_substring("hello", "help")
        'hel'
        >>> longest_common_substring("", "test")
        ''
        >>> longest_common_substring("abcde", "cde")
        'cde'
    """
    # Handle edge cases
    if not str1 or not str2:
        return ""

    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0

    # Fill the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Exact character match (case-sensitive)
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update longest substring if current is longer
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1

    # Extract the longest common substring
    # Prioritize the first occurrence of the longest substring
    if max_length > 0:
        # Find the first occurrence in str1
        candidates = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if dp[i][j] == max_length and str1[i-max_length:i] == str2[j-max_length:j]:
                    candidates.append(str1[i-max_length:i])
        
        # Return the lexicographically smallest (or first) substring
        return min(candidates) if candidates else ""
    
    return ""