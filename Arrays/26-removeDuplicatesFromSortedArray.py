class Solution(object):
    def removeDuplicates(self, nums):
        # If the list is empty, return 0
        if len(nums) == 0:
            return 0

        # Initialize a pointer to track the position of the last unique element
        i = 0

        # Iterate over the list starting from the second element
        for j in range(1, len(nums)):
            # If the current element is not equal to the element at pointer i
            if nums[j] != nums[i]:
                # Move the pointer i to the next position
                i = i + 1
                # Update the element at pointer i to the current element
                nums[i] = nums[j]

        # Return the length of the list with unique elements
        return i + 1


X =Solution()
print(X.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# Time complexity : O(N)

# Space complexity : O(1)