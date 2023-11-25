# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):

        InorderLt = []
        self.inorderTree(root,InorderLt)
        return InorderLt

    def inorderTree(self,root,lt=[]):
        if(root == None):
            return
        else:
            self.inorderTree(root.left,lt)
            lt.append(root.val)
            self.inorderTree(root.right,lt)

Tree = TreeNode(1)
Tree.left=None
Tree.right=TreeNode(2)
Tree.right.left = TreeNode(3)
Tree.right.right = TreeNode(4)


X= Solution()
lt = X.inorderTraversal(Tree)
print(lt)

# Time Complexity : O(N)
# Space Complexity : O(N)


