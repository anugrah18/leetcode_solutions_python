# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        # Initialize the node with value x and no children
        self.val = x
        self.left = None
        self.right = None


# Solution class to find the lowest common ancestor in a binary search tree
class Solution:
    # Function to find the lowest common ancestor (LCA) of nodes p and q in the tree rooted at root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both p and q are smaller than root, LCA is in the left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both p and q are greater than root, LCA is in the right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # If p and q are on different sides of root or one is equal to root, then root is the LCA
            return root


# Example usage:
# Construct the binary search tree:
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5

root = TreeNode(6)  # Root node with value 6
p = root.left = TreeNode(2)  # Left child of root with value 2
q = root.right = TreeNode(8)  # Right child of root with value 8
root.left.left = TreeNode(0)  # Left child of node 2 with value 0
root.left.right = TreeNode(4)  # Right child of node 2 with value 4
root.left.right.left = TreeNode(3)  # Left child of node 4 with value 3
root.left.right.right = TreeNode(5)  # Right child of node 4 with value 5
root.right.left = TreeNode(7)  # Left child of node 8 with value 7
root.right.right = TreeNode(9)  # Right child of node 8 with value 9

# Create an instance of Solution and find the LCA of nodes p (2) and q (8)
X = Solution()
print(X.lowestCommonAncestor(root, p, q).val)  # Output should be 6 (the root)

# Time Complexity : O(N)
# The time complexity is O(N) where N is the number of nodes in the tree, as we may have to traverse the tree.

# Space Complexity : O(N)
# The space complexity is O(N) due to the recursion stack in the worst case when the tree is skewed.
