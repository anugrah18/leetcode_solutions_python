class Solution:
    def minMoves(self, nums) -> int:
        # Sort the list of numbers
        nums = sorted(nums)

        # Initialize the counter for the number of moves
        ans = 0
        # Initialize the index of the smallest element
        i = 0

        # Iterate from the second element to the last element
        for j in range(1, len(nums)):
            # Add the difference between the current element and the smallest element to the count
            ans += nums[j] - nums[i]

        # Return the total number of moves
        return ans


X =Solution()
print(X.minMoves([1,2,3]))

# Time Complexity : O(NlogN)
# Space complexity : O(1)