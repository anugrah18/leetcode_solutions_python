class Solution(object):
    def maxProfit(self, prices):
        # Check if the list of prices is empty
        if(len(prices)==0):
            return 0
        # Initialize variables to track current minimum price and maximum profit
        ans = 0
        currPrice = prices[0]

        # Iterate through the list of prices starting from the second price
        for i in range(1, len(prices)):
            # Check if the current price is less than the current minimum price
            if prices[i] < currPrice:
                # Update current minimum price
                currPrice = prices[i]
            else:
                # Calculate the profit if selling at the current price
                # Update the maximum profit if the calculated profit is greater
                ans = max(ans, prices[i] - currPrice)
        # Return the maximum profit that can be achieved
        return ans


X = Solution()
print(X.maxProfit([7,1,5,3,6,4]))

# Time Complexity : O(N)
# Space Complexity : O(1)

