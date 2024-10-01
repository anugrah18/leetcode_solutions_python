# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# Solution class to determine if a binary tree is symmetric
class Solution:
    # Function to check if the tree is symmetric by calling the isMirror helper function
    def isSymmetric(self, root):
        # The tree is symmetric if the tree is a mirror of itself (root, root)
        return self.isMirror(root, root)

    # Helper function to check if two trees (t1 and t2) are mirrors of each other
    def isMirror(self, t1, t2):
        # If both trees are None, they are mirrors of each other
        if t1 == None and t2 == None:
            return True
        # If one of the trees is None and the other is not, they are not mirrors
        if t1 == None or t2 == None:
            return False
        # Check if the values of t1 and t2 are equal, and recursively check if:
        # 1. The left subtree of t1 is a mirror of the right subtree of t2
        # 2. The right subtree of t1 is a mirror of the left subtree of t2
        return (t1.val == t2.val) and (self.isMirror(t1.left, t2.right)) and (self.isMirror(t2.left, t1.right))

# Example usage:

# Construct the following symmetric binary tree:
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3

tree = TreeNode(1)  # Root node with value 1
tree.left = TreeNode(2)  # Left child of root with value 2
tree.right = TreeNode(2)  # Right child of root with value 2
tree.left.left = TreeNode(3)  # Left child of node 2 with value 3
tree.left.right = TreeNode(4)  # Right child of node 2 with value 4
tree.right.left = TreeNode(4)  # Left child of node 2 with value 4
tree.right.right = TreeNode(3)  # Right child of node 2 with value 3

# Create a Solution object and check if the tree is symmetric
X = Solution()
print(X.isSymmetric(tree))  # Output: True (The tree is symmetric)

# Time Complexity: O(N), where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N), due to the recursion stack in the worst case of a completely unbalanced tree
