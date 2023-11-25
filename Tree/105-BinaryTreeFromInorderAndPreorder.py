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
    def buildTree(self, preorder, inorder):
        def rec(inorder, preorder):
            if not inorder or not preorder:
                return

            root = TreeNode(preorder.pop(0))
            mid = inorder.index(root.val)
            root.left = rec(inorder[:mid], preorder)
            root.right = rec(inorder[mid + 1:], preorder)
            return root

        return rec(inorder, preorder)

    def buildTree2(self, preorder, inorder):

        mapper = {}
        for i, v in enumerate(inorder):
            mapper[v] = i

        def helper(low, high):
            if low > high:
                return

            root = TreeNode(preorder.pop(0))
            mid = mapper[root.val]
            root.left = helper(low, mid - 1)
            root.right = helper(mid + 1, high)

            return root

        return helper(0, len(inorder) - 1)

X= Solution()
root = X.buildTree([3,9,20,15,7],[9,3,15,20,7])
Inorder(root)

# Time Complexity : O(N)
# Space Complexity : O(N)