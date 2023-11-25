
class TreeNode(object):
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):

        levels = []
        if not root:
            return levels

        level = 0
        queue = []
        queue.append(root)

        while (queue):
            levels.append([])
            lvl_length = len(queue)
            for i in range(lvl_length):
                node = queue.pop(0)
                levels[level].append(node.val)

                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)

            level += 1

        for i in range(0, len(levels)):
            if (i % 2 == 1):
                levels[i] = levels[i][::-1]

        return levels

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)

X = Solution()
print(X.zigzagLevelOrder(tree))

# Time Complexity : O(N)
# Space Complexity : O(N)