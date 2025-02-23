# 5. Write a Python program to identify degree of a given node.
# Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to find the degree of a given node
def find_degree(root, target):
    """
    Finds the degree of a given node in the binary tree.
    :param root: The root node of the binary tree.
    :param target: The value of the node whose degree is to be found.
    :return: The degree of the node (0, 1, or 2).
    """
    if root is None:
        return -1  # Node not found
    
    # If the current node is the target node
    if root.data == target:
        if root.left and root.right:
            return 2  # Node has two children
        elif root.left or root.right:
            return 1  # Node has one child
        else:
            return 0  # Node has no children
    
    # Recursively search in the left subtree
    left_degree = find_degree(root.left, target)
    if left_degree != -1:
        return left_degree
    
    # Recursively search in the right subtree
    right_degree = find_degree(root.right, target)
    if right_degree != -1:
        return right_degree
    
    return -1  # Node not found

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

    # Node to find the degree of
    target_node = 2

    # Find the degree of the target node
    degree = find_degree(root, target_node)
    if degree != -1:
        print(f"The degree of node {target_node} is: {degree}")
    else:
        print(f"Node {target_node} not found in the tree.")