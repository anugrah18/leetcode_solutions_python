# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


# Solution class to determine if a binary tree is height-balanced
class Solution:
    def isBalanced(self, root) -> bool:
        # Helper function to perform depth-first search (DFS) and check if the tree is balanced
        def dfs(root):
            if not root:
                # If the node is None, it's considered balanced with a height of 0
                return [True, 0]

            # Recursively check the left and right subtrees
            left = dfs(root.left)  # Returns [isBalanced, height] for left subtree
            right = dfs(root.right)  # Returns [isBalanced, height] for right subtree

            # A tree is balanced if both left and right subtrees are balanced and the height difference is ≤ 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Return whether the tree rooted at 'root' is balanced and its height
            return [balanced, 1 + max(left[1], right[1])]

        # Start the DFS traversal and return whether the entire tree is balanced
        return dfs(root)[0]


# Example usage:

# Construct the binary tree:
#        3
#       / \
#      9  20
#         / \
#        15  7

root = TreeNode(3)  # Root node with value 3
root.left = TreeNode(9)  # Left child of root with value 9
root.right = TreeNode(20)  # Right child of root with value 20
root.right.left = TreeNode(15)  # Left child of node 20 with value 15
root.right.right = TreeNode(7)  # Right child of node 20 with value 7

# Instantiate the Solution class and check if the binary tree is balanced
X = Solution()
print(X.isBalanced(root))  # Output True if the tree is balanced, otherwise False

# Time Complexity: O(N), where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N), due to the recursion stack in a skewed tree scenario
