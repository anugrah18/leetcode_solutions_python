# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with a value, left child, and right child
        self.val = val
        self.left = left
        self.right = right


# Solution class to count good nodes in the binary tree
class Solution:
    # Initialize a counter for good nodes
    count = 0

    # Main function to find the number of good nodes
    def goodNodes(self, root: TreeNode) -> int:
        # Inner helper function to perform DFS on the tree
        def dfs(node, maxVal):
            if not node:
                # Base case: if the node is None, return (end of recursion)
                return

            # If the current node's value is greater than or equal to the max value seen so far, it's a good node
            if node.val >= maxVal:
                self.count += 1  # Increment the good node counter
                maxVal = node.val  # Update maxVal to the current node's value

            # Recursively traverse the left and right subtrees
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        # Start DFS with the root and initialize maxVal to negative infinity
        dfs(root, -float('inf'))

        # Return the final count of good nodes
        return self.count


# Example usage
# Construct the binary tree
#         3
#       /   \
#      1     4
#     /     / \
#    3     1   5

root = TreeNode(3)             # Root node with value 3
root.left = TreeNode(1)        # Left child of root with value 1
root.right = TreeNode(4)       # Right child of root with value 4
root.left.left = TreeNode(3)   # Left child of node 1 with value 3
root.right.left = TreeNode(1)  # Left child of node 4 with value 1
root.right.right = TreeNode(5) # Right child of node 4 with value 5

# Create an instance of Solution and count the good nodes
X = Solution()
print(X.goodNodes(root))  # Output the number of good nodes


# Time Complexity: O(N) - Each node is visited once.
# Space Complexity: O(N) - Space for the recursion stack in the worst case (when the tree is skewed).
