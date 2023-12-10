class Solution:
    def search(self, nums, target):
        # Initialize start and end pointers for binary search
        start, end = 0, len(nums) - 1
        # Perform binary search
        while start <= end:
            # Calculate mid index
            mid = start + (end - start) // 2
            # Check if the mid element is the target
            if nums[mid] == target:
                return mid
            # Check if the left half of the array is sorted
            elif nums[mid] >= nums[start]:
                # Check if the target is within the sorted left half
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                # If not, search in the right half
                else:
                    start = mid + 1
            # If the left half is not sorted, then the right half must be sorted
            else:
                # Check if the target is within the sorted right half
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    # If not, search in the left half
                    end = mid - 1
        # If the target is not found, return -1
        return -1

X =Solution()
print(X.search([4,5,6,7,0,1,2],0))

# Time Complexity : O(logN)
# Space Complexity : O(1)