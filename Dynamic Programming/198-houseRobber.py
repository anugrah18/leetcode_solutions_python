class Solution(object):
    def rob(self, nums):
        # If the list of houses is empty, return 0 (no money to rob)
        if len(nums) == 0:
            return 0
        # If there's only one house, return its value (only option to rob)
        if len(nums) == 1:
            return nums[0]

        # Create a dp array to store the maximum amount of money that can be robbed up to each house
        dp = [0] * len(nums)
        # The first house can only be robbed by itself
        dp[0] = nums[0]
        # For the second house, choose the maximum between robbing the first house or the second house
        dp[1] = max(nums[0], nums[1])

        # Iterate over the remaining houses
        for i in range(2, len(nums)):
            # For each house, choose the maximum between:
            # 1. Not robbing the current house and taking the maximum amount robbed up to the previous house (dp[i-1])
            # 2. Robbing the current house and adding its value to the maximum amount robbed up to the house before the previous house (dp[i-2] + nums[i])
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The last element in the dp array contains the maximum amount that can be robbed
        return dp[-1]


X =Solution()
houses = [2,7,9,3,1]
print(X.rob(houses))

# Time Complexity : O(N)
# Space Complexity : O(N)
