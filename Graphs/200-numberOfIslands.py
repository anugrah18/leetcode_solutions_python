class Solution(object):
    def num_of_islands(self, grid):
        count = 0
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If a land cell ("1") is found, it indicates a new island
                if grid[i][j] == "1":
                    count += 1
                    # Use DFS to mark all cells in the current island
                    self.helper(grid, i, j)
        return count

    def helper(self, grid, i, j):
        # Base case: if the current cell is out of bounds or water ("0"), return
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == "0":
            return
        else:
            # Mark the current cell as visited by setting it to "0"
            grid[i][j] = "0"
        # Perform DFS in all four possible directions
        self.helper(grid, i + 1, j)
        self.helper(grid, i - 1, j)
        self.helper(grid, i, j + 1)
        self.helper(grid, i, j - 1)


X = Solution()
island = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(X.num_of_islands(island))

# Time Complexity : O(MN), M = number of rows and N = number of columns
# Space Complexity : O(MN)