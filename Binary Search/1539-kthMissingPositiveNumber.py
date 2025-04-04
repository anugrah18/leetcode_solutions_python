class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        low = 0
        high = len(arr) - 1  # Set up binary search boundaries

        while low <= high:
            mid = (low + high) // 2  # Mid index of current search range

            # Calculate how many numbers are missing up to index `mid`
            # Expected value at index `mid` is `mid + 1`
            # So missing = actual_value - expected_value = arr[mid] - (mid + 1)
            missing = arr[mid] - mid - 1

            # If fewer than k numbers are missing up to `mid`,
            # we need to look to the right (increase low)
            if missing < k:
                low = mid + 1
            else:
                # Otherwise, look to the left (decrease high)
                high = mid - 1

        # After the loop, `high` is the last index where missing < k
        # The k-th missing number is `high + k + 1`
        return high + k + 1


X = Solution()
print(X.findKthPositive([2, 3, 4, 7, 11], 5))

# Time Complexity : O(logN)
# Space Complexity : O(1)
