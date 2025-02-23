# 3. Write a Python program to create a binary tree using array only and display the tree level wise.
class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size  # Array representation of the binary tree
        self.size = size

    def insert(self, index, value):
        if index >= self.size:
            print("Index out of bounds")
            return
        self.tree[index] = value

    def display(self):
        level = 0
        index = 0
        while index < self.size:
            count = 2 ** level  # Number of nodes at this level
            level_values = []
            for i in range(count):
                if index < self.size and self.tree[index] is not None:
                    level_values.append(str(self.tree[index]))
                else:
                    level_values.append("_")
                index += 1
            print(" ".join(level_values))
            level += 1

# Example Usage
tree_size = 15  # Example size
tree = BinaryTree(tree_size)

# Inserting elements into the binary tree
tree.insert(0, 1)
tree.insert(1, 2)
tree.insert(2, 3)
tree.insert(3, 4)
tree.insert(4, 5)
tree.insert(5, 6)
tree.insert(6, 7)

tree.display()
