class Solution(object):
    def numDecodings(self, s):
        dp = [0] * (len(s) + 1)

        dp[0] = 1

        if s[0] != "0":
            dp[1] = 1

        for i in range(2, len(s) + 1):
            one_digit = s[i - 1]
            if int(one_digit) > 0:
                dp[i] = dp[i - 1]

            two_digit = s[i - 2:i]
            if int(two_digit) >= 10 and int(two_digit) <= 26:
                dp[i] = dp[i] + dp[i - 2]

        return dp[-1]

X = Solution()
print(X.numDecodings("125"))

# Time Complexity : O(N) , N = length of string
# Space Complexity : O(N)