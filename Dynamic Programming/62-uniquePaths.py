class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D dp array with dimensions m x n, where all values are set to 1
        # dp[i][j] represents the number of unique paths to reach cell (i, j)
        dp = [[1 for x in range(n)] for y in range(m)]

        # Iterate through the grid starting from cell (1, 1)
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to reach cell (i, j) is the sum of the paths to reach
                # the cell directly above (i-1, j) and the cell directly to the left (i, j-1)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Return the number of unique paths to reach the bottom-right cell (m-1, n-1)
        return dp[-1][-1]


X = Solution()
print(X.uniquePaths(3,7))


# Time Complexity : O(M*N)
# Space Complexity : O(M*N)