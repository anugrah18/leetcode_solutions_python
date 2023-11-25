class Solution:
    def minMoves2(self, nums):
        nums = sorted(nums)
        N = len(nums)
        ans = 0

        if N % 2 == 1:
            median = nums[N // 2]
        else:
            median = (nums[(N // 2) - 1] + nums[(N // 2)]) // 2

        for num in nums:
            ans += abs(num - median)

        return ans

X = Solution()
print(X.minMoves2([1,10,2,9]))