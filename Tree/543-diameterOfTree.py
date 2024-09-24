# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


# Solution class to compute the diameter of a binary tree
class Solution(object):
    ans = 0  # Class variable to store the maximum diameter found

    def diameterOfBinaryTree(self, root):
        # Function to compute the diameter of the binary tree
        # The diameter is the length of the longest path between any two nodes in the tree.
        # This path may or may not pass through the root.

        if not root:
            # If the tree is empty, the diameter is 0
            return 0

        # Update the diameter by considering the sum of left and right depths from the current node
        self.ans = max(self.ans, self._depth(root.left) + self._depth(root.right) + 1)

        # Recursively compute the diameter for the left and right subtrees
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        # The result is the maximum diameter found minus 1 (to account for the number of edges)
        return self.ans - 1

    def _depth(self, root):
        # Helper function to calculate the depth (or height) of a subtree
        # The depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        if not root:
            # If the node is None, the depth is 0
            return 0

        # Recursively calculate the depth of the left and right subtrees
        L = self._depth(root.left)
        R = self._depth(root.right)

        # The depth of the current node is 1 plus the maximum of the depths of its left and right subtrees
        return max(L, R) + 1


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
