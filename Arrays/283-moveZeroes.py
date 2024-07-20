class Solution(object):
    def moveZeroes(self, nums):
        # Initialize a pointer for the position to place the next non-zero element
        ptr = 0

        # Iterate over the array
        for i in range(0, len(nums)):
            # If the current element is not zero
            if nums[i] != 0:
                # Swap the current element with the element at the ptr index
                nums[ptr], nums[i] = nums[i], nums[ptr]
                # Increment the ptr to the next position
                ptr += 1


X = Solution()
nums = [1,0,2,3,5,0,7,9]
X.moveZeroes((nums))
print(nums)

# Time Complexity : O(N)
# Space Complexity : O(1)