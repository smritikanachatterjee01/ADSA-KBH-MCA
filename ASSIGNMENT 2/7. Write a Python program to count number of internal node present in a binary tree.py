# 7. Write a Python program to count number of internal node present in a binary tree.
# Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def count_internal_nodes(root):
    if root is None:
        return 0  # Base case: empty tree has no internal nodes
    
    if root.left is None and root.right is None:
        return 0
    
    left_internal = count_internal_nodes(root.left)
    right_internal = count_internal_nodes(root.right)
    
    # Return the total number of internal nodes, including the current node
    return 1 + left_internal + right_internal

# Example usage
if __name__ == "__main__":
    # Constructing a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    internal_count = count_internal_nodes(root)
    print(f"The number of internal nodes in the binary tree is: {internal_count}")