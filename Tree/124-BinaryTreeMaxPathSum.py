class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    res = None
    def maxPathSum(self, root) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # Compute max path sum with split
            self.res = max(self.res, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return self.res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
X = Solution()
print(X.maxPathSum(root))