class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        maxTillNow = 1

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxTillNow = max(maxTillNow, dp[i])

        return maxTillNow


X = Solution()
print(X.lengthOfLIS([10,9,2,5,3,7,101,18]))


# Time Complexity : O(N*N)
# Space Complexity : O(N)


