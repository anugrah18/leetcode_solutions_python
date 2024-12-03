class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:

        def inorder(root):
            if not root:
                return True  # An empty subtree is a valid BST

            # Check the left subtree
            if not inorder(root.left):
                return False

            # Ensure the current node's value is greater than the previous node's value
            if root.val <= self.prev:
                return False

            # Update the previous node's value
            self.prev = root.val

            # Check the right subtree
            return inorder(root.right)

        self.prev = -float('inf')  # Initialize previous node value to negative infinity
        return inorder(root)  # Start the inorder traversal from the root


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

X = Solution()
print(X.isValidBST(root))

# Time Complexity = O(N)
# Space Complexity = O(N)