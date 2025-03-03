# 6. Write a Python program to sort a given set of integers using BST.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_recursive(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert_recursive(root.right, key)
        else:
            root.left = insert_recursive(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Example usage
integers = [50, 30, 20, 40, 70, 60, 80]
root = None
for num in integers:
    root = insert_recursive(root, num)

print("Sorted integers:")
inorder_traversal(root)