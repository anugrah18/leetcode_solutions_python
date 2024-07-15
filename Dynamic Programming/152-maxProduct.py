class Solution:
    def maxProduct(self, nums):
        # Edge case: if the list is empty, return 0
        if len(nums) == 0:
            return 0
        # Initialize the max and min product so far to the first element
        max_so_far = nums[0]
        min_so_far = nums[0]
        # Initialize the result to the first element
        result = max_so_far
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            curr = nums[i]
            # Calculate the maximum product up to the current position
            temp_max = max(curr, curr * max_so_far, curr * min_so_far)
            # Calculate the minimum product up to the current position
            min_so_far = min(curr, curr * max_so_far, curr * min_so_far)
            # Update max_so_far with the temporary maximum
            max_so_far = temp_max
            # Update the result with the maximum product found so far
            result = max(max_so_far, result)

        return result


X = Solution()
print(X.maxProduct([2,3,-2,4]))

# Time Complexity : O(N)
# Space Complexity : O(1)

