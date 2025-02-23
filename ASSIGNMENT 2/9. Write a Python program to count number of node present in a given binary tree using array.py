# 9. Write a Python program to count number of node present in a given binary tree using array.
# Function to count the number of nodes in a binary tree represented as an array
def count_nodes_in_array(tree_array):
    count = 0
    for node in tree_array:
        if node is not None:  # Count only non-None values
            count += 1
    return count
if __name__ == "__main__":
    # Array representation of a binary tree
    # None represents the absence of a node
    tree_array = [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None]
    node_count = count_nodes_in_array(tree_array)
    print(f"The number of nodes in the binary tree is: {node_count}")