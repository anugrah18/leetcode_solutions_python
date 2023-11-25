class Solution:
    def canJump(self, nums):
        lastPos = len(nums) - 1

        i = len(nums) - 1

        while (i >= 0):
            if nums[i] + i >= lastPos:
                lastPos = i
            i -= 1

        return lastPos == 0

X = Solution()
print(X.canJump([2,3,1,1,4]))


# Time Complexity : O(N)
# Space Complexity : O(1)
