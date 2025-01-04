class Solution:
    def search(self, nums, target):
        # Initialize two pointers: left (l) and right (r)
        l, r = 0, len(nums) - 1
        # Perform binary search until pointers meet or cross
        while l <= r:
            mid = (l + r) // 2
            # Check if the target is found at the middle index
            if nums[mid] == target:
                return mid
            # If the target is smaller than the middle value
            # Narrow the search range to the left half
            if nums[mid] > target:
                r = mid - 1
            else:
                # If the target is greater, narrow to the right half
                l = mid + 1
        # If the target is not found, return -1
        return -1


X = Solution()
print(X.search([-1,0,3,5,9,12],9))

# Time Complexity : O(logN)
# Space Complexity : O(1)