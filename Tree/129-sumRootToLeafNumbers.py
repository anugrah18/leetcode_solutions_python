# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root) -> int:


        def dfs(curr, num):
            if not curr:
                return 0

            num = num * 10 + curr.val  # Append current node value to the number

            # If leaf node is reached, return the formed number
            if not curr.left and not curr.right:
                return num

            # Recursively compute sum from left and right subtrees
            return dfs(curr.left, num) + dfs(curr.right, num)

        return dfs(root, 0)  # Start DFS with an initial sum of 0


# Example Usage:
X = Solution()

# Constructing the tree:
#      1
#     / \
#    2   3
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

print(X.sumNumbers(node1))  # Output: 25 (12 + 13)

# Time Complexity: O(N), where N is the number of nodes in the tree
# Space Complexity: O(N)
