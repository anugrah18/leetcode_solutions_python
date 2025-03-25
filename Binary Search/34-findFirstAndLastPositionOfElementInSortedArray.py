class Solution:
    def searchRange(self, nums, target):
        # Find the leftmost (first) index of target
        left = self.binSearch(nums, target, True)
        # Find the rightmost (last) index of target
        right = self.binSearch(nums, target, False)

        return [left, right]

    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1  # Default index if target is not found

        while l <= r:
            m = (l + r) // 2  # Middle index

            if target > nums[m]:
                l = m + 1  # Target must be to the right
            elif target < nums[m]:
                r = m - 1  # Target must be to the left
            else:
                # Target found, record the index
                i = m
                # If we're searching for the leftmost index, keep going left
                if leftBias:
                    r = m - 1
                # Otherwise, keep going right to find the rightmost index
                else:
                    l = m + 1

        return i  # Return the found index or -1 if not found


X = Solution()
print(X.searchRange([5,7,7,8,8,10],8))

# Time Complexity : O(LogN)
# Space Complexity : O(1)