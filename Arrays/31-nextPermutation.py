class Solution:
    def nextPermutation(self,nums):
        i = len(nums)-2

        #Find the first decreasing element from behind
        while(i>=0 and nums[i]>=nums[i+1]):
            i = i-1

        if (i >= 0):
            j = len(nums) - 1
            # Find the index of number just larger than nums[i]
            while (j >= 0 and nums[j] <= nums[i]):
                j = j - 1

            # Swapping with number just larger than nums[i]
            nums[i], nums[j] = nums[j], nums[i]

            # Reversing the numbers after i+1 index
        nums[i + 1:] = reversed(nums[i + 1:])

        return nums

X =Solution()
print(X.nextPermutation([1,2,3]))

# Time Complexity : O(N)
# Space Complexity : O(1)