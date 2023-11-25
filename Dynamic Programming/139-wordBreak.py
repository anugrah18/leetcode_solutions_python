class Solution:
    def wordBreak(self,s,wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(0,len(s)):
            if(dp[i]==True):
                for j in range(i+1,len(s)+1):
                    if(s[i:j] in wordDict):
                        dp[j]=True

        return dp[-1]

X = Solution()
print(X.wordBreak('leetcode',['leet','code']))

# Time Complexity : O(N^3) , N^2 for loops and additional N for substring computation.
# Space Complexity : O(N)

