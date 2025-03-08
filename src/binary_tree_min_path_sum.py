class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        val (int): The value stored in the node.
        left (TreeNode, optional): Left child node. Defaults to None.
        right (TreeNode, optional): Right child node. Defaults to None.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_min_path_sum(root):
    """
    Find the minimum path sum from the root to any leaf in a binary tree.
    
    Args:
        root (TreeNode): The root of the binary tree.
    
    Returns:
        int: The minimum path sum. Returns float('inf') if the tree is empty.
    
    Raises:
        TypeError: If the input is not a TreeNode or None.
    
    Time Complexity: O(n), where n is the number of nodes in the tree
    Space Complexity: O(h), where h is the height of the tree (due to recursion)
    """
    # Check for invalid input
    if root is None:
        return float('inf')
    
    # If it's a leaf node, return its value
    if root.left is None and root.right is None:
        return root.val
    
    # Recursively find minimum path sum to a leaf in left and right subtrees
    # If a side is None, use infinity to ensure the other side is chosen
    left_min = (find_min_path_sum(root.left) if root.left else float('inf'))
    right_min = (find_min_path_sum(root.right) if root.right else float('inf'))
    
    # Return the node's value plus the minimum path sum to a leaf
    return root.val + min(left_min, right_min)