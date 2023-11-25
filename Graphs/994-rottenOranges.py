class Solution(object):
    def orangesRotting(self, grid):

        rotten = self.find_orange(grid, 2)

        fresh = self.find_orange(grid, 1)
        fresh_count = len(fresh)

        count = 0

        # if no fresh oranges exist return 0
        if fresh_count <= 0:
            return count

        while rotten:
            rotten = self.spreadInfection(grid, rotten)
            fresh_count = fresh_count - len(rotten)
            count = count + 1

            if fresh_count <= 0:
                return count

        return -1

    # new infected oranges
    def spreadInfection(self, grid, rotten=[]):
        new_rotten = []
        while len(rotten) > 0:
            (i, j) = rotten.pop(0)

            if (i > 0) and (grid[i - 1][j] == 1):
                grid[i - 1][j] = 2
                new_rotten.append((i - 1, j))
            if (i < (len(grid) - 1)) and (grid[i + 1][j] == 1):
                grid[i + 1][j] = 2
                new_rotten.append((i + 1, j))
            if (j > 0) and (grid[i][j - 1] == 1):
                grid[i][j - 1] = 2
                new_rotten.append((i, j - 1))
            if (j < (len(grid[0]) - 1)) and (grid[i][j + 1] == 1):
                grid[i][j + 1] = 2
                new_rotten.append((i, j + 1))

        return new_rotten

    # find oranges of corresponding value
    def find_orange(self, grid, value):
        oranges = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == value:
                    oranges.append((i, j))
        return oranges


X = Solution()
print(X.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

# Time Complexity : O(MN) , MN = size of grid
# Space Complexity : O(MN)
