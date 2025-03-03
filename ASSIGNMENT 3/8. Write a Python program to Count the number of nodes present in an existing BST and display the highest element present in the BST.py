# 8. Write a Python program to Count the number of nodes present in an existing BST and display the highest element present in the BST.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current.val

# Example usage
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Number of nodes in BST:", count_nodes(root))
print("Highest element in BST:", find_max(root))