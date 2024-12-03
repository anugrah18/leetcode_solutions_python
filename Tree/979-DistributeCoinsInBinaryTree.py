class TreeNode:
    # Initialize a tree node with a value, and optional left and right child nodes
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Number of coins in this node
        self.left = left  # Left child node
        self.right = right  # Right child node

class Solution:
    # Method to calculate the minimum number of moves to distribute coins so that every node has exactly one coin
    def distributeCoins(self, root):
        self.ans = 0  # Initialize the answer (number of moves) to 0

        def dfs(node):
            # Perform a depth-first search (DFS) to calculate the excess coins at each node
            if not node:  # Base case: if the node is None, return 0
                return 0

            # Recursively calculate the excess coins for the left and right subtrees
            L, R = dfs(node.left), dfs(node.right)

            # Update the total moves required by adding the absolute excess coins from the left and right subtrees
            self.ans += abs(L) + abs(R)

            # Return the net excess coins for the current node
            # Net coins = coins at current node + excess from left subtree + excess from right subtree - 1 (coin needed for the node itself)
            return node.val + L + R - 1

        dfs(root)  # Start the DFS traversal from the root node
        return self.ans  # Return the total number of moves required

# Example tree:
#       3
#      / \
#     0   0
# Expected output: 2 (move 2 coins from the root to its two children)

root = TreeNode(3)  # Root has 3 coins
root.left = TreeNode(0)  # Left child has 0 coins
root.right = TreeNode(0)  # Right child has 0 coins

X = Solution()
print(X.distributeCoins(root))  # Output the result: 2

# Time Complexity: O(N)

# Space Complexity: O(H), where H is the height of the tree
# - The recursion stack uses space proportional to the height of the tree.
