# 9. Write a Python program to prove that binary search tree is better than binary tree.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search_bst(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search_bst(root.right, key)
    return search_bst(root.left, key)

def search_bt(root, key):
    if root is None:
        return None
    if root.val == key:
        return root
    left = search_bt(root.left, key)
    if left:
        return left
    return search_bt(root.right, key)

# Example usage
# BST
bst_root = TreeNode(50)
bst_root.left = TreeNode(30)
bst_root.right = TreeNode(70)
bst_root.left.left = TreeNode(20)
bst_root.left.right = TreeNode(40)
bst_root.right.left = TreeNode(60)
bst_root.right.right = TreeNode(80)

# Binary Tree (not a BST)
bt_root = TreeNode(50)
bt_root.left = TreeNode(30)
bt_root.right = TreeNode(70)
bt_root.left.left = TreeNode(80)
bt_root.left.right = TreeNode(40)
bt_root.right.left = TreeNode(60)
bt_root.right.right = TreeNode(20)

element = 60
print("Searching in BST:")
result = search_bst(bst_root, element)
print(f"Element {element} found in BST." if result else f"Element {element} not found in BST.")

print("Searching in Binary Tree:")
result = search_bt(bt_root, element)
print(f"Element {element} found in Binary Tree." if result else f"Element {element} not found in Binary Tree.")