# Definition of a tree node for a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize the node with a value, left child, and right child
        self.val = val
        self.left = left
        self.right = right


# Inorder traversal function to print nodes in "left-root-right" order
def Inorder(root):
    # Base case: If the current node is None, return (end of recursion)
    if not root:
        return
    # Recursively visit the left subtree
    Inorder(root.left)
    # Print the value of the current node
    print(root.val)
    # Recursively visit the right subtree
    Inorder(root.right)


# Solution class to build the binary tree
class Solution:
    # Function to build a binary tree from inorder and postorder traversal lists
    def buildTree(self, inorder, postorder):
        # Recursive helper function to construct the tree
        def rec(inorder, postorder):
            # Base case: If either list is empty, return None
            if not inorder or not postorder:
                return None

            # The last element in postorder is the root of the current subtree
            root = TreeNode(postorder.pop())
            # Find the index of the root in the inorder list
            mid = inorder.index(root.val)

            # Recursively build the right subtree using elements after the root in inorder
            root.right = rec(inorder[mid + 1:], postorder)
            # Recursively build the left subtree using elements before the root in inorder
            root.left = rec(inorder[:mid], postorder)

            # Return the root node of the constructed subtree
            return root

        # Start the recursive construction of the tree
        return rec(inorder, postorder)


# Create an instance of Solution and build the tree using inorder and postorder traversals
X = Solution()
root = X.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# Perform inorder traversal of the constructed tree and print the node values
Inorder(root)

# Time Complexity : O(N) - Each node is processed once.
# Space Complexity : O(N) - Space for recursion stack and storing the tree nodes.
