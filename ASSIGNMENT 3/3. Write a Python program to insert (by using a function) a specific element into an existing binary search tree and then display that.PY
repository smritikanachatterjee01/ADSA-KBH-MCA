# 3. Write a Python program to insert (by using a function) a specific element into an existing binary search tree and then display that.
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
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert_recursive(root, key)

print("BST before insertion:")
inorder_traversal(root)

# Insert a new element
root = insert_recursive(root, 55)
print("\nBST after insertion:")
inorder_traversal(root)