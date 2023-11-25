class Solution:
    def maximalSquare(self,matrix):
        if(len(matrix)==0 or len(matrix[0])==0):
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*(cols+1) for i in range(0,rows+1)]

        maxSqLen = 0
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if(matrix[i-1][j-1]=='1'):
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxSqLen = max(maxSqLen,dp[i][j])

        return maxSqLen*maxSqLen


X = Solution()
print(X.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

# Time Complexity : O(M*N)
# Space Complexity : O(M*N)

