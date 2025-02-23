# 6. Write a Python program to count number of leaf node present in a binary tree.
# Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def count_leaf_nodes(root):
   
    if root is None:
        return 0  
   
    if root.left is None and root.right is None:
        return 1
    left_leaves = count_leaf_nodes(root.left)
    right_leaves = count_leaf_nodes(root.right)
    return left_leaves + right_leaves


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    leaf_count = count_leaf_nodes(root)
    print(f"The number of leaf nodes in the binary tree is: {leaf_count}")