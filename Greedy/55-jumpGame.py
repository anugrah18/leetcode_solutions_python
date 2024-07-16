class Solution:
    def canJump(self, nums):
        # Initialize lastPos to the last index of the array
        lastPos = len(nums) - 1

        # Iterate from the second last element to the first element
        i = len(nums) - 1

        while i >= 0:
            # If the current element can reach or exceed lastPos, update lastPos to the current index
            if nums[i] + i >= lastPos:
                lastPos = i
            # Move to the previous element
            i -= 1

        # If lastPos is 0, it means we can reach the end from the start
        return lastPos == 0


X = Solution()
print(X.canJump([2,3,1,1,4]))


# Time Complexity : O(N)
# Space Complexity : O(1)
