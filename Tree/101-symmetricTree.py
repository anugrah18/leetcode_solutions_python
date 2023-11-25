class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self,root):
        return self.isMirror(root,root)

    def isMirror(self,t1,t2):
        if(t1==None and t2==None):
            return True
        if(t1==None or t2==None):
            return False
        return ((t1.val==t2.val) and (self.isMirror(t1.left,t2.right)) and (self.isMirror(t2.left,t1.right)))

X= Solution()
tree= TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(3)

print(X.isSymmetric(tree))

# Time Complexity: O(N)
# Space Complexity : O(N)
