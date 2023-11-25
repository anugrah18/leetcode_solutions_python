class Solution:
    def isMatch(self, s, p):
        dp = [[False for x in range(len(p) + 1)] for y in range(len(s) + 1)]

        dp[0][0] = True

        for j in range(1, len(dp[0])):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]

                    if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

X = Solution()
print(X.isMatch("aabacde","a*b.cd."))