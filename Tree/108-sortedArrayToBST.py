# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a node with a value, left child, and right child
        self.val = val
        self.left = left
        self.right = right


# Solution class to convert a sorted array into a Binary Search Tree (BST)
class Solution(object):
    # Main function to convert sorted array to a BST
    def sortedArrayToBST(self, nums):
        # If the array is empty, return None (no tree can be created)
        if len(nums) == 0:
            return None

        # Call helper function to recursively build the BST
        return self.convertArrayToBST(nums, 0, len(nums) - 1)

    # Helper function to recursively build the BST
    def convertArrayToBST(self, nums, left, right):
        # Base case: if left index is greater than right, return None
        if left > right:
            return None

        # Find the middle element to create a balanced BST
        mid = left + int((right - left) / 2)

        # Create a node using the middle element of the array
        node = TreeNode(nums[mid])

        # Recursively build the left subtree using the left half of the array
        node.left = self.convertArrayToBST(nums, left, mid - 1)

        # Recursively build the right subtree using the right half of the array
        node.right = self.convertArrayToBST(nums, mid + 1, right)

        # Return the constructed node
        return node


# Example usage
X = Solution()

# Convert the sorted array [1, 2, 3, 4, 5] to a BST
Tree = X.sortedArrayToBST([1, 2, 3, 4, 5])

# Output the value of the root node of the constructed BST
print(Tree.val)  # Should print 3 (the middle element of the array)

# Time Complexity : O(N) - Every element in the array is visited once to build the tree
# Space Complexity : O(N) - Space required for recursion stack and tree nodes
