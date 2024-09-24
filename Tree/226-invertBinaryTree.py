# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# Solution class to invert a binary tree
class Solution(object):
    # Inverting the tree using recursion
    def invertTree_I(self, root):
        # Function to invert a binary tree recursively
        if not root:
            # If the node is None, return None (base case)
            return None

        # Recursively invert the left and right subtrees
        left = self.invertTree_I(root.left)
        right = self.invertTree_I(root.right)

        # Swap the left and right children
        root.left = right
        root.right = left

        # Return the inverted tree rooted at the current node
        return root

    # Inverting the tree using iteration
    def invertTree_II(self, root):
        # Function to invert a binary tree iteratively
        if not root:
            # If the tree is empty, return None
            return None

        queue = []  # Queue for level order traversal
        queue.append(root)  # Start by adding the root node to the queue

        while queue:
            # Process nodes in the queue
            current = queue.pop(0)  # Dequeue the front node

            # Swap the left and right children of the current node
            current.left, current.right = current.right, current.left

            # Enqueue the left and right children (if they exist) for further processing
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        # Return the root of the inverted tree
        return root

# Example usage:

# Construct the binary tree:
#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9

tree = TreeNode(4)  # Root node with value 4
tree.left = TreeNode(2)  # Left child of root with value 2
tree.right = TreeNode(7)  # Right child of root with value 7
tree.left.left = TreeNode(1)  # Left child of node 2 with value 1
tree.left.right = TreeNode(3)  # Right child of node 2 with value 3
tree.right.left = TreeNode(6)  # Left child of node 7 with value 6
tree.right.right = TreeNode(9)  # Right child of node 7 with value 9

# Instantiate the Solution class and invert the binary tree
X = Solution()
invertTree1 = X.invertTree_I(tree)  # Inversion using recursion
invertTree2 = X.invertTree_II(tree)  # Inversion using iteration

# Check if both methods yield the same result (should be True)
print(invertTree1 == invertTree2)  # Output True if both trees are equivalent

# Time Complexity: O(N), where N is the number of nodes in the tree (we visit each node once)
# Space Complexity: O(N), due to the recursion stack in the recursive method and the queue in the iterative method
