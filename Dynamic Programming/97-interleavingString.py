class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If combined lengths don't match, it's impossible to interleave
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize a DP table to track interleaving possibilities
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # Base case: empty s1 and s2 matches empty s3
        dp[len(s1)][len(s2)] = True

        # Iterate backwards through dp table to fill it
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # Check if the next character from s1 matches s3, and next state is valid
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                # Check if the next character from s2 matches s3, and next state is valid
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        # Result is whether the full strings can interleave to form s3
        return dp[0][0]

X = Solution()
print(X.isInterleave("aabcc","dbbca","aadbbcbcac"))

# Time Complexity = O(M*N) , where M = len(s1) N = len(s2)
# Space Complexity = O(M*N)
