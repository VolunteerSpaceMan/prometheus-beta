import pytest
from src.fibonacci_sequence import generate_fibonacci_sequence

def test_basic_sequence():
    """Test a basic sequence generation."""
    result = generate_fibonacci_sequence(5, 3)
    assert result == [1, 3, 4, 7, 11]
    assert len(result) == 5

def test_small_k():
    """Test sequence generation with a small k value."""
    result = generate_fibonacci_sequence(4, 2)
    assert result == [1, 2, 3, 5]
    assert len(result) == 4

def test_large_k():
    """Test sequence generation with a larger k value."""
    result = generate_fibonacci_sequence(3, 10)
    assert result == [1, 10, 11]
    assert len(result) == 3

def test_n_one():
    """Test when n is 1."""
    result = generate_fibonacci_sequence(1, 5)
    assert result == [5]
    assert len(result) == 1

def test_n_two():
    """Test when n is 2."""
    result = generate_fibonacci_sequence(2, 3)
    assert result == [1, 3]
    assert len(result) == 2

def test_invalid_n():
    """Test invalid n parameter."""
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_sequence(0, 3)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_sequence(-1, 3)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_sequence(1.5, 3)

def test_invalid_k():
    """Test invalid k parameter."""
    with pytest.raises(ValueError, match="k must be a positive integer"):
        generate_fibonacci_sequence(5, 0)
    with pytest.raises(ValueError, match="k must be a positive integer"):
        generate_fibonacci_sequence(5, -1)
    with pytest.raises(ValueError, match="k must be a positive integer"):
        generate_fibonacci_sequence(5, 1.5)

def test_sequence_constraints():
    """Verify that sequence meets sum constraint."""
    def check_sum_constraint(sequence, k):
        for i in range(len(sequence) - 1):
            assert sequence[i] + sequence[i+1] >= k

    result1 = generate_fibonacci_sequence(6, 5)
    check_sum_constraint(result1, 5)

    result2 = generate_fibonacci_sequence(4, 8)
    check_sum_constraint(result2, 8)