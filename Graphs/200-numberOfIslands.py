class Solution(object):
    def num_of_islands(self,grid):
        count = 0
        for i in range (0, len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]=="1"):
                    count = count + 1
                    self.BFSIslands(grid,i,j)
        return count

    def BFSIslands(self,grid,i,j):
        if(i<0 or j<0 or i==len(grid) or j==len(grid[0]) or grid[i][j] == "0"):
            return
        else:
            grid[i][j] = "0"
        self.BFSIslands(grid,i+1,j)
        self.BFSIslands(grid,i-1,j)
        self.BFSIslands(grid,i,j+1)
        self.BFSIslands(grid,i,j-1)

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