class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1  # Base case: There's 1 way to make amount 0 (no coins)

        # Traverse coins in reverse
        for i in range(len(coins) - 1, -1, -1):
            coin = coins[i]
            for a in range(1, amount + 1):
                # If the coin can be used to form the current amount
                if coin <= a:
                    dp[a] += dp[a - coin]  # Add ways to form (a - coin)

        return dp[amount]

X = Solution()
print(X.change(5,[1,2,5]))

# Time Complexity : O(N*A) , where N = number of coin types , A = amount
# Space Complexity : O(A) , where A = amount

