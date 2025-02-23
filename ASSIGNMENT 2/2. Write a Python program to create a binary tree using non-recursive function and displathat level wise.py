# 2. Write a Python program to create a binary tree using non-recursive function and displathat level wise
from collections import deque

# Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to create a binary tree using a non-recursive approach
def create_binary_tree(elements):
    if not elements:
        return None
    
    # Create the root node
    root = Node(elements[0])
    q = deque([root])
    
    idx = 1
    while q and idx < len(elements):
        current_node = q.popleft()
        
        # Assign the left child
        if idx < len(elements):
            current_node.left = Node(elements[idx])
            q.append(current_node.left)
            idx += 1
        
        # Assign the right child
        if idx < len(elements):
            current_node.right = Node(elements[idx])
            q.append(current_node.right)
            idx += 1
    
    return root

# Function to display the binary tree level-wise
def display_level_wise(root):
    if not root:
        print("Tree is empty")
        return
    
    q = deque([root])
    while q:
        level_size = len(q)
        for _ in range(level_size):
            current_node = q.popleft()
            print(current_node.data, end=" ")
            
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        print()  # Move to the next level

# Example usage
if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5, 6, 7]
    root = create_binary_tree(elements)
    print("Level-wise display of the binary tree:")
    display_level_wise(root)