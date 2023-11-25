class Solution(object):
    def maxProfit(self, prices):
        if(len(prices)==0):
            return 0
        ans = 0
        currPrice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < currPrice:
                currPrice = prices[i]
            else:
                ans = max(ans, prices[i] - currPrice)

        return ans


X = Solution()
print(X.maxProfit([7,1,5,3,6,4]))

# Time Complexity : O(N)
# Space Complexity : O(1)

