class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkCompleted(self,root):
        if(not root):
            return True

        queue = []
        flag = False
        queue.append(root)

        while(queue):
            node = queue.pop(0)

            if(node.left):
                if(flag):
                    return False
                queue.append(node.left)
            else:
                flag = True

            if(node.right):
                if(flag):
                    return False
                queue.append(node.right)
            else:
                flag = True

        return True

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)

X = Solution()
print(X.checkCompleted(tree))

# Time Complexity : O(N)
# Space Complexity : O(N)