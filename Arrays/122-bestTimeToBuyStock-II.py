class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        for i in range(1, len(prices)):
            if (prices[i] > prices[i - 1]):
                maxProfit = maxProfit + prices[i] - prices[i - 1]

        return maxProfit


X =Solution()
stockPrices = [7,1,55,3,6,24]

print(X.maxProfit(stockPrices))

# Time Complexity : O(n)

# Space Complexity = O(1)
