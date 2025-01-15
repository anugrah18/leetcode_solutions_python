class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # By Recursion
    def isValidBST_I(self, root) -> bool:

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

    # By Iteration
    def isValidBST_II(self, root) -> bool:
        # Initialize an empty list to store the in-order traversal result
        self.ans = []

        def inorder(root):
            if not root:
                return
            # Recursively traverse the left subtree
            inorder(root.left)
            # Append the value of the current node to the result list
            self.ans.append(root.val)
            # Recursively traverse the right subtree
            inorder(root.right)

        # Perform an in-order traversal of the tree
        inorder(root)
        # Check if the in-order traversal result is sorted in strictly increasing order
        for i in range(1, len(self.ans)):
            # If a previous value is greater than or equal to the current value,
            # the tree is not a valid Binary Search Tree (BST)
            if self.ans[i - 1] >= self.ans[i]:
                return False
        # If no violations are found, the tree is a valid BST
        return True


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

X = Solution()
print(X.isValidBST_I(root))
print(X.isValidBST_II(root))

# Time Complexity = O(N)
# Space Complexity = O(N)