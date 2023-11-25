class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    res = 0
    def goodNodes(self,root):
        self.dfs(root,-float('inf'),self.res)
        return self.res

    def dfs(self,root,max_value,result):
        if not root:
            return

        if root.val>=max_value:
            self.res+=1
            max_value=root.val

        self.dfs(root.left,max_value,result)
        self.dfs(root.right,max_value,result)

root= TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

X =Solution()
print(X.goodNodes(root))

# Time Complexity : O(N)
# Space Complexity : O(N)