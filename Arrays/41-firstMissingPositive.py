class Solution:
    def firstMissingPositive(self, nums) -> int:
        # Replace all negative numbers with zero
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # Use the array itself to mark the presence of numbers
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                # Mark the number as seen by negating the value at the index corresponding to the number
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                # Edge case for when the value at the index is zero
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        # Find the first positive index, which corresponds to the missing positive number
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        # If all numbers from 1 to len(nums) are present, return the next number
        return len(nums) + 1

# Example usage
X = Solution()
print(X.firstMissingPositive([1, 2, 0]))

# Time Complexity : O(N)
# Space Complexity : O(1)

