class Solution:
    def dfs(self,i,j,grid):
        if(i<0 or i>len(grid)-1 or j<0 or j>len(grid[i])-1 or grid[i][j]==0):
            return 0

        grid[i][j]=0
        count=1

        count+=self.dfs(i+1,j,grid)
        count+=self.dfs(i-1,j,grid)
        count+=self.dfs(i,j+1,grid)
        count+=self.dfs(i,j-1,grid)
        return count

    def maxAreaOfIsland(self,grid):
        maxArea = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if(grid[i][j]==1):
                    maxArea = max(maxArea,self.dfs(i,j,grid))
        return maxArea

X = Solution()
print(X.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))

# Time Complexity : O(RC), R = number of rows and C = number of column
# Space Complexity : O(RC)