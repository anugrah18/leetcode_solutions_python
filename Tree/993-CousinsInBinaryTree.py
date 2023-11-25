class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSibling(self, root, x, y):
        if not root:
            return False

        return ((root.left and root.left.val == x and root.right and root.right.val == y) or
                (root.left and root.left.val == y and root.right and root.right.val == x) or
                self.isSibling(root.left, x, y) or
                self.isSibling(root.right, x, y))

    def level(self, root, p, lvl):
        if not root:
            return 0
        if root.val == p:
            return lvl

        # Return level if Node is present in left subtree
        l = self.level(root.left, p, lvl + 1)
        if l != 0:
            return l

        # Else search in right subtree
        return self.level(root.right, p, lvl + 1)

    def isCousins(self, root, x: int, y: int) -> bool:
        if ((self.level(root, x, 0) == self.level(root, y, 0)) and
                not (self.isSibling(root, x, y))):
            return True
        else:
            return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

X = Solution()
print(X.isCousins(root,4,6))

# Time Complexity : O(N) , N = Number of nodes in binary tree.
# Space Complexity : O(N) , N = Number of nodes in binary tree.