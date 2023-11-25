class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -float('inf')
        return inorder(root)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

X = Solution()
print(X.isValidBST(root))

# Time Complexity = O(N)
# Space Complexity = O(1)