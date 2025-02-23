# 10. Write a Python program to count number of siblings present in a binary tree.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_siblings(root):
    if root is None:
        return 0
    
    count = 0
    if root.left and root.right:
        count += 2  # Both children exist, so they are siblings
    
    count += count_siblings(root.left)
    count += count_siblings(root.right)
    
    return count

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Number of siblings in the binary tree:", count_siblings(root))
