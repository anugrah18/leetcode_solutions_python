class Solution:
    def findMin(self, nums):
        # Initialize left and right pointers for binary search
        L, R = 0, len(nums) - 1

        # Initialize result to positive infinity
        res = float('inf')

        # Perform binary search
        while L <= R:
            # If the array is already sorted, update result and exit
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            # Calculate mid index
            mid = (L + R) // 2

            # Update result with the minimum of current mid and previous result
            res = min(res, nums[mid])

            # If the left half is sorted, search in the right half
            if nums[mid] >= nums[L]:
                L = mid + 1
            # If the right half is sorted, search in the left half
            else:
                R = mid - 1

        # Return the minimum element found during the search
        return res


X= Solution()
print(X.findMin([4,5,6,7,0,1,2]))

# Time complexity : O(logN)
# Space complexity : O(1)