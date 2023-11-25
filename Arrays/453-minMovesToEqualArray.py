class Solution:
    def minMoves(self, nums) -> int:
        nums = sorted(nums)
        count = 0
        for i in range(len(nums) - 1, 0, -1):
            count += nums[i] - nums[0]

        return count

X =Solution()
print(X.minMoves([1,2,3]))

# Time Complexity : O(NlogN)
# Space complexity : O(1)