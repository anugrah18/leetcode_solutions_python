class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

class Solution:
    def buildTree(self, inorder, postorder):

        def rec(inorder,postorder):
            if not inorder or not postorder:
                return

            root = TreeNode(postorder.pop())
            mid = inorder.index(root.val)
            root.right = rec(inorder[mid+1:],postorder)
            root.left = rec(inorder[:mid],postorder)
            return root

        return rec(inorder,postorder)


X= Solution()
root = X.buildTree([3,9,20,15,7],[9,3,15,20,7])
Inorder(root)

# Time Complexity : O(N)
# Space Complexity : O(N)