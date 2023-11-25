class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for x in range(n)] for y in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

X = Solution()
print(X.uniquePaths(3,7))


# Time Complexity : O(M*N)
# Space Complexity : O(M*N)