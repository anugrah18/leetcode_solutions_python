class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for x in range(len(text1) + 1)] for y in range(len(text2) + 1)]

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                c1 = text1[j - 1]
                c2 = text2[i - 1]
                if c2 == c1:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

X = Solution()
print(X.longestCommonSubsequence("abcde","ace"))


# Time Complexity : O(M*N)
# Space Complexity : O(M*N)