# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# Inorder traversal function to print the tree nodes in in-order sequence
def Inorder(root):
    # Base case: if the root is None, return
    if not root:
        return
    # Traverse the left subtree
    Inorder(root.left)
    # Print the current node's value
    print(root.val)
    # Traverse the right subtree
    Inorder(root.right)

# Solution class for constructing the tree from preorder and inorder traversals
class Solution:
    # Function to build a binary tree from preorder and inorder traversal using slicing
    def buildTree(self, preorder, inorder):
        # Recursive function to build the tree
        def rec(inorder, preorder):
            if not inorder or not preorder:
                # Base case: if either list is empty, return None
                return None

            # Create the root node from the first element of preorder (Root is always first in preorder)
            root = TreeNode(preorder.pop(0))

            # Find the index of the root value in inorder traversal
            mid = inorder.index(root.val)

            # Recursively build the left subtree using the left part of inorder
            root.left = rec(inorder[:mid], preorder)

            # Recursively build the right subtree using the right part of inorder
            root.right = rec(inorder[mid + 1:], preorder)

            return root  # Return the constructed subtree

        return rec(inorder, preorder)  # Start building the tree recursively

    # Optimized version of buildTree using a dictionary for faster lookups in inorder traversal
    def buildTree2(self, preorder, inorder):
        # Create a dictionary to map values to their indices in inorder traversal
        mapper = {}
        for i, v in enumerate(inorder):
            mapper[v] = i  # Store value and index in the mapper

        # Helper function to build the tree using the low and high bounds for inorder traversal
        def helper(low, high):
            if low > high:
                # Base case: if low > high, return None
                return None

            # Create the root node from the first element of preorder
            root = TreeNode(preorder.pop(0))

            # Find the index of the root in inorder using the mapper
            mid = mapper[root.val]

            # Recursively build the left subtree with the elements before the root in inorder
            root.left = helper(low, mid - 1)

            # Recursively build the right subtree with the elements after the root in inorder
            root.right = helper(mid + 1, high)

            return root  # Return the constructed subtree

        return helper(0, len(inorder) - 1)  # Start building the tree using the full range of inorder

# Example usage:
# Construct the tree from preorder and inorder traversals:
# Preorder: [3, 9, 20, 15, 7]
# Inorder: [9, 3, 15, 20, 7]
X = Solution()
root = X.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# Perform inorder traversal on the constructed tree
Inorder(root)

# Time Complexity: O(N)
# The time complexity is O(N) because each node is visited once.
# Space Complexity: O(N)
# The space complexity is O(N) due to the recursive call stack and the storage for the tree structure.
