# 1. Write a Python program to create a binary tree using recursive function and display that level wise.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_binary_tree(data, index):
    if index >= len(data) or data[index] is None:
        return None

    node = TreeNode(data[index])
    node.left = create_binary_tree(data, 2 * index + 1)
    node.right = create_binary_tree(data, 2 * index + 2)
    return node

def display_level_order(root):
    if not root:
        return

    queue = [root]
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

# Example usage with a single tree:
tree_data = [1, 2, 3, 4, 5, None, 6, None, None,]
root = create_binary_tree(tree_data, 0)

print("Level-order traversal:")
display_level_order(root)