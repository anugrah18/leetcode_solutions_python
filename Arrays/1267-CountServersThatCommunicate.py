class Solution:
    def countServers(self, grid) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        target = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    target += 1

        return target

X = Solution()
print(X.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
