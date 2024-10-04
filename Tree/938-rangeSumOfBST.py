# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with a value, left child, and right child
        self.val = val
        self.left = left
        self.right = right


# Solution class to calculate the sum of nodes with values within a given range in a Binary Search Tree
class Solution:
    # Initialize the sum to 0
    ans = 0

    # Function to compute the range sum of BST
    def rangeSumBST(self, root, low: int, high: int):

        # Helper function to perform Depth-First Search (DFS)
        def dfs(node):
            if node:
                # If the current node's value is within the range [low, high], add its value to the sum
                if low <= node.val <= high:
                    self.ans += node.val
                # If the current node's value is greater than low, explore the left subtree (values less than current node)
                if low < node.val:
                    dfs(node.left)
                # If the current node's value is less than high, explore the right subtree (values greater than current node)
                if node.val < high:
                    dfs(node.right)

        # Reset the sum to 0 before starting the DFS
        self.ans = 0
        dfs(root)  # Start the DFS from the root node
        return self.ans  # Return the final sum


# Example usage:
# Construct the following binary search tree (BST):
#           10
#         /    \
#        5      15
#       / \       \
#      3   7      18

root = TreeNode(10)  # Root node with value 10
root.left = TreeNode(5)  # Left child of root with value 5
root.left.left = TreeNode(3)  # Left child of node 5 with value 3
root.left.right = TreeNode(7)  # Right child of node 5 with value 7
root.right = TreeNode(15)  # Right child of root with value 15
root.right.right = TreeNode(18)  # Right child of node 15 with value 18

# Create an instance of Solution and calculate the range sum of nodes within [7, 15]
X = Solution()
print(X.rangeSumBST(root, 7, 15))  # Output the sum of values within the range [7, 15]

# Time Complexity : O(N) - We may visit all the nodes in the tree in the worst case.
# Space Complexity : O(N) - Space used by the recursion stack, proportional to the tree height in the worst case.
