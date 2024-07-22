class Solution(object):

    def rotate_I(self, nums, k):
        # Helper function to reverse a portion of the list in-place
        def reverse(nums: list, start: int, end: int) -> None:
            while start < end:
                # Swap the elements at start and end indices
                nums[start], nums[end] = nums[end], nums[start]
                # Move towards the center
                start, end = start + 1, end - 1

        n = len(nums)
        # Handle cases where k is greater than the length of the list
        k %= n

        # Reverse the entire list
        reverse(nums, 0, n - 1)
        # Reverse the first k elements
        reverse(nums, 0, k - 1)
        # Reverse the remaining elements
        reverse(nums, k, n - 1)

        # Return the rotated list
        return nums

    def rotate_II(self, nums, k):
        # Handle cases where k is greater than the length of the list
        k = k % len(nums)
        # Perform the rotation by slicing and swapping the list parts
        nums[k:], nums[:k] = nums[:-k], nums[-k:]

        # Return the rotated list
        return nums


X =Solution()
print(X.rotate_I([1,2,3,4,5,6,7],4))
print(X.rotate_II([1,2,3,4,5,6,7],4))

# Time Complexity : O(N)
# Space Complexity : O(1)