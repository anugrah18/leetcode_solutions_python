# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return None

        if (root.val == p.val or root.val == q.val):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right):
            return root

        else:
            return left or right

tree= TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)

Node1 = tree.left.right.right
Node2 = tree.left.left
ans = Solution()

print(ans.lowestCommonAncestor(tree,Node1,Node2).val)

# Time Complexity : O(N)
# Space Complexity : O(N)


