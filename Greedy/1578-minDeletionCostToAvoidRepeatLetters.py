class Solution:
    def minCost(self,s,cost):
        prev = 0
        res = 0
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                prev = i
            else:
                res += min(cost[prev], cost[i])
                if cost[prev] < cost[i]:
                    prev = i

        return res

X= Solution()
print(X.minCost("abaac",[1,2,3,4,5]))

# Time Complexity : O(N)
# Space Complexity : O(1)