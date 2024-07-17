class Solution:
    def countBits(self, n):
        # Initialize an array to store the number of 1's for each number from 0 to n
        dp = [0] * (n + 1)
        offset = 1

        # Loop through each number from 1 to n
        for i in range(1, n + 1):
            # Update the offset when i is a power of 2
            if offset * 2 == i:
                offset = i
            # Calculate the number of 1's for the current number i
            dp[i] = 1 + dp[i - offset]

        # Return the array containing the number of 1's for each number from 0 to n
        return dp


X= Solution()
print(X.countBits(2))

# Time Complexity: O(N)
# Space Complexity: O(N)