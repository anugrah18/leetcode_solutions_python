class Solution:
    def pacificAtlantic(self, heights):
        # Get the number of rows and columns in the grid
        ROWS, COLS = len(heights), len(heights[0])

        # Sets to keep track of cells reachable from the Pacific and Atlantic oceans
        pac, atl = set(), set()

        # Helper function to perform DFS
        def dfs(r, c, visit, prevHeight):
            # Base case: if the cell is out of bounds, already visited, or the height is less than the previous height, return
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            # Mark the cell as visited
            visit.add((r, c))
            # Perform DFS in all four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Perform DFS from all cells in the first and last row
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Perform DFS from all cells in the first and last column
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Find all cells that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res


X = Solution()
print(X.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

# Time Complexity : O(RC)
# Space Complexity : O(RC)