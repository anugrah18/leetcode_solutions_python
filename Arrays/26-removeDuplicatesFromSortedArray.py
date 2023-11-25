class Solution(object):
    def removeDuplicates(self, nums):
        if (len(nums) == 0):
            return 0

        i = 0
        for j in range(1, len(nums)):
            if (nums[j] != nums[i]):
                i = i + 1
                nums[i] = nums[j]

        return i + 1

X =Solution()
print(X.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# Time complexity : O(N)

# Space complexity : O(1)