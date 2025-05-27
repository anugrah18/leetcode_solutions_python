class Solution(object):
    def maxProfit(self, prices):
        # Initialize the states:
        # sold  = profit after selling a stock today
        # held  = profit while currently holding a stock
        # reset = profit while doing nothing today (resting or after cooldown)
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            pre_sold = sold  # Store previous sold value for use in reset

            # If we sell the stock today, we must have held it before
            sold = held + price

            # If we hold a stock today, we either:
            # - continue holding (held)
            # - buy it today (reset - price), only allowed if we were in reset state
            held = max(held, reset - price)

            # If we are in reset today, we either:
            # - were already in reset yesterday
            # - sold a stock yesterday (and are now in cooldown)
            reset = max(reset, pre_sold)

        # The final max profit will be either:
        # - in sold state (last action was a sell)
        # - in reset state (last action was a rest or cooldown)
        # We can't return 'held' because the stock hasn't been sold yet
        return max(sold, reset)

X = Solution()
print(X.maxProfit([1, 2, 3, 0, 2]))

# Time Complexity : O(N)
# Space Complexity : O(1)