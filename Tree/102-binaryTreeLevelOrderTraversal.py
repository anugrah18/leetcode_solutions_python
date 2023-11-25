class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution(object):
    def levelOrder(self, root):
        levels = []
        if (root == None):
            return levels

        level = 0
        queue = []
        queue.append(root)
        while (queue):
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                levels[level].append(node.val)
                if (node.left != None):
                    queue.append(node.left)
                if (node.right != None):
                    queue.append(node.right)

            level = level + 1

        return levels

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

X = Solution()
ans = X.levelOrder(root)
print(ans)

# Time Complexity : O(N)
# Space Complexity : O(N)