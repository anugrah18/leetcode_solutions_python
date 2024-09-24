# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


# Solution class to check if a binary tree is complete
class Solution:
    def checkCompleted(self, root):
        # Function to check if a binary tree is a complete binary tree
        # A complete binary tree has all levels completely filled except possibly the last,
        # which is filled from left to right.

        if not root:
            # If the tree is empty, it's considered complete
            return True

        queue = []  # Queue for level order traversal
        flag = False  # Flag to track if a missing child has been encountered
        queue.append(root)  # Start by adding the root node to the queue

        while queue:
            # Process nodes level by level
            node = queue.pop(0)  # Dequeue the first node from the queue

            # Check the left child
            if node.left:
                if flag:
                    # If a missing child was encountered previously, and now we see a left child,
                    # it means the tree is not complete
                    return False
                queue.append(node.left)  # Add the left child to the queue for further processing
            else:
                flag = True  # Set the flag if the left child is missing

            # Check the right child
            if node.right:
                if flag:
                    # If a missing child was encountered previously, and now we see a right child,
                    # it means the tree is not complete
                    return False
                queue.append(node.right)  # Add the right child to the queue for further processing
            else:
                flag = True  # Set the flag if the right child is missing

        # If we completed the traversal without issues, the tree is complete
        return True


# Example usage:

# Construct the binary tree:
#        1
#       / \
#      2   3
#     / \  /
#    4  5 6

tree = TreeNode(1)  # Root node with value 1
tree.left = TreeNode(2)  # Left child of root with value 2
tree.right = TreeNode(3)  # Right child of root with value 3
tree.left.left = TreeNode(4)  # Left child of node 2 with value 4
tree.left.right = TreeNode(5)  # Right child of node 2 with value 5
tree.right.left = TreeNode(6)  # Left child of node 3 with value 6

# Instantiate the Solution class and check if the binary tree is complete
X = Solution()
print(X.checkCompleted(tree))  # Output True if the tree is complete, otherwise False

# Time Complexity: O(N), where N is the number of nodes in the tree (we visit each node once)
# Space Complexity: O(N), for the queue used in the level order traversal
