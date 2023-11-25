class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self,root):
        res = [root.val]

        def leftBoundary(root):
            if not root:
                return
            if root.left:
                res.append(root.val)
                leftBoundary(root.left)
            elif root.right:
                res.append(root.val)
                leftBoundary(root.right)

        def rightBoundary(root):
            if not root:
                return
            if root.right:
                rightBoundary(root.right)
                res.append(root.val)
            elif root.left:
                rightBoundary(root.left)
                res.append(root.val)

        def leaves(root):
            if not root:
                return
            leaves(root.left)
            if not root.left and not root.right:
                res.append(root.val)
            leaves(root.right)

        leftBoundary(root.left)
        leaves(root.left)
        leaves(root.right)
        rightBoundary(root.right)

        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)

X = Solution()
print(X.boundaryOfBinaryTree(root))

# Time Complexity : O(n)
# Space Complexity : O(n)