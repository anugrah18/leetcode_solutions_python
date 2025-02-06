class Solution(object):
    def maxSubArray(self, nums) -> int:
        # Initialize maxSum to the first element (to handle cases where all elements are negative)
        maxSum = nums[0]
        # Initialize currSum to the first element, representing the sum of the current subarray
        currSum = nums[0]

        for i in range(1, len(nums)):
            # Decide whether to extend the existing subarray or start a new one
            currSum = max(currSum + nums[i], nums[i])
            # Update maxSum if the current subarray sum is greater than the previous maxSum
            maxSum = max(currSum, maxSum)

        return maxSum



X = Solution()
ans = X.maxSubArray([5,4,-1,7,8])

print(ans)

# Time Complexity : O(N)
# Space Complexity : O(1)

