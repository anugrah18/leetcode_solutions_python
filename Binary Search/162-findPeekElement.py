class Solution:
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1  # Initialize two pointers for binary search

        while l <= r:
            m = (l + r) // 2  # Calculate the middle index

            # If the middle element is smaller than its left neighbor, move left
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1  # Shift the right pointer to search in the left half

            # If the middle element is smaller than its right neighbor, move right
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1  # Shift the left pointer to search in the right half

            else:
                # If the middle element is greater than both its neighbors, it's a peak
                return m


X = Solution()
print(X.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 1 or 5 (both are valid peak indices)

# Time Complexity : O(LogN)
# Space Complexity : O(1)


