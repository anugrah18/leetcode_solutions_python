class Solution:
    def search(self, nums, target):
        # Define a recursive binary search function
        def binarySearch(nums, target, i, j):
            # Calculate mid index
            mid = (i + j) // 2

            # Base case: If indices are inverted, target is not found
            if i > j:
                return -1

            # Check if the target is found at the mid index
            if target == nums[mid]:
                return mid
            # If the target is smaller, search in the left half
            elif nums[mid] > target:
                return binarySearch(nums, target, i, mid - 1)
            # If the target is larger, search in the right half
            else:
                return binarySearch(nums, target, mid + 1, j)

        # Call the binary search function with initial indices
        return binarySearch(nums, target, 0, len(nums) - 1)


X = Solution()
print(X.search([-1,0,3,5,9,12],9))

# Time Complexity : O(logN)
# Space Complexity : O(1)