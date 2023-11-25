
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Using Recursion.
    def invertTree_I(self, root):
        if not root:
            return None

        left = self.invertTree_I(root.left)
        right = self.invertTree_I(root.right)

        root.left = right
        root.right = left

        return root

    # Using Iterations.
    def invertTree_II(self, root):
        if not root:
            return None

        queue =[]
        queue.append(root)
        while queue:
            current = queue.pop(0)
            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root


tree= TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

X =Solution()
invertTree1= X.invertTree_I(tree)
invertTree2= X.invertTree_II(tree)
print(invertTree1==invertTree2)

# Time Complexity : O(N)
# Space Complexity : O(N)