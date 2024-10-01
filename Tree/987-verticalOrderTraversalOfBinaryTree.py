# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a binary tree node with a value, left child, and right child
        self.val = val  # Node value
        self.left = left  # Left child
        self.right = right  # Right child

# Solution class for performing vertical order traversal of a binary tree
class Solution:
    # Function to perform vertical traversal of a binary tree
    def VerticalTraversal(self, root):
        # List to store tuples of (column, row, node value)
        node_list = []

        # Helper function to perform Depth-First Search (DFS)
        # It tracks the column and row of each node in the tree
        def DFS(column, row, node):
            if node is not None:
                # Add the current node's column, row, and value to the node_list
                node_list.append((column, row, node.val))
                # Traverse the left subtree (column - 1, row + 1)
                DFS(column - 1, row + 1, node.left)
                # Traverse the right subtree (column + 1, row + 1)
                DFS(column + 1, row + 1, node.right)

        # Start DFS traversal from the root node, located at column 0 and row 0
        DFS(0, 0, root)

        # Sort the node_list first by column, then by row, and finally by node value
        node_list.sort()

        # Initialize variables to track the current column index and list of values in the current column
        curr_column_index = node_list[0][0]  # Start with the first column in the list
        curr_column = []  # List to store node values for the current column
        ans = []  # List to store the final result of the vertical traversal

        # Iterate through the sorted node_list
        for column, row, value in node_list:
            # If the current node is in the same column as the previous one
            if column == curr_column_index:
                # Add the node value to the current column list
                curr_column.append(value)
            else:
                # If the column has changed, append the current column list to the result
                ans.append(curr_column)
                # Update the current column index and start a new column list
                curr_column_index = column
                curr_column = [value]

        # Append the last column to the result
        ans.append(curr_column)

        # Return the list of node values grouped by vertical columns
        return ans

# Example usage:
# Construct the following binary tree:
#         3
#       /   \
#      9     20
#           /  \
#         15    7

root = TreeNode(3)  # Root node with value 3
root.left = TreeNode(9)  # Left child of root with value 9
root.right = TreeNode(20)  # Right child of root with value 20
root.right.left = TreeNode(15)  # Left child of node 20 with value 15
root.right.right = TreeNode(7)  # Right child of node 20 with value 7

# Create a Solution object and perform vertical order traversal
X = Solution()
print(X.VerticalTraversal(root))  # Output: [[9], [3, 15], [20], [7]]

# Time Complexity: O(NLogN)
# Sorting the node list takes O(N log N) time, where N is the number of nodes.
# Space Complexity: O(N)
# The space complexity is O(N) due to the space required to store the node_list.
