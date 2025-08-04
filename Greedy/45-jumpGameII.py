class Solution:
    def jump(self, nums):
        # curr_jump_end: farthest index reachable with the current jump
        # jumps: number of jumps taken so far
        # farthest_jump: farthest index reachable overall at current step
        curr_jump_end = jumps = farthest_jump = 0

        # Loop through array up to the second last index
        # (we don't need to jump from the last element)
        for i in range(len(nums) - 1):
            # Update the farthest we can reach from index i
            farthest_jump = max(farthest_jump, nums[i] + i)

            # When we reach the end of the current jump's range,
            # we need to make another jump
            if i == curr_jump_end:
                jumps += 1
                curr_jump_end = farthest_jump  # update new range end

        # Return the total number of jumps needed
        return jumps


X = Solution()
print(X.jump([2,3,1,1,4]))

# Time Complexity : O(N)
# Space Complexity : O(1)
