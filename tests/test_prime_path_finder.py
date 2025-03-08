import pytest
from src.prime_path_finder import find_prime_path, is_prime

def test_is_prime():
    # Test prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(101) == True
    
    # Test non-prime numbers
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(100) == False

def test_find_prime_path_basic():
    grid1 = [
        [1, 1, 1],
        [2, 3, 5],
        [7, 8, 9]
    ]
    path = find_prime_path(grid1)
    assert len(path) > 0, "Should find a prime path"
    path_value = int(''.join(str(grid1[x][y]) for x, y in path))
    assert is_prime(path_value), "Path should form a prime number"

def test_find_prime_path_no_solution():
    grid2 = [
        [4, 6, 8],
        [9, 10, 12],
        [14, 16, 18]
    ]
    path = find_prime_path(grid2)
    assert len(path) == 0, "Should return empty path with no prime sequence"

def test_find_prime_path_multiple_solutions():
    grid3 = [
        [1, 1, 2],
        [3, 5, 7],
        [11, 13, 17]
    ]
    path = find_prime_path(grid3)
    assert len(path) > 0, "Should find at least one prime path"
    path_value = int(''.join(str(grid3[x][y]) for x, y in path))
    assert is_prime(path_value), "Path should form a prime number"

def test_find_prime_path_edge_cases():
    # Empty grid
    assert find_prime_path([]) == []
    
    # Single cell grid
    grid_single_cell = [[2]]
    path = find_prime_path(grid_single_cell)
    assert path == [(0, 0)], "Single prime cell should return its coordinate"
    
    # Single cell non-prime grid
    grid_non_prime_cell = [[4]]
    assert find_prime_path(grid_non_prime_cell) == [], "Non-prime single cell should return empty path"

def test_find_prime_path_complex_scenario():
    grid4 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 13],
        [17, 19, 23, 29]
    ]
    path = find_prime_path(grid4)
    assert len(path) > 0, "Should find a prime path in complex grid"
    path_value = int(''.join(str(grid4[x][y]) for x, y in path))
    assert is_prime(path_value), "Path should form a prime number"