# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, x):
        # Initialize a binary tree node with a value
        self.val = x  # Node value
        self.left = None  # Left child
        self.right = None  # Right child

# Solution class to find the lowest common ancestor (LCA) of two nodes in a binary tree
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Function to find the lowest common ancestor (LCA) of nodes p and q in the binary tree rooted at 'root'

        if not root:
            # If the root is None, return None (base case for recursion)
            return None

        if root.val == p.val or root.val == q.val:
            # If the current node is either p or q, return the current node
            return root

        # Recursively search for the LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # If both left and right return non-None values, then p and q are found in different subtrees,
            # and the current node is the LCA
            return root

        # If only one side returns a non-None value, that side contains both p and q
        # Return the non-None result (either left or right)
        return left or right

# Example usage:

# Construct the binary tree:
#        3
#       / \
#      5   1
#     / \ / \
#    6  2 0  8
#      / \
#     7   4

tree = TreeNode(3)  # Root node with value 3
tree.left = TreeNode(5)  # Left child of root with value 5
tree.right = TreeNode(1)  # Right child of root with value 1
tree.left.left = TreeNode(6)  # Left child of node 5 with value 6
tree.left.right = TreeNode(2)  # Right child of node 5 with value 2
tree.left.right.left = TreeNode(7)  # Left child of node 2 with value 7
tree.left.right.right = TreeNode(4)  # Right child of node 2 with value 4
tree.right.left = TreeNode(0)  # Left child of node 1 with value 0
tree.right.right = TreeNode(8)  # Right child of node 1 with value 8

# Find the LCA of nodes with values 4 and 6
Node1 = tree.left.right.right  # Node with value 4
Node2 = tree.left.left  # Node with value 6
ans = Solution()

# Print the value of the lowest common ancestor of Node1 and Node2
print(ans.lowestCommonAncestor(tree, Node1, Node2).val)  # Output: 5

# Time Complexity: O(N), where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N), due to the recursion stack in a skewed tree scenario
