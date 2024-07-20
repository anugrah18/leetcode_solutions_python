class Solution(object):
    def maxProfit(self, prices):
        # Initialize the maximum profit to 0
        maxProfit = 0

        # Iterate through the list of prices from the second day
        for i in range(1, len(prices)):
            # If the current price is greater than the previous day's price
            if prices[i] > prices[i - 1]:
                # Add the difference to the maximum profit
                maxProfit += prices[i] - prices[i - 1]

        # Return the total maximum profit
        return maxProfit


X =Solution()
stockPrices = [7,1,55,3,6,24]

print(X.maxProfit(stockPrices))

# Time Complexity : O(n)

# Space Complexity = O(1)
