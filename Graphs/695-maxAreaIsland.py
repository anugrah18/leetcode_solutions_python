class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        maxArea = 0  # Initialize the maximum area of islands to 0

        # Iterate over each cell in the grid
        for i in range(0, len(grid)):  # Loop through rows
            for j in range(0, len(grid[0])):  # Loop through columns
                if grid[i][j] == 1:  # If the cell is part of an island
                    # Update maxArea by calculating the area of the current island
                    maxArea = max(maxArea, self.helper(grid, i, j))

        return maxArea  # Return the maximum area of any island found

    def helper(self, grid, i, j):
        # Base case: If the cell is out of bounds or is water (0), return 0
        if (i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0):
            return 0

        # Mark the current cell as visited by setting it to 0 (to avoid re-visiting)
        grid[i][j] = 0
        count = 1  # Start counting the current cell as part of the island

        # Recursively calculate the area of the island in all four directions
        count += self.helper(grid, i + 1, j)  # Down
        count += self.helper(grid, i - 1, j)  # Up
        count += self.helper(grid, i, j + 1)  # Right
        count += self.helper(grid, i, j - 1)  # Left

        return count  # Return the total area of the island connected to this cell


# Example usage:
X = Solution()
print(X.maxAreaOfIsland([[1, 1, 0, 0, 0],
                         [1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 1],
                         [0, 0, 0, 1, 1]]))  # Output: 4


# Time Complexity: O(RC)
# - R = number of rows, C = number of columns.
# - Each cell is visited once.

# Space Complexity: O(RC)
# - Space is used by the recursion stack in the worst case (all land connected).
