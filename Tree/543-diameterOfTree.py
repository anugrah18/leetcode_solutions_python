# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


# Solution class to compute the diameter of a binary tree
class Solution(object):
    diameter = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def longest_path(node):
            if not node:
                return 0
            # recursively find the longest path in
            # both left child and right child
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # update the diameter if left_path plus right_path is larger
            self.diameter = max(self.diameter, left_path + right_path)

            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return max(left_path, right_path) + 1

        longest_path(root)
        return self.diameter


# Example usage:

# Construct the binary tree:
#        1
#       / \
#      2   3
#     / \  / \
#    4  5 6   7
#             \
#              8

root = TreeNode(1)  # Root node with value 1
root.left = TreeNode(2)  # Left child of root with value 2
root.right = TreeNode(3)  # Right child of root with value 3
root.left.left = TreeNode(4)  # Left child of node 2 with value 4
root.left.right = TreeNode(5)  # Right child of node 2 with value 5
root.right.left = TreeNode(6)  # Left child of node 3 with value 6
root.right.right = TreeNode(7)  # Right child of node 3 with value 7
root.right.right.right = TreeNode(8)  # Right child of node 7 with value 8

# Instantiate the Solution class and compute the diameter of the binary tree
X = Solution()
print(X.diameterOfBinaryTree(root))  # Output the diameter of the tree

# Time Complexity: O(N), where N is the number of nodes in the tree (we visit each node once)
# Space Complexity: O(N), due to the recursion stack in a skewed tree scenario
