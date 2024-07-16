class Solution(object):
    def maxSubArray(self, nums):
        # Initialize maxSum to the first element of the array
        maxSum = nums[0]
        # Initialize currentSum to the first element of the array
        currentSum = nums[0]
        # Start the loop from the second element
        i = 1

        # Iterate through the array
        while i < len(nums):
            # If adding the current element to currentSum is less than the current element itself,
            # start a new subarray from the current element
            if nums[i] > currentSum + nums[i]:
                currentSum = nums[i]
            else:
                # Otherwise, extend the current subarray
                currentSum = currentSum + nums[i]

            # Update maxSum to be the maximum of maxSum and currentSum
            maxSum = max(maxSum, currentSum)
            # Move to the next element
            i = i + 1

        # Return the maximum sum of any subarray found
        return maxSum



X = Solution()
ans = X.maxSubArray([5,4,-1,7,8])

print(ans)

# Time Complexity : O(N)
# Space Complexity : O(1)

