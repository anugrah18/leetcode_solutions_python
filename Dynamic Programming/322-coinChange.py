class Solution(object):
    def coinChange(self, coins, amount):
        # Initialize dp array where dp[i] represents the minimum number of coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        # Base case: 0 coins are needed to make amount 0
        dp[0] = 0

        # Iterate over each coin
        for coin in coins:
            # For each coin, update the dp array for all amounts from coin to amount
            for i in range(coin, amount + 1):
                # Update dp[i] to be the minimum of its current value or dp[i - coin] + 1
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, it means we cannot make the amount with the given coins
        return dp[amount] if dp[amount] != float('inf') else -1


X = Solution()
print(X.coinChange([1,2,5],11))


# Time Complexity : O(N*M) , where N = amount , M = count of denominator
# Space Complexity : O(N)