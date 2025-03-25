class Solution:
    def checkSubarraySum(self, nums, k) -> bool:
        # Dictionary to store the first index where each remainder occurs
        # Initialized with {0: -1} to handle the case where a valid subarray starts at index 0
        remainder = {0: -1}
        total = 0  # Running prefix sum

        for i, n in enumerate(nums):
            total += n  # Update prefix sum
            r = total % k  # Compute remainder of total when divided by k

            if r not in remainder:
                # Store the first occurrence of this remainder
                remainder[r] = i
            elif i - remainder[r] > 1:
                # If the same remainder was seen before and the subarray length is at least 2
                # then subarray sum between those indices is divisible by k
                return True

        # No such subarray found
        return False

X = Solution()
print(X.checkSubarraySum([23,2,4,6,7],6))

# Time Complexity = O(N)
# Space Complexity = O(N)