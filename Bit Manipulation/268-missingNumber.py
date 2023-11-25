class Solution:
    def missingNumber(self, nums) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res

X = Solution()
print(X.missingNumber([3,0,1]))