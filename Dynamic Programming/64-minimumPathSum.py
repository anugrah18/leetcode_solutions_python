class Solution:
    def minPathSum(self, grid):

        # Get the number of rows (ROWS) and columns (COLS) in the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Create a result matrix 'res' initialized with 'inf' (large value)
        # Extra row and column added to handle boundary conditions without extra checks
        res = [[float('inf')] * (COLS + 1) for i in range(ROWS + 1)]

        # Set the bottom-right boundary cell to 0 (to help with min calculation)
        res[ROWS - 1][COLS] = 0

        # Traverse the grid from bottom-right to top-left
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                # Calculate the minimum sum at each cell
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

        # The minimum path sum from (0,0) to (ROWS-1, COLS-1) is stored in res[0][0]
        return res[0][0]


# Example usage:
X = Solution()
print(X.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

# Time Complexity  : O(MN)
# Space Complexity : O(MN)
