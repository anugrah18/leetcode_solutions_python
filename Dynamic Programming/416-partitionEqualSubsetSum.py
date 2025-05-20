class Solution:
    def canPartition(self, nums) -> bool:
        # If total sum is odd, it's not possible to divide into two equal subsets
        if sum(nums) % 2:
            return False

        # Initialize a set to keep track of possible subset sums
        dp = set()
        dp.add(0)  # A subset with sum 0 is always possible (empty subset)

        target = sum(nums) // 2  # We want to find a subset that sums to half

        # Iterate through the numbers in reverse
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()  # Temporary set for the next state
            for t in dp:
                if (t + nums[i]) == target:  # Found a subset that adds up to target
                    return True
                nextDP.add(t + nums[i])  # Include nums[i] in the subset
                nextDP.add(t)            # Exclude nums[i] from the subset
            dp = nextDP  # Move to the next state

        # Final check after loop if target sum is in possible subset sums
        return True if target in dp else False


X = Solution()
print(X.canPartition([1,5,11,5]))

# Time Complexity = O(N*Target) , Where n is the number of elements in nums, and Target = sum(nums) // 2.
# Space Complexity = O(Target)