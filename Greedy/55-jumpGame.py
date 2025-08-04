class Solution:
    def canJump(self, nums):
        # Initialize lastPos as the last index (target to reach)
        lastPos = len(nums) - 1

        # Start from the last index and move backwards
        i = len(nums) - 1

        while i >= 0:
            # Check if you can jump from index i to lastPos (or beyond)
            if nums[i] + i >= lastPos:
                # If yes, then update lastPos to current index
                # because now we need to check if we can reach this index
                lastPos = i
            # Move to the previous index
            i -= 1

        # If we managed to push lastPos all the way back to 0,
        # then we can reach the end from the start
        return lastPos == 0

X = Solution()
print(X.canJump([2,3,1,1,4]))


# Time Complexity : O(N)
# Space Complexity : O(1)
