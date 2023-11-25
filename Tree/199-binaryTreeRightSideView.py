class TreeNode(object):
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        levels = []
        rightVals = []
        if (not root):
            return levels
        queue = []
        level = 0
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

        for lvl in levels:
            rightVals.append(lvl[-1])

        return rightVals


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right  = TreeNode(3)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(4)

X  = Solution()
print(X.rightSideView(tree))

# Time Complexity : O(N)
# Space Complexity : O(N)
