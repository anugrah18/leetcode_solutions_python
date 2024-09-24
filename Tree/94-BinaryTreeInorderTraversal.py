# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


# Solution class to perform inorder traversal of the binary tree
class Solution(object):
    def inorderTraversal(self, root):
        # This function performs inorder traversal and returns the list of node values in inorder

        InorderLt = []  # List to store inorder traversal result
        self.inorderTree(root, InorderLt)  # Call helper function to traverse the tree
        return InorderLt  # Return the result list

    def inorderTree(self, root, lt=[]):
        # Helper function for recursive inorder traversal
        # Takes in the current node (root) and the list to store the result (lt)

        if root == None:
            # Base case: if the current node is None, just return (nothing to process)
            return
        else:
            # Recursive case: traverse the left subtree, process the current node, then traverse the right subtree
            self.inorderTree(root.left, lt)  # Traverse left subtree
            lt.append(root.val)  # Add current node's value to the result list
            self.inorderTree(root.right, lt)  # Traverse right subtree


# Example usage:

# Construct the binary tree:
#     1
#      \
#       2
#      / \
#     3   4

Tree = TreeNode(1)  # Root node with value 1
Tree.left = None  # No left child for root
Tree.right = TreeNode(2)  # Right child with value 2
Tree.right.left = TreeNode(3)  # Left child of node 2 with value 3
Tree.right.right = TreeNode(4)  # Right child of node 2 with value 4

# Instantiate the Solution class and perform inorder traversal
X = Solution()
lt = X.inorderTraversal(Tree)  # Perform inorder traversal on the constructed tree
print(lt)  # Output the result list

# Time Complexity: O(N) where N is the number of nodes in the tree
# Space Complexity: O(N) due to the recursion stack and the result list
