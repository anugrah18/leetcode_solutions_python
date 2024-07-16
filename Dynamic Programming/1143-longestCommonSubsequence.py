class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize a 2D dp array with dimensions (len(text2) + 1) x (len(text1) + 1)
        # dp[i][j] represents the length of the longest common subsequence of text2[0:i] and text1[0:j]
        dp = [[0 for x in range(len(text1) + 1)] for y in range(len(text2) + 1)]

        # Iterate through each character of text2
        for i in range(1, len(text2) + 1):
            # Iterate through each character of text1
            for j in range(1, len(text1) + 1):
                c1 = text1[j - 1]  # Character from text1
                c2 = text2[i - 1]  # Character from text2
                # If the characters match, the LCS length is incremented by 1 from the previous diagonal value
                if c2 == c1:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # If the characters don't match, the LCS length is the maximum of the value above or to the left
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Return the length of the longest common subsequence of the entire strings
        return dp[-1][-1]

X = Solution()
print(X.longestCommonSubsequence("abcde","ace"))


# Time Complexity : O(M*N)
# Space Complexity : O(M*N)