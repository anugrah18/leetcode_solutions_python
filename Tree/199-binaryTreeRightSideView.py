# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child


# Solution class to compute the right side view of a binary tree
class Solution(object):
    def rightSideView(self, root):
        # Function to return the right-side view of the binary tree, i.e.,
        # the nodes that are visible when looking at the tree from the right side.

        levels = []  # List to store values of nodes level by level
        rightVals = []  # List to store the rightmost node values at each level
        if not root:
            # If the tree is empty, return an empty list
            return levels

        queue = []  # Queue to process nodes in a breadth-first manner (FIFO)
        level = 0  # Keep track of the current level
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

        # After processing all levels, get the rightmost value at each level
        for lvl in levels:
            rightVals.append(lvl[-1])  # The last element in each level list is the rightmost node

        return rightVals  # Return the list of right-side view values


# Example usage:

# Construct the binary tree:
#        1
#       / \
#      2   3
#       \    \
#        5    4

tree = TreeNode(1)  # Root node with value 1
tree.left = TreeNode(2)  # Left child of root with value 2
tree.right = TreeNode(3)  # Right child of root with value 3
tree.left.right = TreeNode(5)  # Right child of node 2 with value 5
tree.right.right = TreeNode(4)  # Right child of node 3 with value 4

# Instantiate the Solution class and compute the right side view
X = Solution()
print(X.rightSideView(tree))  # Output the list of rightmost node values from each level

# Time Complexity: O(N), where N is the number of nodes in the tree (we visit each node once)
# Space Complexity: O(N), for the queue used in the breadth-first traversal and the result list
