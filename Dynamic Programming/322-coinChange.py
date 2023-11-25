class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

X = Solution()
print(X.coinChange([1,2,5],11))


# Time Complexity : O(N*M) , where N = amount , M = count of denomintior
# Space Complexity : O(N)