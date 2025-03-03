# 5. Write a Python program to take user name as input and display the sorted sequence of characters using BST.
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
user_name = input("Enter your name: ")
root = None
for char in user_name:
    root = insert_recursive(root, char)

print("Sorted sequence of characters:")
inorder_traversal(root)