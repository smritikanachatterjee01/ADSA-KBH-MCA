# 4. Write a Python program to identify the height of a binary tree.
# Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to calculate the height of a binary tree
def tree_height(root):
    """
    Recursively calculates the height of a binary tree.
    :param root: The root node of the binary tree.
    :return: The height of the binary tree.
    """
    if root is None:
        return -1  # Height of an empty tree is -1 (no edges)
    
    # Recursively calculate the height of the left and right subtrees
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    # Return the maximum height of the two subtrees plus 1 (for the current level)
    return max(left_height, right_height) + 1

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

    # Calculate the height of the binary tree
    height = tree_height(root)
    print(f"The height of the binary tree is: {height}")