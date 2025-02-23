# 8. Write a Python program to count number of node present in a given binary tree using linked list.
# Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to count the number of nodes in a binary tree
def count_nodes(root):
    """
    Recursively counts the number of nodes in a binary tree.
    :param root: The root node of the binary tree.
    :return: The total number of nodes in the tree.
    """
    if root is None:
        return 0  # Base case: empty tree has no nodes
    
    # Recursively count nodes in the left and right subtrees
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    
    # Return the total number of nodes (1 for the current node + left + right)
    return 1 + left_count + right_count

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

    # Count the number of nodes in the binary tree
    node_count = count_nodes(root)
    print(f"The number of nodes in the binary tree is: {node_count}")