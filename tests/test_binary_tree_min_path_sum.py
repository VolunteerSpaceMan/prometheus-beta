import pytest
from src.binary_tree_min_path_sum import TreeNode, find_min_path_sum

def test_empty_tree():
    """Test that an empty tree returns infinity."""
    assert find_min_path_sum(None) == float('inf')

def test_single_node_tree():
    """Test a tree with only a root node."""
    root = TreeNode(5)
    assert find_min_path_sum(root) == 5

def test_simple_two_level_tree():
    """Test a simple two-level tree."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    assert find_min_path_sum(root) == 15

def test_unbalanced_tree():
    """Test an unbalanced tree with different path lengths."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    assert find_min_path_sum(root) == 15

def test_complex_tree():
    """Test a more complex tree scenario."""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)
    root.left.left.left = TreeNode(1)
    assert find_min_path_sum(root) == 16  # 10 -> 5 -> 1

def test_negative_values():
    """Test a tree with negative values."""
    root = TreeNode(-10)
    root.left = TreeNode(5)
    root.right = TreeNode(-15)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(4)
    assert find_min_path_sum(root) == -20  # -10 -> -15 -> 4