# 4. Write a Python program to search an element in a BST and show the result.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search_element(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search_element(root.right, key)
    return search_element(root.left, key)

# Example usage
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

element = 60
result = search_element(root, element)
if result:
    print(f"Element {element} found in the BST.")
else:
    print(f"Element {element} not found in the BST.")