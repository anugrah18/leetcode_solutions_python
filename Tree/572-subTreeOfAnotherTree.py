# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with a value, left child, and right child
        self.val = val
        self.left = left
        self.right = right

# Solution class to check if one tree is a subtree of another
class Solution:
    # Function to check if subRoot is a subtree of root
    def isSubtree(self, root, subRoot) -> bool:
        # If subRoot is None, it's always a subtree
        if not subRoot:
            return True
        # If root is None, but subRoot is not, it's not a subtree
        if not root:
            return False

        # If the trees rooted at current nodes are the same, return True
        if self.isSameTree(root, subRoot):
            return True

        # Recursively check the left and right subtrees of the root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Helper function to check if two trees are identical
    def isSameTree(self, p, q):
        # If both trees are None, they are identical
        if not p and not q:
            return True
        # If one tree is None and the other is not, they are not identical
        if not p or not q:
            return False

        # Check if the current nodes are the same and recursively check left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Example usage:
# Construct the main tree:
#         3
#       /   \
#      4     5
#     / \
#    1   2

root = TreeNode(3)                  # Root node with value 3
root.left = TreeNode(4)             # Left child of root with value 4
root.right = TreeNode(5)            # Right child of root with value 5
root.left.left = TreeNode(1)        # Left child of node 4 with value 1
root.left.right = TreeNode(2)       # Right child of node 4 with value 2

# Construct the subtree:
#       4
#      / \
#     1   2

subRoot = TreeNode(4)               # Root node of subRoot with value 4
subRoot.left = TreeNode(1)          # Left child of subRoot with value 1
subRoot.right = TreeNode(2)         # Right child of subRoot with value 2

# Create an instance of Solution and check if subRoot is a subtree of root
X = Solution()
print(X.isSubtree(root, subRoot))   # Output should be True, as subRoot is a subtree of root

# Time Complexity : O(M * N)
# Where M is the number of nodes in subTree, and N is the number of nodes in the main Tree
# This is because for each node in the main tree, we may have to check the entire subtree.

# Space Complexity : O(M + N)
# Due to the recursion stack in the worst case, when both trees are completely skewed.
