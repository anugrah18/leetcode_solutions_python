class Solution(object):
    def moveZeroes(self, nums):
        zeroPos = 0
        for i in range(len(nums)):
            el = nums[i]
            if (el != 0):
                nums[i], nums[zeroPos] = nums[zeroPos], nums[i]
                zeroPos = zeroPos + 1

X = Solution()
nums = [1,0,2,3,5,0,7,9]
X.moveZeroes((nums))
print(nums)

# Time Complexity : O(N)
# Space Complexity : O(1)