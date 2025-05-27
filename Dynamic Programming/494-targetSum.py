class Solution:
    def findTargetSumWays(self, nums,target ):
        dp = {}
        # Base case: There is 1 way to reach sum = 0 using 0 elements
        dp[0] = 1

        # Iterate over each number in the input list
        for num in nums:
            next_dp = {}  # To store new combinations of sums

            # For each sum seen so far, try adding and subtracting current num
            for total, count in dp.items():
                # Add the number: update ways to reach (total + num)
                next_dp[total + num] = next_dp.get(total + num, 0) + count

                # Subtract the number: update ways to reach (total - num)
                next_dp[total - num] = next_dp.get(total - num, 0) + count

            # Move to the next state
            dp = next_dp

        # Return number of ways to reach the target sum
        return dp.get(target, 0)

X = Solution()
print(X.findTargetSumWays([1,1,1,1,1] , 3))

# Time Complexity : O(N*S) , where N = number of element in nums , S = Range of possible sums (i.e. 2*sum(nums)+1)
# Space Complexity : O(S)