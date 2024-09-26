# Definition for a binary tree node
class Node:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

    # Method to calculate the maximum depth of the binary tree using recursion
    def maxDepth(self, root):
        if root == None:
            # If the current node is None, return 0 (base case)
            return 0
        else:
            # Recursively calculate the depth of the left and right subtrees
            lHeight = self.maxDepth(root.left)  # Left subtree height
            rHeight = self.maxDepth(root.right)  # Right subtree height
            # The maximum depth of the tree is the greater of the left and right heights + 1 for the current node
            return max(lHeight, rHeight) + 1

    # Method to calculate the maximum depth of the binary tree using iteration (DFS)
    def maxDepth_II(self, root):
        # Stack to store pairs of (current_depth, current_node) for DFS
        stack = []
        if root is not None:
            # Start with depth 1 and the root node
            stack.append((1, root))

        depth = 0  # Initialize the depth to 0
        while stack != []:
            # Pop the top element of the stack (current_depth, current_node)
            current_depth, root = stack.pop()
            if root is not None:
                # Update the maximum depth encountered so far
                depth = max(depth, current_depth)
                # Push the left and right children to the stack with their corresponding depths
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        # Return the maximum depth
        return depth

# Example usage:

# Construct the binary tree:
#         3
#        / \
#       9  20
#          / \
#         15  7

tree = Node(3)  # Root node with value 3
tree.left = Node(9)  # Left child of root with value 9
tree.right = Node(20)  # Right child of root with value 20
tree.right.left = Node(15)  # Left child of node 20 with value 15
tree.right.right = Node(7)  # Right child of node 20 with value 7

# Print the maximum depth of the tree using recursion
print(tree.maxDepth(tree))  # Output: 4 (The maximum depth of the tree is 4)

# Print the maximum depth of the tree using iteration
print(tree.maxDepth_II(tree))  # Output: 4 (The maximum depth of the tree is 4)

# Time Complexity: O(N), where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N), due to the recursion stack or iterative stack in the worst case
