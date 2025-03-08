from typing import List, Tuple
from math import sqrt

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find a continuous path of cells that form a prime number sequence.
    
    Args:
        grid (List[List[int]]): A 2D grid of integers.
    
    Returns:
        List[Tuple[int, int]]: A list of coordinates representing the prime path,
                                or an empty list if no prime path is found.
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(r: int, c: int, current_path: List[Tuple[int, int]], seen: set) -> List[Tuple[int, int]]:
        """
        Depth-first search to find prime number path.
        
        Args:
            r (int): Current row
            c (int): Current column
            current_path (List[Tuple[int, int]]): Current path traversed
            seen (set): Set of visited coordinates
        
        Returns:
            List[Tuple[int, int]]: Longest prime path found
        """
        current_value = grid[r][c]
        path_value = int(''.join(str(grid[x][y]) for x, y in current_path))
        
        # If current path is not a prime, return current path
        if path_value and not is_prime(path_value):
            return current_path
        
        best_path = current_path.copy()
        
        for dx, dy in directions:
            new_r, new_c = r + dx, c + dy
            
            # Check bounds and avoid revisiting
            if (0 <= new_r < rows and 
                0 <= new_c < cols and 
                (new_r, new_c) not in seen):
                
                temp_path = current_path + [(new_r, new_c)]
                temp_seen = seen.copy()
                temp_seen.add((new_r, new_c))
                
                candidate_path = dfs(new_r, new_c, temp_path, temp_seen)
                
                # Update best path if new path is longer and forms a prime
                candidate_value = int(''.join(str(grid[x][y]) for x, y in candidate_path))
                best_value = int(''.join(str(grid[x][y]) for x, y in best_path))
                
                if (len(candidate_path) > len(best_path) and 
                    is_prime(candidate_value)):
                    best_path = candidate_path
        
        return best_path
    
    longest_prime_path = []
    
    for r in range(rows):
        for c in range(cols):
            current_path = dfs(r, c, [(r, c)], {(r, c)})
            path_value = int(''.join(str(grid[x][y]) for x, y in current_path))
            
            if (len(current_path) > len(longest_prime_path) and 
                is_prime(path_value)):
                longest_prime_path = current_path
    
    return longest_prime_path