class TreeNode:
 def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right

def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

class Solution:
    def buildTree(self, preorder, inorder):
        def rec(inorder, preorder):
            if not inorder or not preorder:  # Base case: if either list is empty, return
                return

            root = TreeNode(preorder.pop(0))  # Create the root node from the first element of preorder
            mid = inorder.index(root.val)  # Find the index of the root in inorder
            root.left = rec(inorder[:mid], preorder)  # Recursively build the left subtree
            root.right = rec(inorder[mid + 1:], preorder)  # Recursively build the right subtree
            return root

        return rec(inorder, preorder)  # Start the recursive building process

    def buildTree2(self, preorder, inorder):
        mapper = {}  # Dictionary to map values to their indices in inorder
        for i, v in enumerate(inorder):
            mapper[v] = i

        def helper(low, high):
            if low > high:  # Base case: if the range is invalid, return
                return

            root = TreeNode(preorder.pop(0))  # Create the root node from the first element of preorder
            mid = mapper[root.val]  # Get the index of the root from the mapper
            root.left = helper(low, mid - 1)  # Recursively build the left subtree
            root.right = helper(mid + 1, high)  # Recursively build the right subtree

            return root

        return helper(0, len(inorder) - 1)  # Start the recursive building process

X= Solution()
root = X.buildTree([3,9,20,15,7],[9,3,15,20,7])
Inorder(root)

# Time Complexity : O(N)
# Space Complexity : O(N)