class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = None  # Class variable to store the maximum path sum

    def maxPathSum(self, root) -> int:
        self.res = root.val  # Initialize res with the root value

        def dfs(root):
            if not root:  # Base case: if the current node is None, return 0
                return 0

            # Recursively calculate the maximum path sum of the left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Ignore paths with negative sums as they would decrease the overall sum
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # Update res with the maximum path sum that can be achieved by including the current node and its left and right subtrees
            self.res = max(self.res, root.val + leftMax + rightMax)

            # Return the maximum path sum that can be achieved by including the current node and one of its subtrees
            return root.val + max(leftMax, rightMax)

        dfs(root)  # Start the DFS traversal from the root
        return self.res  # Return the maximum path sum

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
X = Solution()
print(X.maxPathSum(root))

# Time Complexity: O(N)
# Space Complexity: O(N)