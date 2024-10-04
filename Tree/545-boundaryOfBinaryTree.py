# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a tree node with a value, left child, and right child
        self.val = val
        self.left = left
        self.right = right


# Solution class to find the boundary of the binary tree
class Solution:
    # Function to find the boundary of a binary tree
    def boundaryOfBinaryTree(self, root):
        # If the root is None, return an empty list
        if not root:
            return []

        # Initialize the result list with the root's value
        res = [root.val]

        # Function to find the left boundary of the tree (excluding leaves)
        def leftBoundary(root):
            if not root:
                return
            # Traverse the left boundary while there are left children
            if root.left:
                res.append(root.val)  # Add the node value to the result list
                leftBoundary(root.left)
            # If no left child, go down the right subtree
            elif root.right:
                res.append(root.val)
                leftBoundary(root.right)

        # Function to find the right boundary of the tree (excluding leaves)
        def rightBoundary(root):
            if not root:
                return
            # Traverse the right boundary while there are right children
            if root.right:
                rightBoundary(root.right)  # Traverse first to add values later (bottom-up)
                res.append(root.val)  # Add node value after visiting right subtree
            # If no right child, go down the left subtree
            elif root.left:
                rightBoundary(root.left)
                res.append(root.val)

        # Function to find all the leaf nodes in the tree
        def leaves(root):
            if not root:
                return
            leaves(root.left)  # Recurse through the left subtree
            # If a node is a leaf (no left or right children), add its value to the result
            if not root.left and not root.right:
                res.append(root.val)
            leaves(root.right)  # Recurse through the right subtree

        # Call the helper functions to build the boundary

        leftBoundary(root.left)  # Find the left boundary (excluding the root and leaves)
        leaves(root.left)  # Find leaf nodes in the left subtree
        leaves(root.right)  # Find leaf nodes in the right subtree
        rightBoundary(root.right)  # Find the right boundary (excluding the root and leaves)

        # Return the boundary list (left boundary + leaves + right boundary)
        return res


# Example usage:
# Construct the following binary tree:
#           1
#         /   \
#        2     3
#       / \   /
#      4   5 6
#         / \ / \
#        7  8 9 10

root = TreeNode(1)  # Root node with value 1
root.left = TreeNode(2)  # Left child of root with value 2
root.right = TreeNode(3)  # Right child of root with value 3
root.left.left = TreeNode(4)  # Left child of node 2 with value 4
root.left.right = TreeNode(5)  # Right child of node 2 with value 5
root.left.right.left = TreeNode(7)  # Left child of node 5 with value 7
root.left.right.right = TreeNode(8)  # Right child of node 5 with value 8
root.right.left = TreeNode(6)  # Left child of node 3 with value 6
root.right.left.left = TreeNode(9)  # Left child of node 6 with value 9
root.right.left.right = TreeNode(10)  # Right child of node 6 with value 10

# Create an instance of Solution and find the boundary of the binary tree
X = Solution()
print(X.boundaryOfBinaryTree(root))  # Output the boundary of the tree

# Time Complexity: O(n) - Each node is visited once.
# Space Complexity: O(n) - Space required for recursion stack and result list.
