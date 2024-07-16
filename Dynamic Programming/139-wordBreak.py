class Solution:
    def wordBreak(self, s, wordDict):
        # Initialize a dp array where dp[i] represents whether the substring s[0:i] can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)
        # Base case: an empty substring can always be segmented (no words needed)
        dp[0] = True

        # Iterate through the string from the start
        for i in range(0, len(s)):
            # If the substring up to i can be segmented
            if dp[i] == True:
                # Check every possible substring starting from i+1 to the end of the string
                for j in range(i + 1, len(s) + 1):
                    # If the substring s[i:j] is in wordDict, mark dp[j] as True
                    if s[i:j] in wordDict:
                        dp[j] = True

        # Return whether the entire string can be segmented
        return dp[-1]


X = Solution()
print(X.wordBreak('leetcode',['leet','code']))

# Time Complexity : O(N^2) , N = length of string.
# Space Complexity : O(N)

