# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # To maintain left-to-right order for nodes with the same (column, row)
    index  = 0
    def verticalOrder(self, root):
        if not root:
            return []  # Handle empty tree case

        node_list = []

        def DFS(col, row, node):
            if node:
                node_list.append((col, row, self.index, node.val))
                self.index += 1  # Increase index to preserve order
                DFS(col - 1, row + 1, node.left)  # Left child goes left
                DFS(col + 1, row + 1, node.right)  # Right child goes right

        # Start DFS traversal from root
        DFS(0, 0, root)

        if not node_list:
            return []

        # Sort by column, then row, then index (to ensure left-to-right order)
        node_list.sort()

        ans = []
        curr_col_index = node_list[0][0]  # First column in sorted list
        curr_col = []

        # Iterate through sorted nodes and group them into columns
        for col, row, idx, val in node_list:
            if col == curr_col_index:
                curr_col.append(val)
            else:
                ans.append(curr_col)  # Store previous column
                curr_col_index = col  # Move to next column
                curr_col = [val]  # Start new column

        ans.append(curr_col)  # Append the last column

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
print(X.verticalOrder(root))

# Time Complexity: O(NLogN)
# Sorting the node list takes O(N log N) time, where N is the number of nodes.
# Space Complexity: O(N)
# The space complexity is O(N) due to the space required to store the node_list.
