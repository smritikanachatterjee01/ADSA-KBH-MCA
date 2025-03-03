# 2. Write a Python program to create a binary search tree using non-recursive function and display that.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_non_recursive(root, key):
    new_node = TreeNode(key)
    if root is None:
        return new_node
    current = root
    while True:
        if key < current.val:
            if current.left is None:
                current.left = new_node
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            else:
                current = current.right
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
    root = insert_non_recursive(root, key)

print("Inorder Traversal of BST:")
inorder_traversal(root)