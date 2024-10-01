# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# Solution class to traverse the tree in a zigzag level order manner
class Solution(object):
    # Function to perform zigzag level order traversal of a binary tree
    def zigzagLevelOrder(self, root):
        # If the root is None, return an empty list
        levels = []
        if not root:
            return levels

        # Initialize level index and a queue for breadth-first search (BFS)
        level = 0
        queue = []
        queue.append(root)  # Start with the root node

        # Perform level-order traversal using BFS
        while queue:
            levels.append([])  # Append an empty list for the current level
            lvl_length = len(queue)  # Number of nodes at the current level

            # Iterate through the nodes at the current level
            for i in range(lvl_length):
                # Pop the first node from the queue
                node = queue.pop(0)
                # Add the node's value to the current level's list
                levels[level].append(node.val)

                # If the node has a left child, add it to the queue
                if node.left:
                    queue.append(node.left)
                # If the node has a right child, add it to the queue
                if node.right:
                    queue.append(node.right)

            # Move to the next level
            level += 1

        # After collecting all levels, reverse every second level to create the zigzag pattern
        for i in range(len(levels)):
            if i % 2 == 1:  # Reverse the list at odd levels (1, 3, 5, etc.)
                levels[i] = levels[i][::-1]

        # Return the list of levels with zigzag ordering
        return levels

# Example usage:

# Construct the following binary tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

tree = TreeNode(1)  # Root node with value 1
tree.left = TreeNode(2)  # Left child of root with value 2
tree.right = TreeNode(3)  # Right child of root with value 3
tree.left.left = TreeNode(4)  # Left child of node 2 with value 4
tree.left.right = TreeNode(5)  # Right child of node 2 with value 5
tree.right.left = TreeNode(6)  # Left child of node 3 with value 6
tree.right.right = TreeNode(7)  # Right child of node 3 with value 7

# Create a Solution object and perform zigzag level order traversal
X = Solution()
print(X.zigzagLevelOrder(tree))  # Output: [[1], [3, 2], [4, 5, 6, 7]]

# Time Complexity: O(N), where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N), due to the space required to store the result and the queue
