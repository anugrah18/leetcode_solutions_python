class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorderSuccessor(self, root, p):
        successor = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor

root = TreeNode(2)
x = root.left = TreeNode(1)
root.right = TreeNode(3)

X = Solution()
print(X.inorderSuccessor(root,x).val)