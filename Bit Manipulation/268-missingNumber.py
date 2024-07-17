class Solution:
    def missingNumber(self, nums) -> int:
        # Initialize res to the length of nums
        res = len(nums)

        # Calculate the expected sum of indices and actual sum of nums
        for i in range(len(nums)):
            res += (i - nums[i])

        return res


X = Solution()
print(X.missingNumber([3,0,1]))

# Time Complexity : O(N)
# Space Complexity : O(1)