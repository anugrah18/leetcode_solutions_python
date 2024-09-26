# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# Solution class to check if two binary trees are identical
class Solution(object):
    def isSameTree(self, p, q):
        # Function to check if two binary trees (p and q) are structurally identical and have the same node values

        if p == None and q == None:
            # If both trees are empty, they are the same
            return True
        if p == None or q == None:
            # If one of the trees is empty and the other is not, they are not the same
            return False
        if p.val != q.val:
            # If the values of the current nodes in both trees are different, they are not the same
            return False

        # Recursively check the left and right subtrees of both trees
        # Both left subtrees and right subtrees must be identical for the trees to be the same
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

# Example usage:

# Construct the first binary tree (root1):
#        1
#       / \
#      2   3

root1 = TreeNode(1)  # Root node with value 1
root1.left = TreeNode(2)  # Left child of root1 with value 2
root1.right = TreeNode(3)  # Right child of root1 with value 3

# Construct the second binary tree (root2):
#        1
#       / \
#      2   3

root2 = TreeNode(1)  # Root node with value 1
root2.left = TreeNode(2)  # Left child of root2 with value 2
root2.right = TreeNode(3)  # Right child of root2 with value 3

# Instantiate the Solution class and check if the two trees are the same
X = Solution()
print(X.isSameTree(root1, root2))  # Output True if the trees are identical, otherwise False

# Time Complexity: O(N), where N is the number of nodes in both trees (each node is visited once)
# Space Complexity: O(N), due to the recursion stack in the worst case of a skewed tree
