class Solution:
    def minimumSwaps(self, nums):
        n = len(nums)

        # If there is only one element, no swaps are needed
        if n == 1:
            return 0

        min_index = 0
        max_index = 0

        # Find the indices of the minimum and maximum elements
        for i in range(n):
            if nums[i] < nums[min_index]:
                min_index = i
            if nums[i] >= nums[max_index]:
                max_index = i

        # Calculate the total number of swaps needed
        min_swaps = min_index  # Swaps to bring the minimum element to the front
        max_swaps = (n - 1 - max_index)  # Swaps to bring the maximum element to the end
        swaps = min_swaps + max_swaps

        # If the minimum index is greater than the maximum index, one swap can be avoided
        if min_index > max_index:
            swaps -= 1

        return swaps

# Example usage
X = Solution()
print(X.minimumSwaps([3, 4, 5, 5, 3, 1]))  # Output: 5

# Time Complexity: O(n), where n is the number of elements in the input list
# Space Complexity: O(1)
