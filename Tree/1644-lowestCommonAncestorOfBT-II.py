# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestorII(self, root, p, q):
        def findLCA(root):
            if not root:
                return None

            if root.val == p.val or root.val == q.val:
                return root

            left = findLCA(root.left)
            right = findLCA(root.right)

            if left and right:
                return root

            return left or right

        def exists(node, target):
            if not node:
                return False

            if node == target:
                return True

            return exists(node.left, target) or exists(node.right, target)

        lca = findLCA(root)

        if exists(root, p) and exists(root, q):
            return lca
        return None


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

print(ans.lowestCommonAncestorII(tree, Node1, Node2).val)

# Time Complexity: O(N), where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N), due to the recursion stack in a skewed tree scenario
