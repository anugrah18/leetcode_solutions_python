# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


# Solution class to perform level order traversal (breadth-first traversal) of the binary tree
class Solution(object):
    def levelOrder(self, root):
        # Function to perform level order traversal and return a list of values at each level

        levels = []  # List to store values level by level
        if root == None:
            # If the tree is empty, return an empty list
            return levels

        level = 0  # Keep track of the current level
        queue = []  # Queue to process nodes in breadth-first order (FIFO)
        queue.append(root)  # Start by adding the root node to the queue

        while queue:
            # While there are still nodes to process in the queue

            levels.append([])  # Add an empty list to store the current level's values
            level_length = len(queue)  # Number of nodes at the current level

            for i in range(level_length):
                # Process all nodes at the current level

                node = queue.pop(0)  # Dequeue the first node from the queue
                levels[level].append(node.val)  # Add the node's value to the current level's list

                # Enqueue the left and right children (if they exist) for processing at the next level
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

            # Move to the next level
            level = level + 1

        return levels  # Return the list of levels with node values


# Example usage:

# Construct the binary tree:
#       3
#      / \
#     9   20
#        /  \
#       15   7

root = TreeNode(3)  # Root node with value 3
root.left = TreeNode(9)  # Left child of root with value 9
root.right = TreeNode(20)  # Right child of root with value 20
root.right.left = TreeNode(15)  # Left child of node 20 with value 15
root.right.right = TreeNode(7)  # Right child of node 20 with value 7

# Instantiate the Solution class and perform level order traversal
X = Solution()
ans = X.levelOrder(root)  # Perform level order traversal on the constructed tree
print(ans)  # Output the result list

# Time Complexity: O(N), where N is the number of nodes in the tree
# Space Complexity: O(N), since we store the nodes in a queue and the result list
