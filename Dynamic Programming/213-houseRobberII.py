class Solution:
    def rob(self, nums) -> int:
        # Edge case: if nums is empty, return 0
        if not nums:
            return 0
        # Edge case: if nums has only one element, return that element
        if len(nums) == 1:
            return nums[0]
        # For a circular house arrangement, consider two cases:
        # 1. Rob houses from 0 to n-2 (excluding the last house)
        # 2. Rob houses from 1 to n-1 (excluding the first house)
        # Take the maximum of these two cases and the first house (for single house array)
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums) -> int:
        # If nums is empty, return 0
        if len(nums) == 0:
            return 0
        # If nums has only one element, return that element
        if len(nums) == 1:
            return nums[0]
        # Initialize a dp array where dp[i] represents the maximum amount of money
        # that can be robbed from the first i houses
        dp = [0] * len(nums)
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # Fill the dp array
        for i in range(2, len(nums)):
            # For each house i, we have two choices:
            # 1. Do not rob house i, in which case the max money is dp[i-1]
            # 2. Rob house i, in which case the max money is dp[i-2] + nums[i]
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # The last element of dp contains the maximum amount of money that can be robbed
        return dp[-1]


X = Solution()
print(X.rob([1,2,3,1]))

# Time Complexity : O(N)
# Space Complexity : O(N)