class Solution:
    def lengthOfLIS(self, nums) -> int:
        # Initialize a dp array where dp[i] represents the length of the longest increasing subsequence ending at index i
        dp = [1] * len(nums)
        # Variable to keep track of the maximum length of LIS found so far
        maxTillNow = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # For each element, check all previous elements
            for j in range(0, i):
                # If the current element nums[i] is greater than nums[j]
                if nums[i] > nums[j]:
                    # Update dp[i] to be the maximum of its current value or dp[j] + 1
                    dp[i] = max(dp[i], dp[j] + 1)
            # Update maxTillNow with the maximum value in dp array
            maxTillNow = max(maxTillNow, dp[i])

        # Return the length of the longest increasing subsequence
        return maxTillNow



X = Solution()
print(X.lengthOfLIS([10,9,2,5,3,7,101,18]))


# Time Complexity : O(N*N)
# Space Complexity : O(N)


