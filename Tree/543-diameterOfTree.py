class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    ans = 0
    def diameterOfBinaryTree(self, root):
        if (not root):
            return 0

        self.ans = max(self.ans, self._depth(root.left) + self._depth(root.right) + 1)
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.ans - 1

    def _depth(self, root):
        if not root:
            return 0
        L = self._depth(root.left)
        R = self._depth(root.right)

        return max(L, R) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

X = Solution()
print(X.diameterOfBinaryTree(root))

# Time Complexity : O(N)
# Space Complexity : O(N)
