class Solution:
    def jump(self, nums):
        curr_jump_end = jumps = farthest_jump = 0

        for i in range(len(nums) - 1):
            farthest_jump = max(farthest_jump, nums[i] + i)

            if i == curr_jump_end:
                jumps += 1
                curr_jump_end = farthest_jump

        return jumps

X = Solution()
print(X.jump([2,3,1,1,4]))

# Time Complexity : O(N)
# Space Complexity : O(1)
